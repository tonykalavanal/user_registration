from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models


def home(request):
    return render(request, 'home.html')

def saveregistration(request):
    varfname = request.POST['fname']
    varlname = request.POST['lname']
    varemail = request.POST['email']
    varpassword = request.POST['password']
    varphone = request.POST['phone']
    varcollege = request.POST['college']
    objuser = models.UserDetails(
        fname = varfname,
        lname = varlname,
        email = varemail,
        password = varpassword,
        phone = varphone,
        college = varcollege
    )
    objuser.save()
    return redirect("/")
