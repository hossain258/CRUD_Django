from django.contrib import admin
from first_app.models import Student

# Register your models here.
@admin.register(Student)

class studentAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','Last_name','date_created']
