import datetime


from django.test import TestCase

# Create your tests here.
from django.utils import timezone

print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# print(timezone.now())