$(document).ready(function() {

    // Touch Device Detector
    if ("ontouchstart" in window || navigator.maxTouchPoints) {
        $('body').addClass('touch');
    } else {
        $('body').addClass('no-touch');
    }
});