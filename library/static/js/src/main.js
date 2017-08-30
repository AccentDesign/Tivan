$(document).ready(function() {

    // Hide Messages
    window.setTimeout( hideMessages, 5000);

    function hideMessages(){
        $('.messages').slideUp();
    }

    // Touch Device Detector
    if ("ontouchstart" in window || navigator.maxTouchPoints) {
        $('body').addClass('touch');
    } else {
        $('body').addClass('no-touch');
    }

    // Homepage Form Switcher
    $('.toggle--form').click(function(){
        if(!$(this).hasClass('active')) {
            $('.toggle--form').removeClass('active');
            $(this).addClass('active');

            var wrapper = $(this).data('target');
            var id = '#';
            var wrapper_id = id.concat(wrapper);
            var str = '_text';
            var text_id = wrapper_id.concat(str);

            if (wrapper == 'register') {
                $('.home--login .gradient').removeClass('gradient--secondary');
                $('.home--login .gradient').addClass('gradient--primary');
            } else if (wrapper == 'login') {
                $('.home--login .gradient').removeClass('gradient--primary');
                $('.home--login .gradient').addClass('gradient--secondary');
            }

            $('.form-wrapper').removeClass('active');
            $(wrapper_id).addClass('active');

            $('.text-wrapper').removeClass('active');
            $(text_id).addClass('active');
        }
    });

    // Scroll to Register
    $('#register_link').click(function(){
        $('html, body').animate({
            'scrollTop': $('.home--login').offset().top
        }, 500);
    });

    // Masonry Initialiser
    function masonryInit() {
        var msnry = new Masonry( '.cards', {
            // options
            itemSelector: '.card__wrapper',
            columnWidth: '.card__wrapper',
            gutter: 20
        });

        msnry.reloadItems();
    }

    masonryInit();

});