from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views her

def home(request):
    return render(request,'play.html')


def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}
    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            NSUO=ufd.save(commit=False)
            password=ufd.cleaned_data['password']
            NSUO.set_password(password)
            NSUO.save()
            NSPO=pfd.save(commit=False)
            NSPO.username=NSUO
            NSPO.save()
            send_mail('Registratioon',"SUCCESSFULLY REGISTERED IN AHA",'gollavishnuyadav2@gmail.com',[NSUO.email],fail_silently=False)
            return HttpResponse('Regsitration is Susssessfulll')
        else:
            return HttpResponse('Not valid')
        
    return render(request,'registration.html',d)

