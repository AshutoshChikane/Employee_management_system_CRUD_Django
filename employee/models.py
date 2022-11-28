from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

def phone_num_check(value):
    if len(str(value))==10:
        return value
    else:
        raise ValidationError('Enter 10 digit Phone number!')

class employee(models.Model):
    emp_id=models.IntegerField(unique=True,null=False)
    first_name=models.CharField(max_length=50,null=False)
    last_name=models.CharField(max_length=50,null=False)
    phone=models.IntegerField(unique=True,null=False,validators=[phone_num_check])

