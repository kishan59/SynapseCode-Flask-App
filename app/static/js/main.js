// app/static/js/main.js

document.addEventListener('DOMContentLoaded', function() {
    // footer current year dynamic...
    document.getElementById('footer-year').innerHTML = new Date().getFullYear();
    // ...

    const snippetModal = new bootstrap.Modal(document.getElementById('snippetModal'));
    const modalTitle = document.getElementById('modalSnippetTitle');
    const modalLanguage = document.getElementById('modalSnippetLanguage');
    const modalCreatedAt = document.getElementById('modalSnippetCreatedAt');
    const modalUpdatedAt = document.getElementById('modalSnippetUpdatedAt');
    const modalDescription = document.getElementById('modalSnippetDescription');
    const modalCode = document.getElementById('modalSnippetCode');
    const modalNotes = document.getElementById('modalSnippetNotes');
    const modalSourceUrl = document.getElementById('modalSnippetSourceUrl');
    const modalTags = document.getElementById('modalSnippetTags');
    const modalEditBtn = document.getElementById('modalEditBtn');
    const modalDeleteBtn = document.getElementById('modalDeleteBtn'); 

    // Attaching event listener to all "View Code" buttons
    document.querySelectorAll('.view-code-btn').forEach(button => {
        button.addEventListener('click', function() {
            const snippetId = this.dataset.snippetId;

            modalDeleteBtn.dataset.snippetId = snippetId;
            modalEditBtn.href = `/snippets/${snippetId}/edit`; 

            fetch(`/snippets/${snippetId}/json`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    modalTitle.innerText = data.title;
                    modalLanguage.innerText = data.language;
                    modalCreatedAt.innerText = new Date(data.created_at).toLocaleString();
                    modalUpdatedAt.innerText = new Date(data.updated_at).toLocaleString();
                    modalDescription.innerText = data.description;
                    modalNotes.innerText = data.notes || 'N/A';
                    modalSourceUrl.href = data.source_url || '#';
                    modalSourceUrl.innerText = data.source_url || 'N/A';
                    if (!data.source_url) {
                        modalSourceUrl.classList.add('pe-none');
                    } else {
                        modalSourceUrl.classList.remove('pe-none');
                    }
                    modalTags.innerText = data.tags || 'N/A';

                    modalCode.textContent = data.code_content;
                    modalCode.className = `language-${data.language.toLowerCase()}`;

                    Prism.highlightElement(modalCode);
                })
                .catch(error => {
                    console.error('Error fetching snippet:', error);
                    alert('Could not load snippet details. Please try again.');
                });
        });
    });


    // Handle Delete button click in the modal
    modalDeleteBtn.addEventListener('click', function() {
        const snippetIdToDelete = this.dataset.snippetId;

        if (confirm('Are you sure you want to delete this snippet? This action cannot be undone.')) {
            fetch(`/snippets/${snippetIdToDelete}/delete`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                flashMessage(data.message || 'Snippet deleted successfully!', 'success');
                snippetModal.hide();
                location.reload();
            })
            .catch(error => {
                console.error('Error deleting snippet:', error);
                flashMessage('Failed to delete snippet: ' + error.message, 'danger');
            });
        }
    });


    // Handle Delete button click on the card directly
    document.querySelectorAll('.delete-snippet-btn').forEach(button => {
        button.addEventListener('click', function() {
            const snippetIdToDelete = this.dataset.snippetId;
            const cardElement = this.closest('.col');

            if (confirm('Are you sure you want to delete this snippet? This action cannot be undone.')) {
                fetch(`/snippets/${snippetIdToDelete}/delete`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                })
                .then(response => {
                    if (!response.ok) {
                        return response.json().then(errorData => {
                            throw new Error(errorData.message || `HTTP error! status: ${response.status}`);
                        }).catch(() => {
                            throw new Error(`HTTP error! status: ${response.status}`);
                        });
                    }
                    return response.json();
                })
                .then(data => {
                    flashMessage(data.message || 'Snippet deleted successfully!', 'success');
                    location.reload();
                })
                .catch(error => {
                    console.error('Error deleting snippet:', error);
                    flashMessage('Failed to delete snippet: ' + error.message, 'danger');
                });
            }
        });
    });


    // Helper function to simulate Flask's flash messages (for AJAX success/error)
    function flashMessage(message, category) {
        const flashContainer = document.querySelector('.container .alert-container') || document.querySelector('.container');
        if (!flashContainer) return;

        const alertDiv = document.createElement('div');
        alertDiv.className = `alert alert-${category} alert-dismissible fade show mt-3`;
        alertDiv.setAttribute('role', 'alert');
        alertDiv.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        `;
        flashContainer.prepend(alertDiv);
        setTimeout(() => alertDiv.classList.remove('show'), 5000);
    }


});