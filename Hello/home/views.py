from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from home.models import Contact

# Create your views here.
def index(request):
    context = {
        "variable":"This is the messaege that is being sent"
    }
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')


def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        description = request.POST.get("description")
        contact = Contact(name = name , email = email , phone = phone , description= description , date = datetime.today())
        contact.save() 

    return render(request,'contact.html')