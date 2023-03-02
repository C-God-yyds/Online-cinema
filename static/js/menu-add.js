
// 加载父菜单下拉列表
var load_parent_menus = function(select_obj){
    var menu_level = $(select_obj).val()  // 获取当前下拉列表选中的选项的值

    if(menu_level == 1){ // 判断是不是要新增的一级菜单
        var option = "<option value='0'>默认父菜单</option>"
        $("#parent_id").html(option)
        return false  // 如果是新增一级菜单，给付菜单下拉列表拼接一个option选择，中断函数
    }

    /*
    ajax，最大特点，请求异步，触发了请求就算ajax的函数执行完了，
    ajax的回调函数success，由后台在返回值之后触发调用

    如果你的需求中确实有需要回调函数执行完才能执行的代码，有2种处理方式
    1、把需要在回调函数执行完后在执行的逻辑放到回调函数中去
    2、把ajax设置为同步请，ajax的回调必须执行完成才会继续往下执行其他的js代码
    */
    // 去后台查询一级菜单的所有数据，组装父菜单的下拉列表
    $.ajax({
        type: "post",
        url: "/menu/first/all",
        data: {},
        async: false, // 设置ajax为同步请求，默认async是true（异步）
        dataType: "json",
        success: function(data){
            // 拼接下拉列表的option选项
            /*
            data =
            [
            {'id': 25, 'menu_code': 'menu-1-template', 'menu_level': '1', 'menu_name': '一级菜单', 'menu_url': '', 'parent_id': 0, 'sort': 1},
            .....
            ]
            */
            var option = "<option value=''>--请选择--</option>"
            // 遍历data
            $.each(data, function(index, menu){
                option += "<option value='" + menu.id + "'>" + menu.menu_name + "</option>"
            })

            // 把拼接好的option放到父菜单的下拉列表中
            $("#parent_id").html(option)
        }
    })
}

/*
提交新增菜单
也是提交修改菜单
对submit_from做改进，兼容新增和修改
*/
var submit_from = function(){
    // isUpdate，如果是新增页面false，修改页true
    var isUpdate = $("#id").val() == "" ? false : true
    // 修改比新增多一个参数，隐藏域的id

    // 组装请求参数，表单对象（输入框、下拉列表。。。）获取的值都是$("#menu_code").val()
    var params = {
        "menu_code": $("#menu_code").val(),
        "menu_name": $("#menu_name").val(),
        "menu_url": $("#menu_url").val(),
        "menu_level": $("#menu_level").val(),
        "parent_id": $("#parent_id").val(),
        "sort": $("#sort").val()
    }

    var url = "/menu/"
    var str = ""
    if(isUpdate){
        params["id"] = $("#id").val()
        url += "update"
        str = "修改"
    }else{
        url += "add"
        str = "新增"
    }
    // 如果新增页，url="/menu/add"，str = "新增"
    // 如果修改页，url="/menu/update"，str = "修改"，params多一个参数

    $.ajax({
        type: "post",
        url: url,
        data: params,
        dataType: "json",
        success: function(data){
            /*
            data = {"code":"200"}
            data = {"code":"999"}
            */
//            if(data.code == "999"){
//                alert("新增菜单失败！")
//            }else{
//                alert("新增菜单成功！")
//            }

            var msg = str + "菜单" + (data.code == "999" ? "失败" : "成功") + "!"
            alert(msg)
        }
    })
}