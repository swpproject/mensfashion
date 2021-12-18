(function ($) {
  "use strict";

  /*[ Load page ]
    ===========================================================*/
  $(".animsition").animsition({
    inClass: "fade-in",
    outClass: "fade-out",
    inDuration: 1500,
    outDuration: 800,
    linkElement: ".animsition-link",
    loading: true,
    loadingParentElement: "html",
    loadingClass: "animsition-loading-1",
    loadingInner: '<div class="loader05"></div>',
    timeout: false,
    timeoutCountdown: 5000,
    onLoadEvent: true,
    browser: ["animation-duration", "-webkit-animation-duration"],
    overlay: false,
    overlayClass: "animsition-overlay-slide",
    overlayParentElement: "html",
    transition: function (url) {
      window.location.href = url;
    },
  });

  /*[ Back to top ]
    ===========================================================*/
  var windowH = $(window).height() / 2;

  $(window).on("scroll", function () {
    if ($(this).scrollTop() > windowH) {
      $("#myBtn").css("display", "flex");
    } else {
      $("#myBtn").css("display", "none");
    }
  });

  $("#myBtn").on("click", function () {
    $("html, body").animate({ scrollTop: 0 }, 300);
  });

  /*==================================================================
    [ Fixed Header ]*/
  var headerDesktop = $(".container-menu-desktop");
  var wrapMenu = $(".wrap-menu-desktop");

  if ($(".top-bar").length > 0) {
    var posWrapHeader = $(".top-bar").height();
  } else {
    var posWrapHeader = 0;
  }

  if ($(window).scrollTop() > posWrapHeader) {
    $(headerDesktop).addClass("fix-menu-desktop");
    $(wrapMenu).css("top", 0);
  } else {
    $(headerDesktop).removeClass("fix-menu-desktop");
    $(wrapMenu).css("top", posWrapHeader - $(this).scrollTop());
  }

  $(window).on("scroll", function () {
    if ($(this).scrollTop() > posWrapHeader) {
      $(headerDesktop).addClass("fix-menu-desktop");
      $(wrapMenu).css("top", 0);
    } else {
      $(headerDesktop).removeClass("fix-menu-desktop");
      $(wrapMenu).css("top", posWrapHeader - $(this).scrollTop());
    }
  });

  /*==================================================================
    [ Menu mobile ]*/
  $(".btn-show-menu-mobile").on("click", function () {
    $(this).toggleClass("is-active");
    $(".menu-mobile").slideToggle();
  });

  var arrowMainMenu = $(".arrow-main-menu-m");

  for (var i = 0; i < arrowMainMenu.length; i++) {
    $(arrowMainMenu[i]).on("click", function () {
      $(this).parent().find(".sub-menu-m").slideToggle();
      $(this).toggleClass("turn-arrow-main-menu-m");
    });
  }

  $(window).resize(function () {
    if ($(window).width() >= 992) {
      if ($(".menu-mobile").css("display") == "block") {
        $(".menu-mobile").css("display", "none");
        $(".btn-show-menu-mobile").toggleClass("is-active");
      }

      $(".sub-menu-m").each(function () {
        if ($(this).css("display") == "block") {
          console.log("hello");
          $(this).css("display", "none");
          $(arrowMainMenu).removeClass("turn-arrow-main-menu-m");
        }
      });
    }
  });

  /*==================================================================
    [ Show / hide modal search ]*/
  $(".js-show-modal-search").on("click", function () {
    $(".modal-search-header").addClass("show-modal-search");
    $(this).css("opacity", "0");
  });

  $(".js-hide-modal-search").on("click", function () {
    $(".modal-search-header").removeClass("show-modal-search");
    $(".js-show-modal-search").css("opacity", "1");
  });

  $(".container-search-header").on("click", function (e) {
    e.stopPropagation();
  });

  /*==================================================================
    [ Isotope ]*/
  var $topeContainer = $(".isotope-grid");
  var $filter = $(".filter-tope-group");

  // filter items on button click
  $filter.each(function () {
    $filter.on("click", "button", function () {
      var filterValue = $(this).attr("data-filter");
      $topeContainer.isotope({ filter: filterValue });
    });
  });

  // init Isotope
  $(window).on("load", function () {
    var $grid = $topeContainer.each(function () {
      $(this).isotope({
        itemSelector: ".isotope-item",
        layoutMode: "fitRows",
        percentPosition: true,
        animationEngine: "best-available",
        masonry: {
          columnWidth: ".isotope-item",
        },
      });
    });
  });

  var isotopeButton = $(".filter-tope-group button");

  $(isotopeButton).each(function () {
    $(this).on("click", function () {
      for (var i = 0; i < isotopeButton.length; i++) {
        $(isotopeButton[i]).removeClass("how-active1");
      }

      $(this).addClass("how-active1");
    });
  });

  /*==================================================================
    [ Filter / Search product ]*/
  $(".js-show-filter").on("click", function () {
    $(this).toggleClass("show-filter");
    $(".panel-filter").slideToggle(400);

    if ($(".js-show-search").hasClass("show-search")) {
      $(".js-show-search").removeClass("show-search");
      $(".panel-search").slideUp(400);
    }
  });

  $(".js-show-search").on("click", function () {
    $(this).toggleClass("show-search");
    $(".panel-search").slideToggle(400);

    if ($(".js-show-filter").hasClass("show-filter")) {
      $(".js-show-filter").removeClass("show-filter");
      $(".panel-filter").slideUp(400);
    }
  });

  /*==================================================================
    [ Cart ]*/
  $(".js-show-cart").on("click", function () {
    $(".js-panel-cart").addClass("show-header-cart");
  });

  $(".js-hide-cart").on("click", function () {
    $(".js-panel-cart").removeClass("show-header-cart");
  });

  /*==================================================================
    [ Cart ]*/
  $(".js-show-sidebar").on("click", function () {
    $(".js-sidebar").addClass("show-sidebar");
  });

  $(".js-hide-sidebar").on("click", function () {
    $(".js-sidebar").removeClass("show-sidebar");
  });

  /*==================================================================
    [ +/- num product ]*/
  $(".btn-num-product-down").on("click", function () {
    var numProduct = Number($(this).next().val());
    if (numProduct > 1) {
      $(this)
        .next()
        .val(numProduct - 1);
      let itemnumber = $(this).attr("data-minusquantity");
      let productprice = $(this).attr("data-price");
      itemtotal(itemnumber, numProduct - 1, productprice);
      let total = $(".cart-total").text();
      let price = parseInt(total) - parseInt(productprice);
      carttotal(price);
    }
  });

  $(".btn-num-product-up").on("click", function () {
    var numProduct = Number($(this).prev().val());
    $(this)
      .prev()
      .val(numProduct + 1);
    let itemnumber = $(this).attr("data-addquantity");
    let productprice = $(this).attr("data-price");
    itemtotal(itemnumber, numProduct + 1, productprice);
    let total = $(".cart-total").text();
    console.log(total);
    let price = parseInt(total) + parseInt(productprice);
    carttotal(price);
  });

  let itemtotal = (count, quantity, price) => {
    $(".item-total-" + count).html(quantity * price);
  };

  let carttotal = (price) => {
    $(".cart-total").text(price);
  };

  /*==================================================================
    [ Rating ]*/
  $(".wrap-rating").each(function () {
    var item = $(this).find(".item-rating");
    var rated = -1;
    var input = $(this).find("input");
    $(input).val(0);

    $(item).on("mouseenter", function () {
      var index = item.index(this);
      var i = 0;
      for (i = 0; i <= index; i++) {
        $(item[i]).removeClass("zmdi-star-outline");
        $(item[i]).addClass("zmdi-star");
      }

      for (var j = i; j < item.length; j++) {
        $(item[j]).addClass("zmdi-star-outline");
        $(item[j]).removeClass("zmdi-star");
      }
    });

    $(item).on("click", function () {
      var index = item.index(this);
      rated = index;
      $(input).val(index + 1);
    });

    $(this).on("mouseleave", function () {
      var i = 0;
      for (i = 0; i <= rated; i++) {
        $(item[i]).removeClass("zmdi-star-outline");
        $(item[i]).addClass("zmdi-star");
      }

      for (var j = i; j < item.length; j++) {
        $(item[j]).addClass("zmdi-star-outline");
        $(item[j]).removeClass("zmdi-star");
      }
    });
  });

  /*==================================================================
    [ Show modal1 ]*/
  $(".js-show-modal1").on("click", function (e) {
    e.preventDefault();
    let img1 = $(this).attr("data-img1");
    let img2 = $(this).attr("data-img2");
    let img3 = $(this).attr("data-img3");
    let product_name = $(this).attr("data-name");
    let product_price = $(this).attr("data-price");
    let product_specifications = $(this).attr("data-specifications");
    let product_description = $(this).attr("data-description");
    $(".js-modal1 .img1").attr({ src: img1, href: img1 });
    $(".js-modal1 .img2").attr({ src: img2, href: img2 });
    $(".js-modal1 .img3").attr({ src: img3, href: img3 });
    $(".js-modal1 .product-name").html(product_name);
    $(".js-modal1 .product-price").html(product_price);
    $(".js-modal1 .product-specifications").html(product_specifications);
    $(".js-modal1 .product_description").html(product_description);
    $(".js-modal1").addClass("show-modal1");
  });

  $(".js-hide-modal1").on("click", function () {
    $(".js-modal1").removeClass("show-modal1");
  });

  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  const csrftoken = getCookie("csrftoken");

  // add to cart
  $(".cart-icon").on("click", function (e) {
    e.preventDefault();
    let productid = $(this).attr("data-product_id");
    $.ajax({
      data: { productid: productid },
      headers: { "X-CSRFToken": csrftoken },
      type: "POST",
      url: "/shop/addtocart/",
      success: function (response) {
        console.log(response);
        if(response.status=="success")
        { 
            let current_item_cart = $(".header-cart-icon").attr("data-notify");
            current_item_cart = parseInt(current_item_cart) + 1;
            swal(response.name, response.msg1, response.status).then(() => {
              $(".header-cart-icon")
                .attr("data-notify", current_item_cart)
                .addClass("icon-header-noti");
            });
        }
        else
        {
          swal(response.name, response.msg1, response.status);
        }
        
      },
    });
  });

  // login before adding into cart
  $(".cart-icon-nologin").on("click", function (e) {
    e.preventDefault();
    swal("Please login before adding product into cart");
  });

  // delete from cart
  $(".deletefromcart").on("click", function (e) {
    e.preventDefault();
    let cartid = $(this).attr("data-cartid");
    swal({
      title: "Are you sure?",
      text: "You want to remove this product from cart",
      icon: "error",
      buttons: {
        cancel: true,
        confirm: true,
      },
    }).then((result) => {
      if (result) {
        $.ajax({
          data: { cartid: cartid },
          headers: { "X-CSRFToken": csrftoken },
          type: "POST",
          url: "/shop/deletefromcart/",
          success: function (response) {
            swal(response.msg1, response.status).then(() => {
              location.reload();
            });
          },
        });
      }
    });
  });

  //upadate cart
  let updatecart = () => {
    let dict = {};
    $(".cart-product").each(function (index, element) {
      let quantity = $(element).val();
      let cartid = $(element).attr("data-cartid");
      dict[cartid] = quantity;
    });
    $.ajax({
      data: dict,
      headers: { "X-CSRFToken": csrftoken },
      type: "POST",
      url: "/shop/updatecart/",
      success: function (response) {
          swal(response.msg1, response.status).then(() => {
            location.reload();
          });
      },
    });
  };

  // update from cart
  $(".update-cart").on("click", function (e) {
    e.preventDefault();
    updatecart();
  });

  // proceed to checkout
  $(".proceed-to-checkout").on("click", function (e) {
    e.preventDefault();
    updatecart();
    window.location = "/shop/checkout/";
  });
})(jQuery);
