String.prototype.format = function() {
    var formatted = this
    for (var i = 0; i < arguments.length; i++) {
        var regexp = new RegExp('\\{'+i+'\\}', 'gi')
        formatted = formatted.replace(regexp, arguments[i])
    }
    return formatted
}

$(function () {
	$('html').css('zoom', $(window).width() / 750)

	var u = navigator.userAgent;
	var isAndroid = u.indexOf('Android') > -1 || u.indexOf('Adr') > -1; //android终端
	var isiOS = !!u.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/); //ios终端
	if (!isiOS) {
		$('body').addClass("android_body")
		$('.text').addClass("android_text")
		$('.title').addClass("android_text")
		$('.time > .date').addClass("android_text_time")
		$('.role').addClass("android_reference_small")
		$('.inst').addClass("android_reference_big")
		$('.qq').addClass("android_reference_big")
		$('.btn-signup').addClass("android_register_now")
		$('form.form-container > input').addClass("android_input")
		$('form.form-container > select').addClass("android_input")
		$('form.form-container > button').addClass("android_button_register")
		$('.msg').addClass("android_msg")
		$('.time > .limit').addClass("android_limit")
		$('.time > .date').addClass("android_date")
	}
})



