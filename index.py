import os
import sys
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

# Get the directory of this file (the root directory)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Add the root directory to the Python path
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

# Get WSGI application at module scope
application = get_wsgi_application()
app = application

# Run migrations at startup of the lambda
try:
    print("DEBUG: Attempting runtime migrations...")
    call_command('migrate', '--noinput', verbosity=0)
    print("DEBUG: Runtime migrations successful.")
    
    # Temporary superuser creation for persistent DB setup
    from django.contrib.auth.models import User
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123456')
        print("DEBUG: Superuser 'admin' created successfully.")
except Exception as e:
    print(f"DEBUG: Runtime migration failed: {e}")

print("DEBUG: WSGI application loaded successfully.")
