/*
在html页面加载完毕之后会自动执行的js
*/
$(function(){
    // 加载左侧菜单页
//    loadHtml({
//        "url": "left-menu.html",  // 加载的html的路径
//        "dom_id": "left-menu"  // 想哪个元素块加载html代码，值就是这个dom元素的id
//    })
    create_left_menus()

    // 加载头部页
    loadHtml({
        "url": "header.html",  // 加载的html的路径
        "dom_id": "header"  // 想哪个元素块加载html代码，值就是这个dom元素的id
    })
    // 加载欢迎页
    loadHtml({
        "url": "wolcome.html",  // 加载的html的路径
        "dom_id": "content"  // 想哪个元素块加载html代码，值就是这个dom元素的id
    })
    // 加载尾部页
    loadHtml({
        "url": "footer.html",  // 加载的html的路径
        "dom_id": "footer"  // 想哪个元素块加载html代码，值就是这个dom元素的id
    })
})

var create_left_menus = function(){
    // 一级菜单模板
    var li_1_temp = '<li class="nav-item">'
            + '	<a href="#" class="nav-link">'
            + '	  <i class="nav-icon fas fa-circle"></i>'
            + '	  <p>'
            + '		视频管理'
            + '		<i class="right fas fa-angle-left"></i>'
            + '	  </p>'
            + '	</a>'
            + '</li>'

    // 二级菜单ul部分模板
    var ul_temp = '<ul class="nav nav-treeview"></ul>'

    // 二级菜单li部分模板
    var li_2_temp = '<li class="nav-item">'
                + '  <a href="javascript:void(0)" class="nav-link">'
                + '    <i class="far fa-circle nav-icon"></i>'
                + '    <p>新增视频信息</p>'
                + '  </a>'
                + '</li>'

    $.ajax({
        type: "post",
        url: "/menu/left",
        data: {},
        dataType: "json",
        success: function(data){
            var left_menus = data.left_menus

            $.each(left_menus, function(index, left_menu){
                var first_menu = left_menu.first_menu  // 一级菜单
                var second_menus = left_menu.second_menus  // 二级菜单

                // 构建一级菜单对象
                var menu_1 = $(li_1_temp)
                $(menu_1).find("p").text(first_menu.menu_name)

                // 构建二级菜单的ul对象
                var ul_2 = $(ul_temp)

                // 遍历second_menus，构建具体的二级菜单的li对象
                $.each(second_menus, function(idx, m2){
                    var li_2 = $(li_2_temp)
                    $(li_2).find("p").text(m2.menu_name)  // 文本值

                    // 使用js构建a标签的点击事件
                    $(li_2).find("a").click(function(){
                        loadHtml({
                            "url": m2.menu_url,  // 加载的html的路径
                            "dom_id": "content"  // 想哪个元素块加载html代码，值就是这个dom元素的id
                        })
                    })

                    $(ul_2).append($(li_2))  // 把二级菜单的li追加到ul中
                })

                $(menu_1).append($(ul_2))  // 把ul对象追加到menu_1中

                // 到这一个一级待定和他下属的二级菜单就组装好了，就是$(menu_1)
                $("#left-menu").append($(menu_1))
            })
        }
    })
}


