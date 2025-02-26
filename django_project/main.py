import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
from django import setup
setup()

from app.models import Task