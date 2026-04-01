from django.contrib.auth import login , logout , authenticate 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render , redirect , get_object_or_404 
from django.http import HttpResponse
from . models import Post , Report , Comment  ,Author , About , UserSettings


# Create your views here.
def user_is_authenticated(user):
    user_is_valid = user.is_authenticated
    return [ user , user_is_valid] 


def home(request):
    blogs = Post.objects.all()
    user , session_authenticated = user_is_authenticated(request.user)[0] , user_is_authenticated(request.user)[1]

    if session_authenticated:
        return render(request,"blog/dashboard.html",{
            "blogs": blogs , 
            "user": user
        })
    else:
        return render(request,"blog/home.html",{
            "blogs": blogs , 
            "user": user
        })
    
    





def blogs(request):
    blogs = Post.objects.all()
    return render(request , "blog/blogs.html",{
        "blogs": blogs
    })



def post_list(request , post_id ):
    post = get_object_or_404(Post , id = post_id)
    return render(request , "blog/post_list.html" , {
        "post": post ,
        "post_id": post_id
    })

def add_report(request , post_id):
    post = get_object_or_404( Post , id = post_id  )
    if request.method == "POST":
        reporter = request.POST.get("name")
        content = request.POST.get("content")
        Report.objects.create_user(post = post , reporter = reporter , content = content)
        return redirect("post_list" , post.id)
    return render(request , "blog/post_detail.html" ,{
        "post":post,
    } )



def about_page(request):
    try:
        about = About.objects.get( about_name = "about site" )
    except Exception as e:
        about = "No About info available"
    return render( request, "blog/about.html",{
        "about": about 
    })



def pricing(request):
    return render( request, "blog/pricing.html" )

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first-name")
        other_name = request.POST.get("other-name")
        name = f"{first_name} {other_name}"
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmed_password = request.POST.get("confirm-password")
        user_to_create = User.objects.filter( username = email )
        if user_to_create.exists():
            messages.error(request , "Email already used by another user"  )
            return redirect("signup")
        if password != confirmed_password:
            messages.error(request , "Passwords do not match Please use matched passwords")
            return redirect("signup")
        try: 
            #Create a user      
            user = User.objects.create_user(
                username = email , 
                password = password
            )
            print(f"user for {user.username} created")
            #Create an author profile as a user instance
            author = Author.objects.create(
                user = user ,
                name = name ,
                email = email , 
                phone_number = phone
            )
            #Initialize user settings
            settings = UserSettings.objects.create(
                user = user , 
                #Other fields( language , theme , ... ) have default values
            )
            print(f"{author.name} with {author.phone_number} created")
            messages.success(request,"Account successfully created. login with your credentials ")
            return redirect("user_login")
        except Exception as e:
            messages.error(request , f"Error creating an account")
            return redirect("signup")

    return render(request , "blog/signup.html")


def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        #Authenticate user
        user = authenticate(request , username = email , password = password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request,"Wrong username or password.")
            return redirect("user_login")
    return render(request , "blog/login.html")

@login_required(login_url= 'user_login')
def user_logout(request):
    if request.method == "POST":  
        user = request.user
        try:
            logout(request)
            messages.info(request,"Logged out successfully")
            return redirect('home')
        except Exception as e:
            messages.info(request , f"Didn't logout , an error has occured, {e}")
            return redirect("dashboard")
    return HttpResponse("Can not logout from url input")


    




@login_required(login_url = "user_login")
def dashboard(request):
    user = Author.objects.get( user = request.user )
    try:
        associated_author = Author.objects.get()
    except Exception as e:
        associated_author = user
    return render(request , "blog/dashboard.html",{
        "user": user ,
        "author": associated_author
    })




def search(request):
    return render(request , "blog/search.html")

def add_comment(request , post_id):
    post = get_object_or_404( Post , id = post_id )
    if request.method == "POST":
        name = request.POST.get("name")
        content = request.POST.get("content")
        #save to database
        Comment.objects.create(post = post , name = name , content = content )
        return redirect("post_list" , post.id)
    return render( request , "blog/post_detail.html" , {
        "post": post
    } )

@login_required(login_url='user_login')
def my_blogs(request):
    user = request.user
    return render(request , "blog/my-blogs.html",{
        "user": user
    })

@login_required(login_url='user_login')
def profile(request):
    return render(request,"blog/profile.html")
        
@login_required(login_url='user_login')
def settings(request):
    if request.method == "POST":
        usersss = 1
    return render(request , "blog/settings.html")
