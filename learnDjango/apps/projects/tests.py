from os import environ

from django.test import TestCase

# Create your tests here.
print(environ.get('CYGWIN'))