# coding=utf-8 ##以utf-8编码储存中文字符
#!/usr/bin/env python
import os
import sys
from testdemo import execute_from_command
if __name__ == "__main__":
    # manage.py self call,will be print __main__
    execute_from_command(sys.argv)
    print(__name__)
    print(os.path.abspath(__file__))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testdemo.settings")
    # If key is in the dictionary, return its value. If not, insert key with a value of default and return default. default defaults to None.
    print(os.environ.get('DJANGO_SETTINGS_MODULE'))#os.environ is dict mysite.settings
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        #避免掩盖
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
    # execute_from_command_line call ManagementUtility.execute method
    #
