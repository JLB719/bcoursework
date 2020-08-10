from django.shortcuts import redirect, render
from django.http import HttpResponse
from cvbuilder.models import SkillItem, AchItem, WorkExperience, School
from cvbuilder.forms import WorkExperienceForm, SchoolForm

# Create your views here.
def home_page(request):
    if request.method == 'POST' :
        if request.POST.get('skill', ''):
            SkillItem.objects.create(text=request.POST['skill'])
            return redirect('/')

        elif request.POST.get('achievement', '') :
            AchItem.objects.create(text=request.POST['achievement'])
            return redirect('/')
        elif request.POST.get('WorkSubmit', '') :
            WorkExperience.objects.create(company=request.POST['placeofwork'], role=request.POST['role'], startdate=request.POST['startdatew'], enddate=request.POST['enddatew'], description=request.POST['description'])
            return redirect('/')
        elif request.POST.get('EducationSubmit', '') :
            School.objects.create(school= request.POST['school'], startdate=request.POST['startdates'], enddate=request.POST['enddates'], qualifications=request.POST['grades'])
            return redirect('/')


    skillitems = SkillItem.objects.all()
    achitems = AchItem.objects.all()
    nameitems = request.POST.get('name', '')
    emailitems = request.POST.get('email', '')
    numberitems = request.POST.get('number', '')
    personalitems = request.POST.get('personalprof', '')
    workitems= WorkExperience.objects.all()
    schoolitems=School.objects.all()

    return render(request, 'template.html', {'skillitems': skillitems, 'achitems': achitems, 'name_item': nameitems,
    'email_item' : emailitems, 'number_item': numberitems, 'profile_item':personalitems,
    'workitems': workitems, 'schoolitems':schoolitems})
