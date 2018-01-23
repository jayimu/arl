$(document).ready(function () {

    //判断是否登录
    var user=new Vue({
        el: '#user',
        data: {
            username:"未登录"
        }
    })
    $.ajax({
        url:'/islogin',
        dataType: "text",
        type:'get',
        success: function (result) {
            user.username=result;
        },

        error:function (err) {
            console.log(err);
        }
    });

	//获取全部分类
	$.ajax({
	    url:'/field',
	    dataType: "json",
	    type:'get',
	    success: function (result) {
	        //alert(result);
	        new Vue({
	            el: '#field',
	            data: {
	                css:result
	            }
	        })
	    },
	    error:function (err) {
	        console.log("123");
	    }
	});

    $(document).on("mouseenter",".nav-li",function(){
        var index=$(this).index();
        var id=$(this).attr("data-id");

        $.ajax({
            url:'/sub_field',
            data:{fid:id},
            dataType: "json",
            type:'post',
            success: function (result) {
                //alert(result);
                new Vue({
                    el: '#meishi',
                    data: {
                        mss:result
                    }
                })
            },
            error:function (err) {
                console.log("123");
            }
        });
        $(".category-nav-detail-wrapper").addClass("active");
        $(".category-nav-detail").eq(index).addClass("active").siblings().removeClass("active");
    });
    $(document).on("mouseleave",".category-nav-detail",function(){
        var index=$(this).index();
        $(".category-nav-detail-wrapper").removeClass("active");
        $(".category-nav-detail").eq(index).removeClass("active").siblings().removeClass("active");
    });
});


