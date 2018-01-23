$(document).ready(function(){
	var url = window.location.href;
	var id = url.replace(/.*\//,'');
	var arr=url.split('/');
	var shopId = arr[4]; // 店铺id

	$.ajax({
		url:'/combo',
		dataType:'json',
		type:'post',
		data:{cid:id},
		success:function(result)
		{
			new Vue({
				el:'#combo',
				data:{
					cms:result
				},
				methods:{
					sub:function()
					{
						var num = $('.J-cart-quantity').val()
						num = parseInt(num);
						if(num > 1)
						{
							$('.J-cart-quantity').val(num - 1);
						}
					},
					add:function()
					{
						var num = $('.J-cart-quantity').val()
						num = parseInt(num);
						$('.J-cart-quantity').val(num + 1);
					}
				}
			})
		}
	})

	$.ajax({
		url:'/shop/combo',
		dataType:'json',
		type:'post',
		data:{sid:shopId},
		success:function(result)
		{
			new Vue({
				el:'#shop-combo',
				data:{
					cas:result
				}
			})
		}
	})

	$.ajax({
		url:'/combo/content',
		dataType:'json',
		type:'post',
		data:{cid:id},
		success:function(result)
		{
			new Vue({
				el:'#sub-combo',
				data:{
					cname:result[0]["cname"],
					subs:result,
					snum:result.length + 1
				}
			})
		}
	})
    //  美团推荐
	$.ajax({
		url:'/combo/recommend',
		dataType:'json',
		type:'post',
		data:{sid:shopId},
		success:function(result)
		{
			new Vue({
				el:'#recommended',
				data:{
					rss:result
				}
			})
		}
	})

	// 获取商户图片
	$.ajax({
		url:'/combo/shoppic',
		dataType:'json',
		type:'post',
		data:{sid:shopId},
		success:function(result)
		{
			new Vue({
				el:'#anchor-bizinfo',
				data:{
					sname:result[0]["shop_name"],
					pics:result
				}
			})
		}
	})
})