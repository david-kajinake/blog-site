document.addEventListener("DOMContentLoaded",(e)=>{
    //Get html elements
    let body = document.querySelector("body");

    function applyFontSize(fontSize){
        body.style.fontSize = fontSize
    }
    function applyTheme(themeName){
        if( themeName === "dark" ){
        //Change the html elements to dark
        body.classList.add("dark-theme");
        body.classList.remove("light-theme");
        }
        else if( themeName === "dark" ){
         //Change the html elements to 
         body.classList.add("light-theme");
         body.classList.remove("dark-theme");
        }
        console.log(themeName , " Applied");
    }

    const userSettings = JSON.parse( document.getElementById("user_settings_config").textContent );
    let userLanguage = userSettings.user_language;
    let userThemeMode = userSettings.user_theme_mode;
    let userFontSize =userSettings.user_font_size;
    console.log( userLanguage , userThemeMode , userFontSize );

    function applyAllSettings(){
        applyFontSize(userFontSize);
        applyTheme(userThemeMode);
    }    

    applyAllSettings();
    
});