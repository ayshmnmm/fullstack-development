from django.contrib import admin

# Register your models here.
from .models import Course,Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('usn', 'name', 'sem')
    list_filter = ['sem']
    search_fields = ['name', 'usn']
    ordering = ['name']

class CourseAdmin(admin.ModelAdmin):
    list_display = ('cid', 'cname')
    search_fields = ['cname']

admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
