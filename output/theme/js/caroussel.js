$(document).ready(function(){

    // Caroussel

    $(".caroussel .next").click(function(){
        caroussel = $(this).parent()
        activeLi = caroussel.find(".active");
        if (activeLi.next().length == 0){
            activeLi.removeClass("active");
            caroussel.find("li:first-child").addClass("active");
        } else {
            activeLi.removeClass("active");
            activeLi.next().addClass("active");    
        }
    });

    $(".caroussel .prev").click(function(){
        caroussel = $(this).parent()
        activeLi = caroussel.find(".active");
        if (activeLi.prev().length == 0){
            activeLi.removeClass("active");
            caroussel.find("li:last-child").addClass("active");
        } else {
            activeLi.removeClass("active");
            activeLi.prev().addClass("active");    
        }
    });

});