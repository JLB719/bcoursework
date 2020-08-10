from django.db import models

# Create your models here.
class SkillItem(models.Model) :
    text = models.TextField(default='')

class AchItem(models.Model) :
    text = models.TextField(default='')

class NameItem(models.Model) :
    text = models.TextField(default='')

class WorkExperience(models.Model) :
    company = models.TextField(default='')
    role = models.TextField(default = '')
    startdate = models.TextField(default = '')
    enddate = models.TextField(default='')
    description = models.TextField(default='')

class School(models.Model) :
    school = models.TextField(default='')
    startdate = models.TextField(default='')
    enddate = models.TextField(default='')
    qualifications = models.TextField(default = '')
