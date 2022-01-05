from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    # null and blank are commonly used together in this fashion so that a form
    # allows an empty value and the database stores that value as NULL.
'''
A common gotcha to be aware of is that the field type dictates how to use these values.
 Whenever you have a string-based field like CharField or TextField, setting both null and 
 blank as we’ve done will result in two possible values for “no data” in the database. 
 Which is a bad idea. The Django convention is instead to use the empty string '', not NULL.
'''