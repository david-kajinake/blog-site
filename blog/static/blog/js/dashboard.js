document.addEventListener("DOMContentLoaded",(e)=>{
    

const openBtn = document.getElementById('openModalBtn');
    const closeBtn = document.getElementById('closeModalBtn');
    const cancelBtn = document.getElementById('cancelModalBtn');
    const modal = document.getElementById('createBlogModal');

    // Prevent default anchor behavior and show modal
    openBtn.addEventListener('click', (e) => {
        e.preventDefault();
        modal.classList.add('show');
    });

    // Close modal functions
    const closeModal = () => {
        modal.classList.remove('show');
    };

    closeBtn.addEventListener('click', closeModal);
    cancelBtn.addEventListener('click', closeModal);

    // Close if user clicks completely outside the modal content
    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });

    //Submit Blog form
    const blogForm = document.getElementById("new-blog-form");
    blogForm.addEventListener("submit", async (e)=>{
        e.preventDefault();
        const blogSubmissionUrl = `${window.origin}/blog/create/new/`;
        const csrfToken = blogForm.querySelector("input[name =csrfmiddlewaretoken]")
        const blogTitle = document.getElementById("blog-title");
        const blogImage = document.getElementById("blog-image");
        const blogContent = document.getElementById("blog-content");
       // const blogInfo = {
            //Names must match the backend's fields
        //    "title": blogTitle.value , 
        //    "content": blogContent.value , 
        //    "image": blogImage.value ,
       // } 

        //const blogData = JSON.stringify( blogInfo );
        const formData = new FormData( blogForm )
        console.log( formData );
        const response = await fetch( blogSubmissionUrl ,{ 
            method:"POST" , 
            headers:{ "X-CSRFToken": csrfToken.value } , 
            body: formData
         } );
         if (response.status){
            console.log(response);
         } else{
            console.error( response );
         }


    });



});