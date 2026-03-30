from django.contrib.auth import login , authenticate 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render , redirect , get_object_or_404 
from django.http import HttpResponse
from . models import Post , Report , Comment  ,Author , About   


# Create your views here.
def user_is_authenticated(user):
    user_is_valid = user.is_authenticated
    return [ user , user_is_valid] 


def home(request):
    # user = request.user
    # posts = Post.objects.all()
    # if user.is_authenticated:
    #     return render(request,"blog/dashboard.html",{
    #         "blogs": blogs , 
    #         "user": user ,
    #     })
    # else:
    #     return render(request , "blog/home.html",{
    #         "posts": posts
    #     })
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
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmed_password = request.POST.get("confirm_password")
        user_exists = User.objects.filter( username = email )
        if user_exists.exists():
            messages.error(request , "Email already used by another user"  )
            return redirect("signup")
        if password != confirmed_password:
            messages.error(request , "Passwords do not match Please user matched passwords")
            return redirect("signup")
        try: 
            #Create a user      
            user = User.objects.create_user(
                username = email , 
                password = password
            )
            print(f"user for {user.username} created")
            author = Author.objects.create(
                user = user ,
                name = name ,
                email = email , 
                phone_number = phone
            )
            print(f"{author.name} with {author.phone_number} created")
            messages.success(request,"Account successfully created. You will be redirected to the login page to login with your credentials ")
            return redirect("user_login")
        except Exception as e:
            messages.error(request , f"Error creating an account: {e}")

    return render(request , "blog/signup.html")


def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        #Authenticate user
        user = authenticate(request , username = email , password = password)
        if user is not None:
            is_loggedin = True
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request,"Wrong username or password.")
            return redirect("user_login")
        
    return render(request , "blog/login.html")

@login_required(login_url = "user_login")
def dashboard(request):
    user = Author.objects.get( user = request.user )
    return render(request , "blog/dashboard.html",{
        "user": user
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
        