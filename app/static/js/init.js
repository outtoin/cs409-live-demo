$(document).ready(function() {
    $('textarea#textarea2').characterCounter();
    $('#nav-comment').click(function() {
        $('.analyze-comment').removeClass('hide');
        $('.spam-words').addClass('hide');
    });
    $('#nav-spam').click(function() {
        $('.analyze-comment').addClass('hide');
        $('.spam-words').removeClass('hide');
    });
    
    $('#comment-form').submit(function(e) {
        console.log(1);
        e.preventDefault();
        var url = "http://localhost:8000/api/predict";
        
       $.ajax({
           type: "POST",
           url: url,
           data: {'text':$('#textarea2').val()},
           success: function(res) {
               console.log(res);
           }   
       })
    });
    
    $('#spam-form').submit(function(e) {
        console.log(1);
        e.preventDefault();
        var url = "http://localhost:8000/api/top";
        
       $.ajax({
           type: "GET",
           url: url,
           data: {'num': $('#icon_prefix2').val()},
           success: function(res) {
               console.log(res);
           }   
       })
    });
});   
