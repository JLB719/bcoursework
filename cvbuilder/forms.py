from django import forms

from .models import WorkExperience, School

class WorkExperienceForm(forms.ModelForm) :

    class Meta:
        model = WorkExperience
        fields = ('company', 'role', 'startdate', 'enddate', 'description',)

class SchoolForm(forms.ModelForm) :

    class Meta:
        model = School
        fields = ('school', 'startdate', 'enddate', 'qualifications')
