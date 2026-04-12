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


});