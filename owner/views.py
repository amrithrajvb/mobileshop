from django.shortcuts import render,redirect
from owner import forms
# Create your views here.

def home(request):
    if request.method=="GET":
        return render(request,"index.html")

def signup(request):
    form=forms.SignupForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.SignupForm(request.POST)
        if form.is_valid():
            firstname=form.cleaned_data["firstname"]
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password1=form.cleaned_data["password1"]
            confirmpassword=form.cleaned_data["confirmpassword"]
            print(firstname,username,email,password1,confirmpassword)
            return redirect('login')
    return render(request,"signup.html",context)

def login(request):
    form=forms.LoginForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            print(username,password)
            return redirect('items')
    return render(request,"login.html",context)

def items(request):
    return render(request,"items.html")

def addmobile(request):
    form=forms.MobileAdd()
    context={"form":form}
    if request.method=="POST":
        form=forms.MobileAdd(request.POST)
        if form.is_valid():
            mobilename=form.cleaned_data["mob_name"]
            color=form.cleaned_data["color"]
            memory=form.cleaned_data["memory"]
            camera=form.cleaned_data["camera"]
            price=form.cleaned_data["price"]
            print(mobilename,color,memory,camera,price)
            return render(request, "addphones.html", context)

    return render(request,"addphones.html",context)

def viewphone(request):
    return render(request, "viewphones.html")

def changephone(request,id):
    return render(request, "changephone.html")

def removephone(request,id):
    return render(request, "removephone.html")