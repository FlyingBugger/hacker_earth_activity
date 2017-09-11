(function(window, document, undefined) {
'use strict';
// var host = 'https://www.hackerearth.cn/';

var host='http://salon.hackerearth.cn/';
var rout_host='salon.hackerearth.cn/'
var API_root = '';
var API_host = host + API_root;

var App = window.App = {};
var Util = App.Util = {};
var Api = App.Api = {};
var Consist = App.Consist = {};
var Config = App.Config = {};
var Page = App.Page = {};
var Check = App.Check = {};

var Route = App.Route = {
    top: rout_host,
    form: 'get_form'
};


/*
 * on domContentLoaded
 */
$(function () {
    var pathname = window.location.href.match(".+/(.+?)([\?#;].*)?$")[1];
//    console.log(pathname)
    /*
     * all
     */
    Util.dispatcher('.', function () {
        Page.all.init();
        Page.top.init();
    });

    /*
     * each page
     */
    if (pathname == Route.top) {
        Util.dispatcher(Route.top, function () {
            Config.currentPage = Route.top;

        });

    } else if (pathname == Route.form) {
        Util.dispatcher(Route.sprint, function () {
            Config.currentPage = Route.form;
            Page.form.init();
        });
    }

    // dispatch
    Util.dispatcher(pathname);
});

Consist.msg ={
    "empty":"请输入完整",
    "email":"请正确填写邮箱",
    "phone":"请正确填写电话",
    "longest":function(key,length) {
        return key+'超过最大限制'+length+'个字符'
    }
};

/*
 * ajax
 */
Util.ajax = function (_option) {
    var baseUrl = _option.url;
    var query = {};
    var $defer = $.Deferred();
    $.extend(query, _option.params);
    if (_option.params) {
        baseUrl = baseUrl + '?' + $.param(query);
    }
    var opt = {
        url: API_host.path_join(baseUrl),
        type: _option.type,
        dataType: _option.dataType,
        data: _option.data,
        success: $defer.resolve,
        error: $defer.reject
    };
    $.ajax(opt);
    return $defer.promise();
};

Util.alert = {
  warning: function (info) {
    var $alert = $('.form-info');
    $alert.removeClass('hidden').addClass('alert-warning').text(info);
    setTimeout(function () {
      $alert.text();
      $alert.removeClass('alert-warning').addClass('hidden');
    }, 3000);
  },

  danger: function (info) {
    var $alert = $('.form-info');
    $alert.removeClass('hidden').addClass('alert-danger').text(info);
    setTimeout(function () {
      $alert.text();
      $alert.removeClass('alert-danger').addClass('hidden');
    }, 3000);
  }
};

/*
 * dispatcher
 */
Util.dispatcher = function (path, callback) {
    this.path_func = this.path_func || [];

    if (callback) return this.path_func.push([path, callback]);

    for (var i = 0, l = this.path_func.length; i < l; ++i) {
        var func = this.path_func[i];
        var match = path.match(func[0]);
        match && func[1](match);
    }
};

/*
 * input
 */
Util.input = {
  clear: function (_option) {
    for (var i = 0; i < _option.length; i++) {
      $('#' + _option[i].key).val('');
    }
  },

  keydown: function ($input) {
    $input.on('keydown', function (e) {
      var keydown = e.which;
      if (keydown == 13) {
        e.preventDefault();
        var nxt_idx = $input.index(this) + 1;
        $input.eq(nxt_idx).focus();
      }
    });
  }
};

Util.json = {
    key_arr: function (option) {
        var key_arr = [];
        for (var key in option) {
            key_arr.push(key);
        }
        return key_arr;
    },
    get_length: function (option) {
        var length = 0;
        for (var item in option) {
            length++;
        }
        return length;
    }
};

/*
 *modal
 */
Util.modal = function () {
  $('body').addClass('no-scroll');
  $('.modal').removeClass('hidden');
  $('.close-btn').click(function () {
    $('body').removeClass('no-scroll');
    $('.modal').addClass('hidden');
    setTimeout(function(){
    window.location.href="/"
    },1000)
  })

};

Util.smooth_scroll = (function () {
    $('a.page-scroll').click(function () {
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
        if (target.length) {
            $('html,body').animate({
                scrollTop: target.offset().top - 40
            }, 900);
            return false;
        }
    })
})();

/*
 * String helper
 */
Util.string = (function () {
    return {
        path_join: function () {
            String.prototype.path_join = function () {
                var current = this,
                    args = Array.prototype.slice.call(arguments);

                args.forEach(function (elem, i) {

                    var ending = current[current.length - 1],
                        starting = elem[0];

                    if (ending !== '/')
                        current = current + '/';

                    if (starting === '/')
                        current += elem.substring(1);
                    else
                        current += elem
                });

                return current
            };
        },
        format: function () {
            String.prototype.format = function () {
                var formatted = this;
                for (var i = 0; i < arguments.length; i++) {
                    var regexp = new RegExp('\\{' + i + '\\}', 'gi');
                    formatted = formatted.replace(regexp, arguments[i])
                }
                return formatted
            };
        },
        insert: function () {
            Array.prototype.insert = function (index, item) {
                this.splice(index, 0, item);
            };
        },
        DBC2SBC: function (string) {
            if (string) {
                var result = "";
                var len = string.length;
                for (var i = 0; i < len; i++) {
                    var c_code = string.charCodeAt(i);
                    c_code = (c_code >= 0xFF01 && c_code <= 0xFF5E) ? (c_code - 65248) : c_code;
                    //空格处理
                    c_code = (c_code == 0x03000) ? 0x0020 : c_code;
                    result += String.fromCharCode(c_code);
                }
                return result;
            }
        }
    }
})();

Check.email = function (email) {
  email = email || '';
  return (email.length > 3 && email.indexOf('@') > -1);
};

Check.number = function (number) {
  var numberreg = /^\+?[1-9][0-9]*$/;
  return (numberreg.exec(number))
};

Check.phone = function (phone) {
  var phonereg = /^((\d{3,4}-)?\d{7,8})?(1[3587]\d{9})?$/;
  return (phonereg.exec(phone) && phone.length == 11)
};

//common verify
Check.verify_item = function (key, value, callback) {
  if (key === 'name') {
    if (value.length > 20) {
      return callback(Consist.msg.longest('姓名', 20))
    }
  }
  if (key === 'company') {
    if (value.length > 40) {
      return callback(Consist.msg.longest('公司名称', 40))
    }
  }

  if (key === 'jobtitle') {
    if (value.length > 15) {
      return callback(Consist.msg.longest('职位', 15))
    }
  }

};

Check.verify = function ($dom) {
  var key = $dom.attr('id');
  var _value = $dom.val();
  var value = $.trim(Util.string.DBC2SBC(_value));
  $("#" + key).val(value);

  if (key === 'email') {
    if (value.length > 100) {
      Util.alert.danger(Consist.msg.longest('邮箱', 100))
      return false;
    }
    if ($("#" + key).val === '' && !Check.email(value)) {
      Util.alert.danger(Consist.msg.email)
      return false;
    }
  } else if (value === '') {
    Util.alert.warning(Consist.msg.empty);
    return false;
  } else {
    Check.verify_item(key, value, function (err) {
      if (err) {
        Util.alert.danger(err);
        return false;
      }
    });

  }

  return true;
};

//submit of form
Util.form_submit = function () {

  var $form = $('#form_item');
  var $input = $form.find('input');
  var option = {
    "name": "",
    "company": "",
    "phone": "",
    "email": "",
    "jobtitle": ""
  };

  Util.input.keydown($input);

  $form.on('submit', function (e) {
    e.preventDefault();
    var option_len = Util.json.get_length(option);
    var key_arr = Util.json.key_arr(option);

    var has_error = false;
    for (var i = 0; i < option_len; i++) {
      var option_key = key_arr[i];
      var $item = $('#' + option_key);
      option[option_key] = $item.val();

      if (option_key === "csrfmiddlewaretoken") {
        continue;
      }

      if (Check.verify($item, option) === false) {
        has_error = true
      }
    }
    if (has_error) {
      return;
    }
    option.csrfmiddlewaretoken = $("input[name='csrfmiddlewaretoken']").val();

     Api.form.submit(option)
       .done(function (_data) {
         if (_data.status == '200') {
          Util.modal();
         Util.input.clear(option);
       }
     })
     .fail(function (err_msg, error) {
       if (err_msg.status == '400') {
         for (var key in err_msg.responseJSON){
          Util.alert.danger(err_msg.responseJSON[key]);
         }

       }
//       console.log(err_msg);
     });

  });


};

Api.form = function ($) {
    var submit = function (_option) {
        var $defer = $.Deferred();
        var options = {
            type: 'post',
            url: 'software/commit/',
            data: _option
        };
        Util.ajax(options).done(function (result) {
            $defer.resolve(result);
        }).fail(function (xhr) {
            $defer.reject(xhr);
        });
        return $defer.promise();
    };

    return {
        submit:submit
    };

}(jQuery);

Page.all = (function () {
    var init = function () {
        Util.string.path_join();
        Util.string.format();
    };
    return {
        init: init
    };
})();

Page.form = (function () {
  var init = function () {
    bind();
  };
  var bind = function () {
    Util.form_submit();
  };
  return {
    init: init
  };
})();

Page.top = (function () {
    var init = function () {
        bind();
    };
    var bind = function () {
        $('.btn-action').click(function () {
            window.location.href ='http://salon.hackerearth.cn/get_form';
        });

        Util.form_submit();
    };
    return {
        init: init
    };
})();

})(window, document);
