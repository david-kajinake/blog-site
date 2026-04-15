from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.models import User

def authenticate_user( request , username , password ):
    user = authenticate( request , username = username , password = password )
    return user