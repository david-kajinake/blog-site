import json
from django.contrib.auth import login , logout , authenticate 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render , redirect , get_object_or_404 
from django.http import HttpResponse , JsonResponse
from . models import Post , Report , Comment  ,Author , About , UserSettings
from services.authentication import authentication


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
    post = get_object_or_404(Post , post_id = post_id)
    return render(request , "blog/post_list.html" , {
        "post": post ,
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
        user = authentication.authenticate_user( request , email , password )
        
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

@login_required( login_url= 'user_login' )
def create_new_blog( request):
    user , session_is_authenticated = user_is_authenticated(request.user)[0] , user_is_authenticated(request.user)[1]
    user = user
    if session_is_authenticated:
        if request.method == "POST":
            try:
                post_title = request.POST.get("title")
                post_content = request.POST.get("content")
                post_image = request.FILES.get("image")
                post = Post.objects.create(
                    title = post_title , 
                    content = post_content , 
                    image = post_image , 
                    author = user.author ,
                )
                return JsonResponse({"result":"created successfully"}, status = 201 )
            except Exception as e:
                return JsonResponse({"error":f"error occured: {e} "} , status = 400 )

        return redirect("home")   
    return render(request , "blog/home.html")





def search(request):
    return render(request , "blog/search.html")

def add_comment(request , post_id):
    post = get_object_or_404( Post , id = post_id )
    if request.method == "POST":
        name = request.POST.get("name")
        content = request.POST.get("content")
        #save comment to database
        Comment.objects.create(post = post , name = name , content = content )
        return redirect("post_list" , post.id)
    return render( request , "blog/post_detail.html" , {
        "post": post
    } )

@login_required(login_url='user_login')
def my_blogs(request):
    user = request.user
    author = Author.objects.get( user = user )
    total_blogs = author.posts.count()
    return render(request , "blog/my-blogs.html",{
        "user": user , 
        "author": author ,
        "total_posts": total_blogs ,
    })

@login_required(login_url='user_login')
def profile(request):
    return render(request,"blog/profile.html")
        
@login_required(login_url='user_login')
def settings(request):
    user , session_authenticated = user_is_authenticated(request.user)[0] , user_is_authenticated(request.user)[1]
    settings = UserSettings.objects.get(user = user )
    if session_authenticated:
        if request.method == "POST":
            try:
                data = json.loads(request.body)
                prefered_theme = data.get( "prefered_theme" )
                prefered_font_family = data.get("prefered_font_family")
                prefered_font_size = data.get("prefered_font_size")
                prefered_language = data.get("prefered_language")
                settings.theme_mode = prefered_theme
                settings.font_family = prefered_font_family
                settings.font_size = prefered_font_size
                settings.language = prefered_language
                settings.save()
                return JsonResponse({"status: ok"})
            except Exception as e:
                print(f"Error: {e}")
                return JsonResponse({"status":"error","message": str(e)},status = 400)
        return render(request,"blog/settings.html")
    return render(request , "blog/home.html")


@login_required(login_url='user_login')
def applySettings(request):

    return render(request , "blog/home.html")

