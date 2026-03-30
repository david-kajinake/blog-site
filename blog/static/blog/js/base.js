document.addEventListener("DOMContentLoaded",(e)=>{
    const routeUrl = (url)=>{
     document.location.href = url;
    };

    const sideLinks = document.querySelectorAll(".sidebar-link");

    //route sidebar links
    for( const link of sideLinks ){
        link.addEventListener("click",(e)=>{
        let linkTag = link.dataset.tag;
        if( linkTag === "dashboard" ){
            linkTag = "";
        }
        const linkUrl = `${window.origin}/${linkTag}/`;
        routeUrl(linkUrl);
        });

    }
});