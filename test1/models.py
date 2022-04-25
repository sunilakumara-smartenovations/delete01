from django.db import models

# Create your models here.

#creating_project_code_and_name

class Project(models.Model):
    projects = models.CharField(max_length=50)
    def __str__(self):
        return self.projects


class Prj_code(models.Model):
    projects = models.ForeignKey(Project,on_delete=models.CASCADE)
    prj_code = models.TextField()
    def __str__(self):
        return self.prj_code   

class Part(models.Model):
    prj_code = models.ForeignKey(Prj_code,on_delete=models.CASCADE)
    part_num = models.CharField(max_length=50)
    def __str__(self):
        return self.part_num

class Team_member(models.Model):
    member_name = models.CharField(max_length=50)
    def __str__(self):
        return self.member_name

class Project_create(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    prj_code = models.ForeignKey(Prj_code, on_delete=models.CASCADE)
    comment = models.TextField() 
    def __str__(self):
        return str(self.project)


#assigning_project_code

#class Assign(models.Model):
#     project_name = models.ForeignKey(Project,related_name='Assign')
#     project_code = models.ForeignKey(Project,related_name='project_code')    
#     part_no = models.ForeignKey(Part, on_delete=models.SET_NULL, null=True) 
#     estimated_hour = models.TimeField()
#     team_members = models.ForeignKey(Team_members,related_name='team_members') 
#     start_date = models.DateField()
#     end_date = models.DateField()
#     comments = models.TextField()