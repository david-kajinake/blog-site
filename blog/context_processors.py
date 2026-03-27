import time 

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