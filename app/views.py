from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def djforms(request):
    SUFO=SignUpForm()
    d={'SUFO':SUFO}
    if request.method=='POST':
        SUFDT=SignUpForm(request.POST)
        if SUFDT.is_valid():
            n=SUFDT.cleaned_data['name']
            return HttpResponse(str(SUFDT.cleaned_data))
                
    return render(request,'djforms.html',d)
