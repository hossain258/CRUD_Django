from django.db import models

# Create your models here.
class Student(models.Model):
    first_name= models.CharField(max_length=50, blank=True, null=True)
    Last_name= models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    phone =models.IntegerField( blank =True,null =True)
    DEPARTMENTS =(
        
        ('Music production', 'Music Production'),
        ('Software', 'Softwarte'),
        ('Computer Gaming', 'Computer Gaming'),
    )
    department = models.CharField(max_length=100,blank=True, null=True, choices= DEPARTMENTS)
    date_created =models.DateTimeField( auto_now_add=False)