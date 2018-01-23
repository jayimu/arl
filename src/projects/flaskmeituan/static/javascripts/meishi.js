$(document).ready(function(){

	var allshop = new Vue({
		el:'#shop',
		data:{
			shops:[]
		}
	})
	//  获取美食的分类
	$.ajax({
		url:'/sub_field',
		dataType:'json',
		type:'get',
		success:function(result)
		{
			new Vue({
				el:'#subfields',
				data:{

					subfields:result
				},
				methods:{
				    sub:function(e)
				    {
				    	var subId = parseInt(e.target.getAttribute('data-id'));
						$.ajax({
							url:'/meishi/click',
							dataType:'json',
							type:'post',
							data:{sub_id:subId},
							success:function(result)
							{
								allshop.shops = result
							}
						})				    	
				    }
				}
			})
		}
		,
		error:function(err)
		{
			console.log(err);
		}
	})

	$.ajax({
		url:'/district',
		dataType:'json',
		type:'post',
		success:function(result)
		{
			new Vue({
				el:'#district',
				data:{
					districts:result
				},
				methods:{
					onClick_District:function(e)
					{
				    	var areaId = parseInt(e.target.getAttribute('data-id'));
						$.ajax({
							url:'/district/click',
							dataType:'json',
							type:'post',
							data:{area_id:areaId},
							success:function(result)
							{
								allshop.shops = result
							}
						})				    	

					}
				}
			})  
		}
	})

	$.ajax({
		url:'/meishi/shop',
		dataType:'json',
		type:'post',
		success:function(result)
		{
			allshop.shops = result
		}
	})

	$('.tag-sort').click(function(){
		var sortType = $('.tag-sort').attr('data-id');
        if(sortType == '0')
        {
        	$('.tag-sort').attr('data-id','1');
        	$.ajax({
        		url:'/meishi/up',
        		dataType:'json',
        		type:'post',
        		success:function(result)
        		{
        			allshop.shops = result
        		}
        	})
        	

        }
        else
        {
        	$('.tag-sort').attr('data-id','0');
        	$.ajax({
        		url:'/meishi/down',
        		dataType:'json',
        		type:'post',
        		success:function(result)
        		{
        			allshop.shops = result
        		}
        	})
        }
	})
	
})