$(document).ready(function(){
	var url = window.location.href;
	var id = url.replace(/.*\/toshop\//,'')
	//  获取店铺信息
	$.ajax({
		url:'/shop',
		dataType:'json',
		type:'post',
		data:{sid:id},
		success:function(result)
		{
			new Vue({
				el:'#shop',
				data:{
					shops:result,
					styleObject:{
						background:'url(' + result[0]['shop_cover'] +') no-repeat center'
					}
				}
			})
		}
	})


	$.ajax({
		url:'/shop/combo',
		dataType:'json',
		type:'post',
		data:{sid:id},
		success:function(result)
		{
			new Vue({
				el:'#combo',
				data:{
					cas:result,
					num:result.length,
					shop_id:id
				}
			})
		}
	})
	$.ajax({
		url:'/shop/discuss',
		dataType:'json',
		type:'post',
		data:{sid:id},
		success:function(result){
			new Vue({
				el:'#discuss',
				data:{
					discussions:result
				}
			})
		}
	})
})