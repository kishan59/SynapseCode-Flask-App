from flask import Blueprint, render_template, redirect, url_for, flash, jsonify, request
from flask_login import login_required, current_user

from ..forms import SnippetForm
from ..models import Snippet
from .. import db
from datetime import datetime, timezone

snippets_bp = Blueprint('snippets', __name__)

PERPAGE = 10



@snippets_bp.route('/my_snippets')
@login_required
def my_snippets():
    page = request.args.get('page', 1, type=int)
    search_query = request.args.get('q', type=str)
    language_filter = request.args.get('language_filter', type=str)

    # query all snippets owned by the current user, ordered by created_at date
    query = Snippet.query.filter_by(user_id=current_user.id).order_by(Snippet.created_at.desc())

    # Applying search filter if a query is provided
    if search_query:
        # Splitting the search query into individual keywords 
        # & Converting to lowercase for case-insensitive matching
        keywords = search_query.lower().split() 

        # Applying AND logic for multiple keywords
        for keyword in keywords:
            # For each keyword, searching across multiple fields using ILIKE (for case-insensitive)
            query = query.filter(db.or_(
                Snippet.title.ilike(f'%{keyword}%'),
                Snippet.description.ilike(f'%{keyword}%'),
                Snippet.code_content.ilike(f'%{keyword}%'),
                Snippet.notes.ilike(f'%{keyword}%'),
                Snippet.tags.ilike(f'%{keyword}%')
            ))

    # Apply language filter if one is provided
    if language_filter:
        query = query.filter(Snippet.language.ilike(f'%{language_filter}%'))

    # Pagination
    snippets_paginated = query.paginate(page=page, per_page=PERPAGE, error_out=False)

    return render_template('snippets/my_snippets.html', 
                           snippets=snippets_paginated,
                           search_query=search_query,
                           language_filter=language_filter)


@snippets_bp.route('/<int:snippet_id>/json', methods=['GET'])
@login_required
def get_snippet_json(snippet_id):
    snippet = Snippet.query.filter_by(id=snippet_id, user_id=current_user.id).first_or_404()
    return jsonify({
        'id': snippet.id,
        'title': snippet.title,
        'code_content': snippet.code_content,
        'language': snippet.language,
        'description': snippet.description,
        'notes': snippet.notes,
        'source_url': snippet.source_url,
        'tags': snippet.tags,
        'created_at': snippet.created_at.isoformat(),
        'updated_at': snippet.updated_at.isoformat()
    })


@snippets_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_snippet():
    form = SnippetForm()

    if form.validate_on_submit():
        new_snippet = Snippet(
            title=form.title.data,
            code_content=form.code_content.data,
            language=form.language.data,
            description=form.description.data,
            notes=form.notes.data if form.notes.data else None,
            source_url=form.source_url.data if form.source_url.data else None,
            tags=form.tags.data if form.tags.data else None,
            user_id=current_user.id
        )
        db.session.add(new_snippet)
        db.session.commit()
        flash('Your snippet has been added!', 'success')
        return redirect(url_for('snippets.my_snippets'))
    
    return render_template('snippets/add_snippet.html', form=form)


@snippets_bp.route("/<int:snippet_id>/edit", methods=['GET', 'POST'])
@login_required
def edit_snippet(snippet_id):
    snippet = Snippet.query.get_or_404(snippet_id)

    if snippet.user != current_user:
        flash('You are not authorized to edit this snippet.', 'danger')
        return redirect(url_for('snippets.my_snippets'))

    form = SnippetForm()

    # Handling POST request (form submission for updates)
    if form.validate_on_submit():
        form.populate_obj(snippet)
        snippet.updated_at = datetime.now(timezone.utc)

        db.session.commit()
        flash('Your snippet has been updated!', 'success')
        return redirect(url_for('snippets.my_snippets'))

    # Handling GET request (displaying the pre-filled form)
    elif request.method == 'GET':
        form.title.data = snippet.title
        form.code_content.data = snippet.code_content
        form.language.data = snippet.language
        form.description.data = snippet.description
        form.notes.data = snippet.notes
        form.source_url.data = snippet.source_url
        form.tags.data = snippet.tags

    # Pass a custom title and legend for "Edit Snippet" context
    return render_template('snippets/add_snippet.html',
                           title=f'Edit Snippet: {snippet.title}',
                           form=form,
                           edit=True)


@snippets_bp.route("/<int:snippet_id>/delete", methods=['POST'])
@login_required
def delete_snippet(snippet_id):
    snippet = Snippet.query.get_or_404(snippet_id)

    if snippet.user != current_user:
        flash('You are not authorized to delete this snippet.', 'danger')
        return redirect(url_for('snippets.my_snippets'))

    db.session.delete(snippet)
    db.session.commit()
    flash('Your snippet has been deleted!', 'success')

    # For AJAX requests, sending a JSON response
    if request.is_json:
        return jsonify({'message': 'Snippet deleted successfully!'}), 200

    return redirect(url_for('snippets.my_snippets'))
