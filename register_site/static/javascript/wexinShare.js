

$.ajax({
     url:'http://salon.hackerearth.cn/get_wexin_params',
     type:'post',
     data:{
            "share_url":window.location.href.split('#')[0],
            "csrfmiddlewaretoken":$("input[name='csrfmiddlewaretoken']").val(),

     },
     success:function(_data){

        wx.config({
            debug: false,
            appId: 'wxb6d7b7803694fc83',
            timestamp: _data.timestamp,
            nonceStr: _data.nonceStr,
            signature: _data.signature,
            jsApiList: ["onMenuShareTimeline","onMenuShareAppMessage","onMenuShareQZone","onMenuShareQQ"]
        });
        wx.ready(function () {

          var title='沙龙邀请函'// 分享标题
          var desc='大数据时代“人才”+“创新”一体化新生态系统'
          var link='http://salon.hackerearth.cn/'
          var imageUrl='http://salon.hackerearth.cn/media/QQ20170911-150722copy.png'

          wx.onMenuShareAppMessage({
             title: title,
             desc: desc,
             link: link,
             imgUrl: imageUrl,
             type: '', // 分享类型,music、video或link，不填默认为link
             dataUrl: '', // 如果type是music或video，则要提供数据链接，默认为空
             success: function () {
              // 用户确认分享后执行的回调函数
            },
             cancel: function () {
              // 用户取消分享后执行的回调函数
            }
          })


          wx.onMenuShareTimeline({
            title: title,
            link: link,
            imgUrl: imageUrl,
            success: function () {
              // 用户确认分享后执行的回调函数
            },
             cancel: function () {
              // 用户取消分享后执行的回调函数
            }
          })

        })
    }
})


