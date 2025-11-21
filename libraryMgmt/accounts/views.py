from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from .forms import CustomRegisterForm
from .models import CustomUser
from books.models import Book, BookRequest
# Create your views here.




def register (request):
    if request.method =="POST":
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.is_staff=False
            user.is_superuser= False

            user.save()
            login(request,user)
            return redirect('user_dashboard')
    else:
        form =CustomRegisterForm()

    return render(request, 'accounts/register.html',{'form':form}) 

def login_user(request):
    context={}
    if request.method=="POST":
        username = request.POST['username']
        password= request.POST['password']

        user = authenticate(request,username=username,password=password)
        if user:

            login  (request,user)
            if user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('user_dashboard')

        
        else:
            context['error']= "Invalid username or password"

    return render (request, 'accounts/login.html',context)    

def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html')

def user_dashboard (request):
    return render(request,'accounts/user_dashboard.html')

def logout_user(request):
    logout(request)
    return redirect('login')

# manage usersss 

def manage_users(request):
    users = CustomUser.objects.filter(is_superuser= False)
    return render(request, 'accounts/manage_users.html',{'users':users})

def add_user (request):
    if request.method=='POST':
        username = request.POST.get("username")
        email =  request.POST.get('email')
        password= request.POST.get('password')


        CustomUser.objects.create_user(
            username = username ,
            email= email,
            password = password

    )
        return redirect("manage_users")
    return render (request, "add_user.html")

def edit_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == "POST":
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.save()
        return redirect("manage_users")

    return render(request, "accounts/edit_user.html", {"user": user})

def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    return redirect("manage_users")


# book mgmnt
