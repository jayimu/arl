function getUrlParam(name)
{
    var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
    var r = window.location.search.substr(1).match(reg);  //匹配目标参数
    if (r!=null) return unescape(r[2]); return null; //返回参数值
}
$(document).ready(function () {
    $.ajax({
        url:'/account',
        dataType: "json",
        type:'post',
        success: function (result) {
            //alert(result[0]['nickname']);
            new Vue({
                el:"#huser",
                data:{
                    username:result[0]['nickname'],
                    
                }
            })
        },
        error:function (err) {
            console.log("123");
        }
    })
    $.ajax({
        url:"/account",
        dataType:"json",
        type:'post',
        success:function (result) {

            new Vue({
                el:'#content',
                data:{
                    users:result
                },
                methods:{
                    nick:function(e)
                    {
                        var nickname = prompt('输入您的姓名');
                        $.ajax({
                            url:'/account/nickname',
                            dataType:'json',
                            type:'post',
                            data:{username:nickname},
                            success:function(result)
                            {
                                window.location.href = "/toaccount"
                            }
                        })
                    },
                    pwd:function(e)
                    {
                        var password = prompt('输入您的密码');
                        $.ajax({
                            url:'/account/password',
                            dataType:'json',
                            type:'post',
                            data:{password:password},
                            success:function(result)
                            {
                                window.location.href = "/toaccount"
                            }
                        })
                    }   
                }
            })
        }
    });


});