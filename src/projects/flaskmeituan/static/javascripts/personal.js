$(document).ready(function () {

    $.ajax({
        url:'/account',
        dataType: "json",
        type:'post',
        success: function (result) {

            new Vue({
                el:"#user",
                data:{
                    username:result[0]['nickname'],
                   
                }
            })
            new Vue({
                el:"#huser",
                data:{
                    username:result[0]['nickname'],
                   
                }
            })
        },
        error:function (err) {
            console.log(err);
        }
    })
    $(".J-nav__trigger").mouseenter(function () {
        $(".J-nav__list").show();
        $(".F-glob-caret-up").show();
        $(".F-glob-caret-down").hide();
    });
    $(".J-nav__trigger").mouseleave(function () {
        $(".J-nav__list").hide();
        $(".F-glob-caret-up").hide();
        $(".F-glob-caret-down").show();
    });
    $(".J-nav__list").mouseenter(function () {
        $(".J-nav__list").show();
        $(".F-glob-caret-up").show();
        $(".F-glob-caret-down").hide();
    });
    $(".J-nav__list").mouseleave(function () {
        $(".J-nav__list").hide();
        $(".F-glob-caret-up").hide();
        $(".F-glob-caret-down").show();
    });
    $("#yui_3_16_0_1_1505697438810_548").mouseenter(function () {
        $(".J-nav-level2").show();
    });
    $("#yui_3_16_0_1_1505697438810_548").mouseleave(function () {
        $(".J-nav-level2").hide();
    });
});


