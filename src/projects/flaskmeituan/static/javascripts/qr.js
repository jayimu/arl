$(document).ready(function () {
    var url = window.location.href;
    var id=url.split("#");
    //alert(id[1]);
    //生成二维码
    new Vue({
       el: '#main',
       data: {
            url:"http://paysdk.weixin.qq.com/example/qrcode.php?data="+id[1]
          }
       })
        
    run();
    
});

function run() {
    setInterval(function(){
        setInterval(chat(),2000);
    },2000)
}
function chat() {

    $.ajax({ //获取订单状态是否成功
        url:'/pay/order',
        dataType: "text",
        type:'post',
        success: function (result) {

            if(result=='SUCCESS'){
                $.ajax({ 
                    url:'/update',
                    dataType: "text",
                    type:'post',
                    success:function (result) {
                        if(result=="1"){
                            alert("购买成功！");
                            window.location.href='/'
                        }

                    },
                    error:function(e){
                    	console.dir(e);
                    	alert(e);
                    }
                })
            }

        },
        error:function (err) {
            console.log("123");
        }
    })
}
function getUrlParam(name)
{
    var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
    var r = window.location.search.substr(1).match(reg);  //匹配目标参数
    if (r!=null) return unescape(r[2]); return null; //返回参数值
}
