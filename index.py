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

