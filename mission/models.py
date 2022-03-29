from turtle import title
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
# MINISTRY VISION, MISSION & OBJECTIVES
class top_title(models.Model):
    top_title01 = models.CharField(max_length=200)

# VISION
class vision(models.Model):
    title = models.CharField(max_length=200)
    vision_description = RichTextField(blank=True)

# MISSION
class mission(models.Model):
    title = models.CharField(max_length=200)
    mission_description = RichTextField(blank=True)

# OBJECTIVES
class objective(models.Model):
    title = models.CharField(max_length=200)
    objective_description = RichTextField(blank=True)

# ONGOING PROJECTS
class ongoing_project(models.Model):
    top_title = models.CharField(max_length=200)
    project_top_description = RichTextField(blank=True)

class project(models.Model):
    SI_No = models.IntegerField()
    Project_Title = models.CharField(max_length=200)
    Project_Objective = RichTextField(blank=True)
    Project_Duration = models.IntegerField()
    Progress = models.IntegerField()


   

