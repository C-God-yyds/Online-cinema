var login = function(){
    // 根据id从输入框获取值
    var username = $("#username").val()
    var password = $("#password").val()

    // 校验
    if(username == ""){
        alert("用户名不能为空！")
        return false // 函数终止
    }

    if(password == ""){
        alert("密码不能为空！")
        return false // 函数终止
    }


    // ajax提交请求
    $.ajax({
        type: "post",
        url: "/admin/login",
        async: false,
        data: {
            "username": username,
            "password": password
        },
        dataType: "json",
        success: function(data){
            // 判断data.code是不是200，是就是登录成功，跳转index页
            if(data.code == "200"){
                window.location.href = "/admin/index.html"
            }else{
                alert("用户名或者密码错误！")
            }
        }
    })


    $.ajax({
        type: "post",
        url: "/admin/index.html",
        data: {
            "username": username,
            "password": password
        },
        dataType: "json",
        success: function(data){
            login_name()
            document.getElementById("login_name").innerHTML= data.username
        }
    })
}


