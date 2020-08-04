from django.shortcuts import redirect, render
from django.http import HttpResponse
from cvbuilder.models import SkillItem

# Create your views here.
def home_page(request):
    if request.method == 'POST' :
        SkillItem.objects.create(text=request.POST['skill'])
        return redirect('/')

    skillitems = SkillItem.objects.all()
    return render(request, 'template.html', {'skillitems': skillitems})
