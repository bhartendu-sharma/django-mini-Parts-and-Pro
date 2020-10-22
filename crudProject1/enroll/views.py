from django.shortcuts import render,HttpResponseRedirect

from .forms import StudentRegistrationForm
from .models import User
# Create your views here.
def addAndShow(request):
    if request.method=="POST":
        stfm=StudentRegistrationForm(request.POST)
        if stfm.is_valid():
            stname=stfm.cleaned_data['name']
            stemail=stfm.cleaned_data['email']
            stpass=stfm.cleaned_data['password']
            reg=User(name=stname,email=stemail,password=stpass)
            reg.save()
            stfm=StudentRegistrationForm()
        # if stfm.is_valid():
        #     stfm.save()
    else:
        stfm=StudentRegistrationForm()
    stTable=User.objects.all()
    return render (request,'enroll/addAndShow.html',{'stForm':stfm,'stTable':stTable})


def delete_data(request,id):
    if request.method=="POST":
        pk_data=User.objects.get(pk=id)
        pk_data.delete()
        return HttpResponseRedirect('/')

def update_data(request,id):
    if request.method=="POST":
        pk_data=User.objects.get(pk=id)
        stfm=StudentRegistrationForm(request.POST,instance=pk_data)
        if stfm.is_valid():
            stfm.save()

    else:
        pk_data=User.objects.get(pk=id)
        stfm=StudentRegistrationForm(instance=pk_data)

    return render(request,'enroll/updateStudent.html',{'id':id,'stForm':stfm})