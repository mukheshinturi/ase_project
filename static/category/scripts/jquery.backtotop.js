<<<<<<< HEAD
=======
/*
Template Name: Maxisonix
Author: <a href="http://www.os-templates.com/">OS Templates</a>
Author URI: http://www.os-templates.com/
Licence: Free to use under our free template licence terms
Licence URI: http://www.os-templates.com/template-terms
File: Back to Top JS
*/
>>>>>>> e2e81602d85c6bebcced2f293e90e4ff77cb60f6

jQuery("#backtotop").click(function () {
    jQuery("body,html").animate({
        scrollTop: 0
    }, 600);
});
jQuery(window).scroll(function () {
    if (jQuery(window).scrollTop() > 150) {
        jQuery("#backtotop").addClass("visible");
    } else {
        jQuery("#backtotop").removeClass("visible");
    }
<<<<<<< HEAD
});
=======
});
>>>>>>> e2e81602d85c6bebcced2f293e90e4ff77cb60f6
