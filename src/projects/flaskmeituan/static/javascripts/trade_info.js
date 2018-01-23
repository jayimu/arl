$(document).ready(function () {
    $.ajax({
        url:'/account',
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
    //订单详情页
    var url=window.location.href;
    var tid=$.trim(url.replace(/.*\/totinfo\//," ")); //订单ID

    $.ajax({
        url:'/tradeinfo',
        data:{tid:tid},//订单id
        dataType: "json",
        type:'post',
        success: function (result) {
            new Vue({
                    el:"#content",
                    data:{
                        infos:result
                    }
            })
        },
        error:function (err) {
            console.log("123");
        }
    })


});




