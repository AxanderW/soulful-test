$(document).ready(function(){
    $(".navbar-toggler-icon").click(function () {
        $(".click-menu-btn").toggleClass("change-btn");
        $(".navbar-collapse").fadeToggle();
    });

    $(".product-filter-content h6").click(function () {
        $(this).toggleClass("rotate-icon");
        $(this).parent().find(".product-filter-toggle").slideToggle();
    });

    $(".color-wrap ul li").click(function () {
        $(".color-wrap ul li").removeClass("clr-select");
        $(this).toggleClass("clr-select");
    });

    $(".select-clr li").click(function () {
        $(".select-clr li").removeClass("selected-clr");
        $(this).toggleClass("selected-clr");
    });

    $(".favr-product").click(function () {
        $(this).toggleClass("my-favr");
    });

    $("#price-range").slider(
        {range: true, 
            min: 0,
            max: 500,
            values: [0, 500], 
            slide: function(event, ui) {
                $("#priceRange1").val(ui.values[0] + " USD");
                $("#priceRange2").val(ui.values[1] + " USD");
            }
    });
    $("#priceRange1").val($("#price-range").slider("values", 0) + " USD");
    $("#priceRange2").val($("#price-range").slider("values", 1) + " USD");

    $('.cart-quantity').on('click', '.button-plus', function(e) {
        e.preventDefault();
        var fieldName = $(e.target).data('field');
        var parent = $(e.target).closest('div');
        var currentVal = parseInt(parent.find('input[name=' + fieldName + ']').val(), 10);

        if (!isNaN(currentVal)) {
            parent.find('input[name=' + fieldName + ']').val(currentVal + 1);
        } else {
            parent.find('input[name=' + fieldName + ']').val(0);
        }
    });
      
    $('.cart-quantity').on('click', '.button-minus', function(e) {
        e.preventDefault();
        var fieldName = $(e.target).data('field');
        var parent = $(e.target).closest('div');
        var currentVal = parseInt(parent.find('input[name=' + fieldName + ']').val(), 10);
      
        if (!isNaN(currentVal) && currentVal > 1) {
          parent.find('input[name=' + fieldName + ']').val(currentVal - 1);
        } else {
          parent.find('input[name=' + fieldName + ']').val(0);
        }
    });

    $('.delete-btn').on('click', function(){
        $(this).parent().parent().remove();
    })

    $('.thumbnail').on('click', function() {
        var clicked = $(this);
        var newSelection = clicked.data('big');
        var $img = $('.primary').css("background-image","url(" + newSelection + ")");
        clicked.parent().find('.thumbnail').removeClass('selected');
        clicked.addClass('selected');
        $('.primary').empty().append($img.hide().fadeIn('slow'));
    });

    $('.best-product-slider').slick({
        dots: false,
        arrows: true,
        infinite: false,
        speed: 800,
        slidesToShow: 4,
        slidesToScroll: 1,
        prevArrow:"<button type='button' class='slick-prev'><i class='far fa-arrow-left'></i></button>",
        nextArrow:"<button type='button' class='slick-next'><i class='far fa-arrow-right'></i></button>",
        responsive: [
            {
            breakpoint: 992,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1,
                }
            },
            {
                breakpoint: 767,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
            // You can unslick at a given breakpoint now by adding:
            // settings: "unslick"
            // instead of a settings object
        ]
    });

    $('.feat-items-img-slider').slick({
        dots: false,
        arrows: true,
        infinite: false,
        speed: 800,
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 3000,
        prevArrow:"<button type='button' class='slick-prev'><i class='far fa-arrow-left'></i></button>",
        nextArrow:"<button type='button' class='slick-next'><i class='far fa-arrow-right'></i></button>",
    });

    $('.our-team-slider').slick({
        dots: false,
        arrows: true,
        infinite: false,
        speed: 800,
        slidesToShow: 4,
        slidesToScroll: 1,
        // autoplay: true,
        // autoplaySpeed: 5000,
        prevArrow:"<button type='button' class='slick-prev'><i class='far fa-arrow-left'></i></button>",
        nextArrow:"<button type='button' class='slick-next'><i class='far fa-arrow-right'></i></button>",
        responsive: [
            {
            breakpoint: 1200,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1,
                }
            },
            {
                breakpoint: 992,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 576,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
            // You can unslick at a given breakpoint now by adding:
            // settings: "unslick"
            // instead of a settings object
        ]
    });

    $('.blog-content-slider').slick({
        dots: false,
        arrows: true,
        infinite: false,
        speed: 800,
        slidesToShow: 3,
        slidesToScroll: 1,
        // autoplay: true,
        // autoplaySpeed: 5000,
        prevArrow:"<button type='button' class='slick-prev'><i class='far fa-arrow-left'></i></button>",
        nextArrow:"<button type='button' class='slick-next'><i class='far fa-arrow-right'></i></button>",
        responsive: [
            {
                breakpoint: 992,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
            // You can unslick at a given breakpoint now by adding:
            // settings: "unslick"
            // instead of a settings object
        ]
    });

    $('.pgwSlider').pgwSlider({
        autoSlide : false,
        transitionDuration : 500,
    });
});