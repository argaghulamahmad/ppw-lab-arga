#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "draft_lab.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "praktikum.settings")
>>>>>>> b80a2738b5018e63cdf9fdc4a7f28364875518a0
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
<<<<<<< HEAD
=======
        # The above import may fail for some other reason. Ensure that the
>>>>>>> b80a2738b5018e63cdf9fdc4a7f28364875518a0
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
