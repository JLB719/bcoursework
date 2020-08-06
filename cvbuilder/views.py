from django.shortcuts import redirect, render
from django.http import HttpResponse
from cvbuilder.models import SkillItem, AchItem, NameItem

# Create your views here.
def home_page(request):
    if request.method == 'POST' :
        if request.POST.get('skill', ''):
            SkillItem.objects.create(text=request.POST['skill'])
            return redirect('/')

        elif request.POST.get('achievement', '') :
            AchItem.objects.create(text=request.POST['achievement'])
            return redirect('/')



    skillitems = SkillItem.objects.all()
    achitems = AchItem.objects.all()
    nameitems = request.POST.get('name', '')
    emailitems = request.POST.get('email', '')
    numberitems = request.POST.get('number', '')
    personalitems = request.POST.get('personalprof', '')

    return render(request, 'template.html', {'skillitems': skillitems, 'achitems': achitems, 'name_item': nameitems,
    'email_item' : emailitems, 'number_item': numberitems, 'profile_item':personalitems})
