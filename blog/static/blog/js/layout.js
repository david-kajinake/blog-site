document.addEventListener("DOMContentLoaded",()=>{
    const headerNavItems = document.querySelectorAll(".header-nav-item");
    //Route the header nav links 
    for( const navItem of headerNavItems ){
        navItem.addEventListener("click",()=>{
            let itemTag = navItem.dataset.tag;
            if(itemTag == "home"){
                itemTag = "";
            }
            const itemUrl = `${window.origin}/${itemTag}/`;
            document.location.href = itemUrl;
        });
    }
});

                                                                                                                                                                                                                                                                                                                                                                                                                         