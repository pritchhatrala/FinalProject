from django.shortcuts import render, redirect,get_object_or_404
from noteapp.models import *
from datetime import datetime

# Create your views here.


def admin_index(request):
    if request.method == "POST":
        username = "admin"
        password = "admin@123"

        unm = request.POST["username"]
        pas = request.POST["password"]

        if username == unm and password == pas:
            print("Login Successfully!")
            return redirect("admin_home")
        else:
            print("Error!Login faild...")
    return render(request, "admin_index.html")


def admin_home(request):
    return render(request, "admin_home.html")


def admin_userinfo(request):
    userdata = userSignup.objects.all()
    return render(request, "admin_userinfo.html",{'userdata':userdata})


def admin_notesinfo(request):
    notesinfo = Notes.objects.all()
    return render(request, "admin_notesinfo.html",{'notesinfo':notesinfo})


def notes_approve(request, id):
    notes = get_object_or_404(Notes, id=id)
    notes.status = "Approved"
    notes.updated_at = datetime.now()
    notes.save()
    print("Your notes has been approved!")

    # Email Sending

    return redirect("admin_notesinfo")


def notes_reject(request, id):
    notes = get_object_or_404(Notes, id=id)
    notes.status = "Rejected"
    notes.updated_at = datetime.now()
    notes.save()
    print("Your notes has been rejected!")
    return redirect("admin_notesinfo")