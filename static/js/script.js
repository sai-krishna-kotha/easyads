function scrollingHandler() {
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', function () {
        let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        if (scrollTop > 80 && scrollTop < 100) {
            navbar.style.transform = 'translateY(-100%)';
        }
        else {
            navbar.style.transform = 'translateY(0)';
        }        
    });
};

document.addEventListener('DOMContentLoaded', scrollingHandler);
