document.addEventListener("DOMContentLoaded",()=>{
    console.log("Woking");
    const headerNavItems = document.querySelectorAll(".header-nav-item");

    for( const navItem of headerNavItems ){
        navItem.addEventListener("click",()=>{
            const itemTag = navItem.dataset.tag;
            const itemUrl = `${window.origin}/${itemTag}/`;
            document.location.href = itemUrl;
        });
    }
});