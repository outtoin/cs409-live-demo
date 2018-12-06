$(document).ready(function() {
    $.ajaxSetup({cache: false});

    $('textarea#textarea2').characterCounter();
    $('#nav-comment').click(function() {
        $('.analyze-comment').removeClass('hide');
        $('.spam-words').addClass('hide');
        $('.image-getter2').addClass('hide');
    });
    $('#nav-spam').click(function() {
        $('.analyze-comment').addClass('hide');
        $('.spam-words').removeClass('hide');
        $('.image-getter1').addClass('hide');
    });
    
    $('#comment-form').submit(function(e) {
        console.log(1);
        e.preventDefault();
        var url = "http://13.125.143.82:8000/api/predict";
        
       $.ajax({
           type: "POST",
           url: url,
           data: {'text':$('#textarea2').val()},
           success: function(res) {
            console.log(res);
            $('#image1').attr("src", "static/img/fig1.png");
            $('.image-getter1').removeClass('hide');
           }   
       })
    });
    
    $('#spam-form').submit(function(e) {
        console.log(1);
        e.preventDefault();
        var url = "http://13.125.143.82:8000/api/top";
        
       $.ajax({
           type: "GET",
           url: url,
           data: {'num': $('#icon_prefix2').val()},
           success: function(res) {
               console.log(res);
               $('#image2').attr("src", "static/img/fig2.png");
               $('.image-getter2').removeClass('hide');
           }   
       });
    });
});   
