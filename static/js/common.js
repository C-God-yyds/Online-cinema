/*
加载html页面代码到指定的位置
参数是json
{
"url": "xxx.html",  // 加载的html的路径
"dom_id": "xxxxx",  // 想哪个元素块加载html代码，值就是这个dom元素的id
"func": function(){}  // 在dom元素加载完html代码后，需要做的额外操作
}
*/
var loadHtml = function(obj){
	$.ajax({
		type:"get",
		url:"/static/pages/" + obj.url, //需要获取bai的页面du内容
		async:true,
		success:function(data){ // data就是ajax读取html文件的代码
			//console.log(id);
			// 把读取的html文件的代码加载到dom_id对应块中
			$("#" + obj.dom_id).html(data)
			// obj.func只是获取obj对象的func，后面加()是执行函数
			if(obj.func){
                if($.isFunction(obj.func)){
                    obj.func()
                }
            }
		}
	});
}

// 公共根据表单元素的id的数组组装请求json
var create_params = function(params_ids){
    var params = {}
    $.each(params_ids, function(index, param_id){
        params[param_id] = $("#" + param_id).val()
    })
    return params
}


/*
公共的提交新增修改请求
参数submit_form_params是json对象
{
    "params": params, // 表单请求参数json对象
    "prefix": prefix, // ajax请求url的一级路径
    "model_name"：model_name // 操作的模块名
}
*/
var submit_add_update = function(submit_form_params){
    // isUpdate，如果是新增页面false，修改页true
    var isUpdate = $("#id").val() == "" ? false : true

    var url = submit_form_params.prefix
    var str = ""
    if(isUpdate){
        submit_form_params.params["id"] = $("#id").val()
        url += "update"
        str = "修改"
    }else{
        url += "add"
        str = "新增"
    }

    str += submit_form_params.model_name
    // 如果新增页，url="/menu/add"，str = "新增"
    // 如果修改页，url="/menu/update"，str = "修改"，params多一个参数

    $.ajax({
        type: "post",
        url: url,
        data: submit_form_params.params,
        dataType: "json",
        success: function(data){
            var msg = str + (data.code == "999" ? "失败" : "成功") + "!"
            alert(msg)
        }
    })
}

/*
公共删除组件，参数是json对象
{
    "prefix": "/role/",
    "model_name": "角色",
    "id": id
}
*/
var del_by_json = function(params){
    $.ajax({
        type: "post",
        url: params.prefix + "del/id",
        data: {"id": params.id},
        dataType: "json",
        success: function(data){
            var msg = "删除" + params.model_name + (data.code == "200" ? "成功" : "失败") + "!"
            alert(msg)
        }
    })
}

/*
公共加载下拉列表组件
{
    "tab_name": "language", // 查询的表名
    "value": "id", // 想要填到option的value的数据的对应的字段名
    "text": "language", // 想要填到option的text的数据的对应的字段名
    "dom_id": "language_id" // 组装下拉列表的下拉列表id
}
*/
var create_select = function(params){
    $.ajax({
        type: "post",
        url: "/admin/load/select",
        data: {"tab_name": params.tab_name},
        dataType: "json",
        success: function(data){
            var option = "<option value=''>--请选择--</option>"
            $.each(data, function(index, obj){
                option += "<option value='" + obj[params.value] + "'>" + obj[params.text] + "</option>"
            })
            $("#" + params.dom_id).html(option)
        }
    })
}