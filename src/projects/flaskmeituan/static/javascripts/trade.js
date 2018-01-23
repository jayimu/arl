$(document).ready(function () {
    $.ajax({
        url:'/personal',
        dataType: "json",
        type:'post',
        success: function (result) {
            
            new Vue({
                el:"#huser",
                data:{
                    username:result[0]['nickname'],
                    tel:result[0]['tel_number'],
                    pic:result[0]['pic_url']
                }
            })
        },
        error:function (err) {
            console.log("123");
        }
    })
    //获取订单信息
    var trade=new Vue({
        el:"#yui_3_16_0_1_1505369383117_860",
        data:{
            trades:[]
        },
        methods:{
            select:function($e){
                var val=$("#select").val();

                if (val=="0"){
                    $.ajax({
                        url:'/trade',
                        dataType:'json',
                        type:'post',
                        success:function (result) {
                            trade.trades=result;
                        }
                    })
                }else if(val=="1"){
                      $.ajax({//已付款
                        url:'/trade/paid',
                        dataType:'json',
                        type:'post',
                        success:function (result) {
                            trade.trades=result;
                        }
                    })
                }else if(val=="2"){//未付款
                     $.ajax({
                        url:'/trade/non-payment',
                        dataType:'json',
                        type:'post',
                        success:function (result) {
                            trade.trades=result;
                        }
                    })
                }
            }
        }
    })

    $.ajax({
        url:'/trade',
        dataType: "json",
        type:'post',
        success: function (result) {
            //alert(result[0]['nickname']);
            trade.trades=result;
        },
        error:function (err) {
            console.log("123");
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


