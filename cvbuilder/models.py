from django.db import models

# Create your models here.
class SkillItem(models.Model) :
    text = models.TextField(default='')

class AchItem(models.Model) :
    text = models.TextField(default='')

class NameItem(models.Model) :
    text = models.TextField(default='')
