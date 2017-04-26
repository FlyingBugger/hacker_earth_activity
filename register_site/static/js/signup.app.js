$(function () {
	$('p.msg').hide()

	$('.back').click(function () {
		window.location.href = '/'
	})

	$('form.form-container').on('submit', function (e) {
		var self = this
		e.preventDefault()
		var formData = new FormData(self)
		$.ajax({
			url: $(self).attr('action'),
			type: $(self).attr('method'),
			data: formData,
			processData: false,
			contentType: false,
			success: function (res) {
				console.log('success')
				console.log(res)
				$('p.msg').show()
				// setTimeout(function () {window.location.href = '/'}, 1000)
			},
			error: function (xhr) {
				console.log('failed')
				console.log(xhr)
				if (xhr.status === 403) {
					alert('无权作此操作, 请联系管理员')
				}
				let json = xhr.responseJSON
				
				for (let i of ['email', 'phone', 'name', 'grade', 'campus']) {
					if (json[i]) {
						console.log(i)
						$('[name={0}]'.format(i)).toggleClass('error')
					}
				}
			}
		})
	})
})