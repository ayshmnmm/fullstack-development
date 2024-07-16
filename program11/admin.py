from django.contrib import admin
from .models import Student, Course

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['usn', 'name', 'sem']
    list_filter = ['sem']
    search_fields = ['usn', 'name']
    filter_horizontal = ['courses']
    
admin.site.register(Student, StudentAdmin)
admin.site.register(Course)
