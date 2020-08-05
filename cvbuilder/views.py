from django.shortcuts import redirect, render
from django.http import HttpResponse
from cvbuilder.models import SkillItem, AchItem

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

    return render(request, 'template.html', {'skillitems': skillitems, 'achitems': achitems})
