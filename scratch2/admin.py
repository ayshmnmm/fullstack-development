from django.contrib import admin

# Register your models here.
from .models import Course, Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','USN','sem')
    list_filter = ('sem',)
    search_fields = ('sem',)
    ordering = ('-USN',)
    
admin.site.register(Course)
admin.site.register(Student, StudentAdmin)
