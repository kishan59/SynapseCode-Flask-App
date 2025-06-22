from app import create_app

# This is the actual WSGI application object that Gunicorn will serve
app = create_app()