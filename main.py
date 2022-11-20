import os
import locale
from dotenv import load_dotenv

from django.core.management import execute_from_command_line



def main():
    load_dotenv()
    locale.setlocale(locale.LC_ALL, '')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    execute_from_command_line('manage.py runserver 0.0.0.0:8000'.split())


if __name__ == "__main__":
    main()