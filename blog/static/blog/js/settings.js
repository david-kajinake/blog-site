

document.addEventListener("DOMContentLoaded",()=>{

    const userSettings = JSON.parse( document.getElementById("user_settings_config").textContent);
    const supportedLanguages = JSON.parse( document.getElementById("supported_languages").textContent);
    const supportedFonts = JSON.parse( document.getElementById("supported_fonts").textContent);
    const supportedThemes = JSON.parse( document.getElementById("supported_themes").textContent );
    const supportedFontSizes = JSON.parse( document.getElementById("supported_font_sizes").textContent );
    const themeSelect = document.getElementById("theme");
    const fontSelect = document.getElementById("font-family");
    const fontSizeSelect = document.getElementById("font-size");
    const languageSelect = document.getElementById("language");
    const currentSelectedLanguage = userSettings.user_language;
    const currentSelectedFontFamily = userSettings.user_font_family;
    const currentSelectedTheme = userSettings.user_theme_mode;
    const currentSelectedFontSize = userSettings.user_font_size;
    
    function displaySettingSelection(
    settingsSource , //eg: supported languages
    settingsSelector , //eg: languageSelect 
    preferedSettings //eg: currentSelectedLanguage
    ){
       for( const[ settingsName , settingsValue ] of Object.entries(settingsSource) ){
        let settingsOption = document.createElement("option");
        settingsOption.textContent = settingsName;
        settingsOption.value = settingsValue;
        settingsSelector.appendChild(settingsOption);
        if( settingsValue == preferedSettings ){
            settingsOption.selected = true;
        }
        if( settingsSelector.id  === "font-family" ){
            settingsOption.style.fontFamily = settingsValue;
        }

       }
    }

    //Languages
    displaySettingSelection(
        supportedLanguages , 
        languageSelect ,
        currentSelectedLanguage 
    );

    //Font families
    displaySettingSelection(
        supportedFonts , 
        fontSelect , 
        currentSelectedFontFamily 
    );

    //Font size
    displaySettingSelection(
        supportedFontSizes ,
        fontSizeSelect , 
        currentSelectedFontSize
    );

    //Theme Mode
    displaySettingSelection(
        supportedThemes , 
        themeSelect , 
        currentSelectedTheme
    )


    //Submit Settings Form
    const settingsForm = document.getElementById("settings-form");
    settingsForm.addEventListener("submit", async (e)=>{
        e.preventDefault();
        const csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value;
        const settingsUrl = `${window.origin}/settings/`;
        const settingsdData = {
            "prefered_theme": themeSelect.value , //themeSelect is a select tag
            "prefered_font_family": fontSelect.value , //fontSelect is a select tag
            "prefered_font_size": fontSizeSelect.value, //fontSizeSelect is a select tag
            "prefered_language": languageSelect.value, //languageSelect is a select tag
        }
        const settingsPreferences = JSON.stringify(settingsdData);
        console.log( settingsPreferences );
        const response = await fetch( settingsUrl , {
            method: "POST" ,
            headers: { "Content-Type":"application/json" , 
                       "X-CSRFToken": csrfToken ,
                    },
            body: settingsPreferences ,
        } );
        
        if(response.status){
            window.location.reload();
            console.log("Data successfully received");
        } else{
            console.error(response);
        }
    });


});




