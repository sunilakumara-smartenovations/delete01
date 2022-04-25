from django.contrib import admin
from . models import Project,Prj_code,Project_create,Part,Team_member

# Register your models here.
admin.site.register(Project)
admin.site.register(Prj_code)

admin.site.register(Part)
admin.site.register(Team_member)

class Project_create_admin(admin.ModelAdmin):
    list_display = ('project_name','prj_code','comment')    
admin.site.register(Project_create)
#admin.site.register(Prj_code),