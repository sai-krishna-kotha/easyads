function scrollingHandler() {
    const navbar = document.querySelector('.navbar');

    window.addEventListener('scroll', function () {
        let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        // Hide navbar on scroll down, show on scroll up
        if (scrollTop > 80 && scrollTop < 100) {
            // Scrolling up
            navbar.style.transform = 'translateY(-100%)';
        }
        else {
            // Scrolling down
            navbar.style.transform = 'translateY(0)';
            //}   
        }        
    });
};
// console.log("Heyy");

document.addEventListener('DOMContentLoaded', scrollingHandler);
