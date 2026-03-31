import time 
# from . views import user_is_authenticated


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
            "user_language": user.settings.language,
            "user_font_size": user.settings.font_size,
            "user_theme_mode": user.settings.theme_mode, 
            }
        except Exception as e:
            user_settings = {
            "user_language": "english" ,
            "user_font_size": "medium" ,
            "user_theme_mode": "light" ,
            }

    else:
        user_settings = {
            "user_laguage":"english" , 
            "user_font_size":"medium" , 
            "user_theme_mode":"light"
        }

    return user_settings
    