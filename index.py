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

# Run migrations at startup of the lambda (in /tmp/db.sqlite3 if Vercel)
try:
    print("DEBUG: Attempting runtime migrations...")
    call_command('migrate', '--noinput', verbosity=0)
    print("DEBUG: Runtime migrations successful.")
    
    # Create superuser if it doesn't exist (only on Vercel ephemeral DB)
    if os.environ.get('VERCEL'):
        from django.contrib.auth.models import User
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123456')
            print("DEBUG: Ephemeral superuser 'admin' created (password: admin123456)")
except Exception as e:
    print(f"DEBUG: Runtime migration/superuser failed: {e}")

print("DEBUG: WSGI application loaded successfully.")
