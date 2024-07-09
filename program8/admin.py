from django.contrib import admin
from .models import Project, Student

# Register your models here.
class P(admin.ModelAdmin):
    list_display = ('student','duration','languages','topic')

admin.site.register(Project, P)
admin.site.register(Student)