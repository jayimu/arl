function checkpasswd()
{
	var passwd = $('.J-pwd').val()
	var repasswd = $('.J-pwd2').val()
    if(passwd == repasswd)
    {
    	return true;
    }
    else
    {
    	window.alert('两次输入的密码不一致');
    	return false;
    }
}