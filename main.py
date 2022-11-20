import os
import locale

from django.core.management import execute_from_command_line

locale.setlocale(locale.LC_ALL, '')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
execute_from_command_line('manage.py runserver 0.0.0.0:8000'.split())
