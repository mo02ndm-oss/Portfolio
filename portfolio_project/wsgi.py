import os
import sys
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

# Add the project root directory to the path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# Ensure staticfiles folder exists for WhiteNoise
os.makedirs(os.path.join(BASE_DIR, 'staticfiles'), exist_ok=True)

print(f"DEBUG: sys.path is {sys.path}")
print(f"DEBUG: CWD is {os.getcwd()}")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

# Get WSGI app object at module scope (required by Vercel Python runtime)
application = get_wsgi_application()
app = application

# Optionally run migrations at startup (if this is desired and allowed by your environment)
try:
    call_command('migrate', '--noinput', verbosity=0)
except Exception as e:
    print(f"DEBUG: Migration at WSGI startup failed: {e}")

print("DEBUG: WSGI application loaded successfully.")
