var loginQrcodePollTimer;
function loginSwitch(type){
        if(type=='verify'){
            getAliCaptcha('two');
            if($("input[name=nameNormal]").val()){
              $("input[name=nameVerify]").val($("input[name=nameNormal]").val());
            }else{
              setTimeout(function() {$("input[name=nameVerify]").focus();}, 10);
            }
            $('#verifyLoginPanel').show();
            $('#normalLoginPanel').hide();
            $('#qrcodeLoginPanel').hide();
            clearInterval(loginQrcodePollTimer);
            window.localStorage.setItem('logintype',0);
            //zhugeTrack('登录-快捷登录');
        }else if(type=='normal'){
            getAliCaptcha('one');
            if($("input[name=nameVerify]").val()){
              $("input[name=nameNormal]").val($("input[name=nameVerify]").val());
            }
            $('#normalLoginPanel').show();
            $('#verifyLoginPanel').hide();
            $('#qrcodeLoginPanel').hide();
            clearInterval(loginQrcodePollTimer);
            window.localStorage.setItem('logintype',1);
            //zhugeTrack('登录-密码登录');
        }else if(type=='qrcode'){
            loginQrcodeGenerate('qrcodeLoginQr');
            loginQrcodePoll('qrcodeLoginQr');
            $('#qrcodeLoginPanel').show();
            $('#normalLoginPanel').hide();
            $('#verifyLoginPanel').hide();
            window.localStorage.setItem('logintype',2);
            //zhugeTrack('登录-二维码登录');
        }
        $('.login-tab a').removeClass('active');
        $('#'+type+'Login').addClass('active');

    }




function setLoginType(){
    if(window.localStorage.getItem('logintype')=='0'){
        $('#normalLogin').click();
    }else if(window.localStorage.getItem('logintype')=='1'){
        $('#normalLogin').click(); 
    }else{
        $('#normalLogin').click();
    }
}
