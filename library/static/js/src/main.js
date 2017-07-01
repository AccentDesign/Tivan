$(document).ready(function() {

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

            var $wrapper = $(this).data('target');
            var id = '#';
            var $wrapper_id = id.concat($wrapper);

            $('.form-wrapper').removeClass('active');
            $($wrapper_id).addClass('active');
        }
    });
});