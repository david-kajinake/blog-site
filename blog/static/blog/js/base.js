document.addEventListener("DOMContentLoaded",(e)=>{
    const pageName = document.querySelector("body").dataset.pageid;
    const routeUrl = (url)=>{
     document.location.href = url;
    };

    const sideLinks = document.querySelectorAll(".sidebar-link");

    // work on sidebar links
    for( const link of sideLinks ){
        //Route url
        let linkTag = link.dataset.tag;
        link.addEventListener("click",(e)=>{
        if( linkTag === "home" ){
            linkTag = "";
        }
        const linkUrl = `${window.origin}/${linkTag}/`;
        routeUrl(linkUrl);
        });

        //Highlight the current page's side link
        if( pageName.replace(/_/g,"-") == linkTag.replace(/_/g,"-")  ){
            link.classList.add("active");
        } else{
            link.classList.remove("active");
        }
    }

});