from django.shortcuts import redirect, render
from django.http import HttpResponse
from cvbuilder.models import *
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
        elif request.POST.get('name', '') :
            NameItem.objects.create(text=request.POST['name'])
            return redirect('/')
        elif request.POST.get('email', '') :
            EmailItem.objects.create(text=request.POST['email'])
            return redirect('/')
        elif request.POST.get('number', '') :
            NumberItem.objects.create(text=request.POST['number'])
            return redirect('/')
        elif request.POST.get('personalprof', '') :
            PersonalProfileItem.objects.create(text=request.POST['personalprof'])
            return redirect('/')
        elif request.POST.get('qualification', '') :
            Qualifications.objects.create(text=request.POST['qualification'])
            return redirect('/')
        elif request.POST.get('ProjectSubmit', '') :
            Projects.objects.create(title=request.POST['projectover'], description=request.POST['Projectdes'])
            return redirect('/')
        elif request.POST.get('Notes','') :
            Notes.objects.create(note=request.POST['Notes'])
            return redirect('/')



    skillitems = SkillItem.objects.all()
    achitems = AchItem.objects.all()
    nameitems = NameItem.objects.all().last()
    emailitems = EmailItem.objects.all().last()
    numberitems = NumberItem.objects.all().last()
    personalitems = PersonalProfileItem.objects.all().last()
    workitems= WorkExperience.objects.all()
    schoolitems=School.objects.all()
    qualificationitems = Qualifications.objects.all()
    projectitems= Projects.objects.all()
    noteitems = Notes.objects.all()

    return render(request, 'template.html', {'skillitems': skillitems, 'achitems': achitems,
    'nameitems': nameitems,'emailitems' : emailitems,
    'numberitems': numberitems, 'personalitems':personalitems,
    'workitems': workitems, 'schoolitems':schoolitems,
    'qualificationitems':qualificationitems, 'projectitems' : projectitems,
    'noteitems' : noteitems,
    })
