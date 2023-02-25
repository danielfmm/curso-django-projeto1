$(document).ready(function () {
    $('#menu').click(function () {
        $(this).toggleClass('fa-times')
        $('header').toggleClass('toggle')
        $('').toggle
    })



    $(window).on('scroll load', function () {
        $('#menu').removeClass('fa-times')
        $('header').removeClass('toggle')

        if ($(window).scrollTop() > 3000) {
            $('.top').show()
        } else {
            $('.top').hide()
        }

    })
    $('.user img').on('click', function () {
        $('.user img').attr('src', '/imgs/profile.png')
    })
    $('a[href*="#"]').on('click', function (e) {
        e.preventDefault()
        $('html, body').animate({
            scrollTop: $($(this).attr('href')).offset().top,
        },
            500,
            'linear'
        )
    })



})