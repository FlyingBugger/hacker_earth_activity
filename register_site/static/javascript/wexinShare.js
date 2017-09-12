

        $.ajax({
          url:'http://salon.hackerearth.cn/get_wexin_params',
          type:'post',
          data:{
            "share_url":window.location.href.split('#')[0],
            "csrfmiddlewaretoken":$("input[name='csrfmiddlewaretoken']").val(),

          },
          success:function(_data){
           console.log(_data);
             wx.config({
            debug: false, // 开启调试模式,调用的所有api的返回值会在客户端alert出来，若要查看传入的参数，可以在pc端打开，参数信息会通过log打出，仅在pc端时才会打印。
            appId: 'wxb6d7b7803694fc83', // 必填，公众号的唯一标识
            timestamp: _data.timestamp, // 必填，生成签名的时间戳
            nonceStr: _data.nonceStr, // 必填，生成签名的随机串
            signature: _data.signature,// 必填，签名，见附录1
            jsApiList: ["onMenuShareTimeline","onMenuShareAppMessage","onMenuShareQZone","onMenuShareQQ"] // 必填，需要使用的JS接口列表，所有JS接口列表见附录2
        });
             wx.ready(function () {

          var title='沙龙邀请函'// 分享标题
          var desc='大数据时代“人才”+“创新”一体化新生态系统'
          var link='http://salon.hackerearth.cn/'
          var imageUrl='http://salon.hackerearth.cn/media/QQ20170911-150722copy.png'

          wx.onMenuShareAppMessage({
             title: title,
             desc: desc, // 分享描述
             link: link, // 分享链接，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致
             imgUrl: imageUrl, // 分享图标
             type: '', // 分享类型,music、video或link，不填默认为link
             dataUrl: '', // 如果type是music或video，则要提供数据链接，默认为空
             success: function () {
              // 用户确认分享后执行的回调函数
              console.log("分享成功")
            },
             cancel: function () {
              // 用户取消分享后执行的回调函数
              console.log("取消分享")
            }
          })


          wx.onMenuShareTimeline({
            title: title, // 分享标题
            link: link, // 分享链接，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致
            imgUrl: imageUrl, // 分享图标
            success: function () {
              // 用户确认分享后执行的回调函数
              console.log("分享成功")
            },
             cancel: function () {
              // 用户取消分享后执行的回调函数
              console.log("取消分享")
            }
          })

        })


          }
        })

