document.addEventListener("DOMContentLoaded",(e) =>{
    const blogs = document.querySelectorAll(".blog-card");
    blogs.forEach( (blog)=>{
        blog.addEventListener("click",(e)=>{
           const blogId = blog.id;
           console.log(blogId);
           const blogRedirectUrl = `${window.origin}/post/${blogId}/`;
           window.location.href = blogRedirectUrl;
        });
    })
});