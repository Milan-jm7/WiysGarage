from tempfile import template

from django.contrib.auth.hashers import check_password
from django.shortcuts import render,redirect
from .models import Registration
# Create your views here.
from django.shortcuts import render

def home(request):
    if request.session["id"]:
     return render(request, 'Home.html')  # Replace 'my_template.html' with your actual template filename

def paintdent(request):
    return render(request,'paintdent.html')
def callback(request):
    return render(request,'Rqst.html')
def booking(request):
    return render(request,'book.html')
def diagnostics(request):
    return render(request,'diagtic.html')
def lube(request):
    return render(request,'lube.html')



def signup(request):
    if request.method == 'POST':
        user_obj = Registration()
        user_obj.Name = request.POST.get("name")
        user_obj.Username = request.POST.get("username")
        user_obj.MobileNumber = request.POST.get("number")
        user_obj.Email = request.POST.get("email")
        user_obj.password = request.POST.get("password")
        user_obj.save()
        return render(request, "login.html")
    return render(request, "signup.html")

def login(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = Registration.objects.get(Email=email , password=password)
            print(user)
            if user:
                request.session['id'] = user.id
                return redirect('/home/')
        except Registration.DoesNotExist:
            return render(request, "login.html", {'error': 'invalid email or password'})
    return render(request, "login.html")



def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        new_password = request.POST.get("password")
        try:
            user = Registration.objects.get(Email=email)
            user.password=new_password
            user.save()
            return render(request, "login.html")
        except Registration.DoesNotExist:
            return render(request, "forgot.html", {"error": "Email not found"})

    return render(request, "forgot.html")


