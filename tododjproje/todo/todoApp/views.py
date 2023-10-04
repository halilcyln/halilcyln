from django.shortcuts import render, get_object_or_404, redirect
from todoApp.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 

# Create your views here.
def home(request, cate="all"):
    
    if cate != "all":
        post = Todo.objects.filter(category__title = cate)
    else:
        post = Todo.objects.all()
    context = {                        
        "post":post,                             
    }
    return render (request,'index.html',context)
 
def detail(request, slug_kart):
    hata = None
    form_page = Form_page.objects.filter(cate__slug = slug_kart)
    post = get_object_or_404(Todo, slug = slug_kart)
    
    
    if request.method == "POST":
            fullname = request.POST.get("name")
            text = request.POST.get("comment")
            if User.objects.filter(username = fullname):
                comment = Form_page(full_name=fullname, text=text, cate=post)
                comment.save()
                return redirect("/detail/siyaset/")
            else:
                hata = "Kayıt olmadan yorum yapamazsınız"
    context = {
        "hata":hata,
        'form_page':form_page,
        "post": post,
    }
    return render(request, 'detail.html', context)

def loginPage(request):
    hata = None
    if request.method =="POST":
        newuser = request.POST.get("username")
        newpassword = request.POST.get("password")
        newuser = authenticate(username = newuser, password = newpassword)
        if newuser is not None:
            login(request, newuser)
            return redirect("/")
        else:
            hata = "kullanıcı adı veya şifre hatalı"
    context = {
        "hata":hata
    }
    return render(request,'user/login.html',context)


def registerPage(request):
    hata = None
    if request.method =="POST":
        username = request.POST.get("username")
        newlname = request.POST.get("lname")
        newfname = request.POST.get("fname")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        email = request.POST.get("email")
        check = request.POST.get("check")
        
             
        if password1 == password2:
            if not User.objects.filter(username = username).exists():
                if not User.objects.filter(email=email).exists():
                    new_user = User.objects.create_user(username=username, first_name=newfname, last_name=newlname, email=email, password=password1)
                    new_user.save()
                    return redirect("/")
    context = {
        "hata":hata
    }
    return render (request,'user/register.html',context)


def logoutUser(request):
    logout(request)
    return redirect('/giris')