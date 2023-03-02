$(function(){
    select_init()
    load_labels()
})

var select_init = function(){
    // 1、language_id
    create_select({
        "tab_name": "language", // 查询的表名
        "value": "id", // 想要填到option的value的数据的对应的字段名
        "text": "language", // 想要填到option的text的数据的对应的字段名
        "dom_id": "language_id" // 组装下拉列表的下拉列表id
    })

    // 2、video_type_id
    create_select({
        "tab_name": "video_type", // 查询的表名
        "value": "id", // 想要填到option的value的数据的对应的字段名
        "text": "video_type", // 想要填到option的text的数据的对应的字段名
        "dom_id": "video_type_id" // 组装下拉列表的下拉列表id
    })

    // 3、district_id
    create_select({
        "tab_name": "district", // 查询的表名
        "value": "id", // 想要填到option的value的数据的对应的字段名
        "text": "district", // 想要填到option的text的数据的对应的字段名
        "dom_id": "district_id" // 组装下拉列表的下拉列表id
    })

    // 4、show_type_id
    create_select({
        "tab_name": "show_type", // 查询的表名
        "value": "id", // 想要填到option的value的数据的对应的字段名
        "text": "show_type", // 想要填到option的text的数据的对应的字段名
        "dom_id": "show_type_id" // 组装下拉列表的下拉列表id
    })

    // 4、classification_id
    create_select({
        "tab_name": "classification", // 查询的表名
        "value": "id", // 想要填到option的value的数据的对应的字段名
        "text": "classification", // 想要填到option的text的数据的对应的字段名
        "dom_id": "classification_id" // 组装下拉列表的下拉列表id
    })
}

// 加载标签
var load_labels = function(){
    $.ajax({
        type: "post",
        url: "/admin/load/select",
        data: {"tab_name": "labels"},
        dataType: "json",
        success: function(data){
            var label_template = '<div class="icheck-primary d-inline">'
                                + '  <input type="checkbox" id="c1">'
                                + '  <label for="c1">情感</label>'
                                + '</div>'
            $.each(data, function(index, obj){
                var la = $(label_template)
                $(la).find("input").attr("id", obj.id)
                $(la).find("label").attr("for", obj.id)
                $(la).find("label").text(obj.label)
                $("#labels").append($(la))
            })
        }
    })
}


var submit_form = function(){
    /*
    ajax提交同时有上传文件和普通的文本框值的请求参数的时候
    自己去构建一个form
    */
    var form = new FormData()

    /*
    form.append，有2个参数
    参数1，是请求的参数名，后台接收请求参数的时要使用
    参数2，传递的值
    */
    var ids = ["v_name","director","leading_players",
    "language_id","video_type_id","district_id",
    "synopsis","episodes","release_time","show_type_id","classification_id"]

    $.each(ids, function(index, id){
        form.append(id, $("#" + id).val())
    })
    form.append("v_pic", document.getElementById("v_pic").files[0])

    // 获取所有选中的复选框label
    var label_ids = ""
    $("#labels").find("input[type='checkbox']:checked").each(function(){
        label_ids += "," + $(this).attr("id")
    })
    label_ids = label_ids.substring(1, label_ids.length)
    form.append("label_ids", label_ids)

    /*
    {}的一个json对象，k:v结构
    json对象和字典实际上结构基本上相同
    */
    $.ajax({
        type: "post", // http请求method
        url: "/video-info/add", // 后台的url
        data: form, // 请求参数
        processData: false, // 指定不对请求参数再次转换对象
        contentType: false, // 不设置请求类型
        dataType: "json", // 后台给ajax返回值的类型
        success: function(data){  // 回调函数，异步调用后台，触发了请求之后，ajax就不管了，直到后台return了，后台去触发回调

            alert(data.code == "200" ? "新增成功！" : "新增失败！")  // 参数data，是后台返回的值
        }
    })
}

