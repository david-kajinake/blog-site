import time 
# from . views import user_is_authenticated -> Imported down in the get_user_and_settings() function to circular import error with models.py


def get_time():
    local_time = time.localtime()
    current_second = local_time.tm_sec
    current_minute = local_time.tm_min
    current_weekday = local_time.tm_wday
    current_month = local_time.tm_mon
    current_monthday = local_time.tm_mday
    current_year = local_time.tm_year
    return f"{current_second}{current_minute}{current_weekday}{current_month}{current_monthday}{current_year}"

def css_js_latest(request):
    latest =  get_time()
    return{
        "css_latest": latest , 
        "js_latest": latest
    }

def get_user_and_settings(request):
    from . views import user_is_authenticated
    user , session_authenticated = user_is_authenticated(request.user)[0] , user_is_authenticated(request.user)[1]
    if session_authenticated: 
        try:   
            user_settings = {
            "user_language": user.settings.language ,
            "user_font_family": user.settings.font_family ,
            "user_font_size": user.settings.font_size ,
            "user_theme_mode": user.settings.theme_mode , 
            "user_settings_status": "As Prefered"
            }
        except Exception as e:
            user_settings = {
            #Default configurations
            "user_language": "english" ,
            "user_font_size": "medium" ,
            "user_theme_mode": "light" ,
            "user_font_family": "sans-serif",  
            "user_settings_status":f"Exception: {e}"          
            }

    else:
        #For unauthenticated users( return default settings )
        user_settings = {
            "user_laguage":"english" , 
            "user_font_size":"medium" , 
            "user_theme_mode":"light" , 
            "user_settings_status": "Defaults for Unauthenticated",

        }

    return{ "user_preference": user_settings }

def supported_theme_mode(request):
    themes = {
        "🌞Light Mode":"light" , 
        "🌙Dark mode":"dark" ,
    }
    return { "supported_theme_mode":themes }


def supported_font_families(request):
    fonts = {
        "sans-serif":"sans-serif" , 
        "Courier New":"Courier New",
        "Courier":"Courier",
        "monospace":"monospace",
        "Franklin Gothic Medium":"Franklin Gothic Medium",
        "Arial Narrow":"Arial Narrow",
        "Arial":"Arial",
        "Gill Sans":"Gill Sans",
        "Gill Sans MT":"Gill Sans MT",
        "Calibri":"Calibri",
        "Trebuchet MS":"Trebuchet MS",
        "Segoe UI":"Trebuchet MS",
        "Tahoma":"Trebuchet MS",
        "Geneva":"Trebuchet MS",
        "Verdana":"Trebuchet MS",
        "Helvetica":"Trebuchet MS",
        "Impact":"Impact",
        "Haettenschweiler":"Haettenschweiler",
        "Arial Narrow Bold":"Haettenschweiler",
    }
    return {"supported_font_families":fonts}


def supported_font_sizes(request):
    font_sizes = {
        "Smaller":"smaller",
        "Small":"small",
        "Medium":"meduim",
        "Large":"large" ,
        "Larger":"larger"
    }
    return{ "supported_font_sizes":font_sizes }


def supported_languages(request):
    languages = {
        "English":"english" , 
        "Swahili":"swahili" , 
        "Francais":"francais",
    }  
    return {"supported_languages":languages}
