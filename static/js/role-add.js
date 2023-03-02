$(function(){
    load_menu_tree()
})

// 加载菜单树
var load_menu_tree = function(obj){
    var setting = {
        check: {
            enable: true
        },
        data: {
            // simpleData简单数据格式，就是json格式的
            simpleData: {
                enable: true,
                idKey: "id", // 用你自己的数据中的什么属性作为节点的id
                pIdKey: "parent_id", // 用你自己的数据中的什么属性作为节点的pId
                rootPId: "0"
            },
            key: {
                name: "menu_name" // 用你自己的数据中的什么属性作为节点的name
            }
        }
    };

    var zNodes =[
        { id:1, pId:0, name:"随意勾选 1", open:true},
        { id:11, pId:1, name:"随意勾选 1-1", open:true},
        { id:111, pId:11, name:"随意勾选 1-1-1"},
        { id:112, pId:11, name:"随意勾选 1-1-2"},
        { id:12, pId:1, name:"随意勾选 1-2", open:true},
        { id:121, pId:12, name:"随意勾选 1-2-1"},
        { id:122, pId:12, name:"随意勾选 1-2-2"},
        { id:2, pId:0, name:"随意勾选 2", checked:true, open:true},
        { id:21, pId:2, name:"随意勾选 2-1"},
        { id:22, pId:2, name:"随意勾选 2-2", open:true},
        { id:221, pId:22, name:"随意勾选 2-2-1", checked:true},
        { id:222, pId:22, name:"随意勾选 2-2-2"},
        { id:23, pId:2, name:"随意勾选 2-3"}
    ];

    $.ajax({
        type: "post",
        url: "/menu/all",
        data: {},
        dataType: "json",
        success: function(data){
            $.fn.zTree.init($("#treeDemo"), setting, data);
            if(obj && obj.func){
                if($.isFunction(obj.func)){
                    obj.func()
                }
            }
        }
    })
}

// 提交新增或修改
var submit_form = function(){
    var params_ids = ["role_code","role_name"]
    // 组装请求参数，表单对象（输入框、下拉列表。。。）获取的值都是$("#menu_code").val()
    var params = create_params(params_ids)

    // 获取选中的所有节点的menu_code，组装到请求参数json对象中
    params["codes"] = get_znodes_checked()

    var prefix = "/role/"  // 请求前缀，一级路径
    var model_name = "角色"  // 操作的模块的名称

    var submit_form_params = {
        "params": params,
        "prefix": prefix,
        "model_name": model_name
    }

    submit_add_update(submit_form_params)
}

// 获取ztree选中的节点
var get_znodes_checked = function(){
    // 获取ztree对象
    var zTreeObj = $.fn.zTree.getZTreeObj("treeDemo")

    // 获取选中的节点
    var nodes = zTreeObj.getCheckedNodes(true)

    var codes = ""
    // 遍历
    $.each(nodes, function(index, node){
        // 取menu_code
        codes += "," + node.menu_code
    })

    // ,ssdad,dsadas,dassd，去掉第1个逗号
    codes = codes.substring(1, codes.length)

    return codes
}