$(document).ready(function(){

    $("#filters button").click(function(){
        $("#filters button").removeClass("active");
        $(this).addClass("active");
        const value = $(this).text();
        $(".block").each(function(){
            if (value === "TOUT" || $(this).attr("data-tag") === value) {
                $(this).fadeIn();
            } else {
                $(this).fadeOut();
            }
        });
        $("html, body").scrollTop(0);
    });

});