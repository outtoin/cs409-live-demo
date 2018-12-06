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
        var url = "";
        
//        $.ajax({
//            type: "POST",
//            url: url,
//            data: 
//        })
    });
    
    $('#spam-form').submit(function(e) {
        console.log(1);
        e.preventDefault();
    });
});   
