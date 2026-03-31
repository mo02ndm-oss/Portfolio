import os
import sys
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

# Add the project directory to the path
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join(path, 'staticfiles'))

app = application
# Explicitly export app for Vercel
__all__ = ['app']
