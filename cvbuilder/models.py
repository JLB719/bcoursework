from django.db import models

# Create your models here.
class SkillItem(models.Model) :
    skill = models.TextField(default='')

class AchievmentItem(models.Model) :
    achievment = models.TextField(defalut='')

class PersonalProfileItem(models.Model) :
    profile = models.TextField(default='')

class DetailsItems(models.Model) :
    name = models.TextField(default='')
    email = models.TextField(default='')
    number = models.TextField(default='')

class SchoolItems(models.Model) :
    school = models.TextField(default='')
    startdate = models.TextField(default='')
    enddate = models.TextField(default='')
    details = models.TextField(default='')

class WorkItems(models.Model) :
    jobtitle = models.TextField(default='')
    jobrole = models.TextField(default='')
    jobdescription = models.TextField(default='')
    jobstartdate = models.TextField(default='')
    jobenddate = models.TextField(default='')
