from django.contrib import admin
from . models import Task

#this class allows us to display more values on the admin panel. 
#pass in the database fields that you want to be displayed then 
#pass in the class to the register function
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'created_at', 'uptaded_at')
    search_fields = ('task',)


admin.site.register(Task, TaskAdmin)