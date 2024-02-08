$(document).ready(function(){

    $("#filtres button").click(function(){
        $("#filtres button").removeClass("active");
        $(this).addClass("active");
        const value = $(this).text();
        $(".contenu").each(function(){
            if (value === "TOUT" || $(this).attr("data-tag") === value) {
                $(this).fadeIn();
            } else {
                $(this).fadeOut();
            }
        });
        $("html, body").scrollTop(0);
    });

});