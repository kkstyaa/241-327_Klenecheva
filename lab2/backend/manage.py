import os #работа с ОС
import sys #доступ к аргументам КС


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab1.settings') #УКАЗЫВАЕТ КАКОЙ ФАЙЛ НАСТРЕОК ИСПОЛЬЗОВАТЬ 
    #проверка наличия django
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv) #аргументы переданные в КС


if __name__ == '__main__':
    main()
