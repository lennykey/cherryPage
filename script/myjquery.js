 $(document).ready(function(){
    var legendContent = $('.key').text();
    /*$('#topBar').text(legendContent).hide();*/
    
    /*$('.key').next().children().toggle();*/
    /*$('.key').next().children().css("visibility", 'hidden');*/
    $('#sidebar ul li a').parent().parent().hide();
    

    $('.key').click(function(){
        var linkList = $('#linkList');
        /*$(this).next().children().toggle();*/
        /*$(this).children().filter(':hidden').show();*/
        $('#sidebar ul li a').parent().parent().show();
        /*var links = $(this).next().children().clone();*/
        var links = $(this).next().find('li div a').clone();
        $('#sidebar ul li a').parent().parent().hide();
                    
        $('#linkList').empty();
        $('#linkList').append().html(links);
        $('#linkList').children().each(function(){
            $(this).append('<br />');
        });
        // linkList.hide().show();
        linkList.hide().fadeIn(700);
        // linkList.animate({opacity:.5},{duration:'slow', easing: 'swing'});

    });



 });