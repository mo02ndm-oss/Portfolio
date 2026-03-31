import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project root directory to the path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

print(f"DEBUG: sys.path is {sys.path}")
print(f"DEBUG: CWD is {os.getcwd()}")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

try:
    application = get_wsgi_application()
    app = application
    print("DEBUG: WSGI application loaded successfully.")
except Exception as e:
    print(f"DEBUG: Failed to load WSGI application: {e}")
    raise
