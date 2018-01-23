$(document).ready(function(){
	//  获取个人信息
	$.ajax({
		url:'/account',
		dataType:'json',
		type:'post',
		success:function(result)
		{
			new Vue({
				el:'#huser',
				data:{
					username:result[0]['nickname']
				}
			})
		},
		error:function(err)
		{
			console.log(err)
		}
	})

	// 获取订单信息
	$.ajax({
		url:'/transaction/payment',
		dataType:'json',
		type:'get',
		success:function(result)
		{
			new Vue({
				el:'#trade',
				data:{
					tss:result
				}
			})
		},
		error:function(err)
		{
			console.log(err)
		}
	})
})