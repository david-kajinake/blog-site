/* GLOBAL CONFIGURATIONS */

document.addEventListener("DOMContentLoaded",(e)=>{
    //Get html elements
    let body = document.querySelector("body");

    function applyFontFamily( fontName ){
        body.style.fontFamily = fontName;
    }
    function applyFontSize(fontSize){
        body.style.fontSize = fontSize;
    }
    function applyTheme(themeName){
        if( themeName === "dark" ){
        //Change the html elements to dark
        body.classList.add("dark-theme");
        body.classList.remove("light-theme");
        }
        else if( themeName === "light" ){
         //Change the html elements to 
         body.classList.add("light-theme");
         body.classList.remove("dark-theme");
        }
    }

    const userSettings = JSON.parse( document.getElementById("user_settings_config").textContent );
    let userLanguage = userSettings.user_language;
    let userThemeMode = userSettings.user_theme_mode;
    let userFontSize =userSettings.user_font_size;
    let userFontFamily = userSettings.user_font_family
    let userSettingsStatus = userSettings.user_settings_status;
    console.log( userLanguage , userThemeMode , userFontSize , userSettingsStatus );


    function applyAllSettings(){
        applyFontFamily(userFontFamily);
        applyFontSize(userFontSize);
        applyTheme(userThemeMode);
    }    

    applyAllSettings();
    
});