$(function(){
    load_roles()
})

// 加载角色下拉列表
var load_roles = function(){

    $.ajax({
        type: "post",
        url: "/role/all",
        data: {},
        dataType: "json",
        success: function(data){
            var option = "<option value=''>--请选择--</option>"
            $.each(data, function(index, role){
                option += "<option value='" + role.role_code + "'>" + role.role_name + "</option>"
            })
            $("#role_code").html(option)
        }
    })
}

// 提交新增或修改
var submit_form = function(){
    var params_ids = ["username","password","real_name","job_no","role_code"]
    // 组装请求参数，表单对象（输入框、下拉列表。。。）获取的值都是$("#menu_code").val()
    var params = create_params(params_ids)

    var prefix = "/admin/"  // 请求前缀，一级路径
    var model_name = "用户"  // 操作的模块的名称

    var submit_form_params = {
        "params": params,
        "prefix": prefix,
        "model_name": model_name
    }

    submit_add_update(submit_form_params)
}