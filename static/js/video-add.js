var add_file = function(){
   if($("#upload_files").find(".row").length > 4){
        return false
   }

   // 获取最后一个file的id的数字部分
   var last_id = parseInt($("#upload_files").find(".row").last().find("input[type='file']").attr("id").replace("v_",""))

   last_id += 1

   var file_template = '<div class="row">'
                    + '  <div class="col-md-8">'
                    + '    <input type="file" id="v_' + last_id + '" class="form-control">'
                    + '  </div>'
                    + '  <div class="col-md-2">'
                    + '    <button type="button" class="btn btn-block btn-success btn-sm" onclick="add_file()">+</button>'
                    + '  </div>'
                    + '  <div class="col-md-2">'
                    + '    <button type="button" class="btn btn-block btn-danger btn-sm" onclick="remove_file(this)">-</button>'
                    + '  </div>'
                    + '</div>'

   $("#upload_files").append(file_template)
}


var remove_file = function(obj){
    if($("#upload_files").find(".row").length == 1){
        return false
    }
    $(obj).parent().parent().remove()
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
    var ids = ["v_name","v_code"]

    $.each(ids, function(index, id){
        form.append(id, $("#" + id).val())
    })


    $("#upload_files").find("input[type='file']").each(function(){
        var file_id = $(this).attr("id")
        form.append(file_id, document.getElementById(file_id).files[0])
    })

    /*
    {}的一个json对象，k:v结构
    json对象和字典实际上结构基本上相同
    */
    $.ajax({
        type: "post", // http请求method
        url: "/video/add", // 后台的url
        data: form, // 请求参数
        processData: false, // 指定不对请求参数再次转换对象
        contentType: false, // 不设置请求类型
        dataType: "json", // 后台给ajax返回值的类型
        success: function(data){  // 回调函数，异步调用后台，触发了请求之后，ajax就不管了，直到后台return了，后台去触发回调

            alert(data.code == "200" ? "新增成功！" : "新增失败！")  // 参数data，是后台返回的值
        }
    })
}