document.addEventListener("DOMContentLoaded",()=>{
    const userSettings = JSON.parse( document.getElementById("user_settings_config").textContent);
    const supportedLanguages = JSON.parse( document.getElementById("supported_languages").textContent );
    const themeSelect = document.getElementById("theme");
    const languageSelect = document.getElementById("language");
    const currentSelectedLanguage = userSettings.user_language;

    for( const [language , value] of Object.entries(supportedLanguages) ){
        let languageOption = document.createElement("option");
        languageOption.textContent = language;
        languageOption.value = value;
        languageSelect.appendChild(languageOption);
        console.log(language , " Appended");
        if( value === currentSelectedLanguage ){
            languageOption.selected = true;
        }
    }

});




