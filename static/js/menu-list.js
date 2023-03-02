$(function () {
    load_page_list()
});


// 加载菜单列表
var load_page_list = function(){
  $("#jsGrid1").jsGrid({
      //height: "100%",
      height: "auto",
      width: "100%",

      sorting: true,  // 支持前端排序
      paging: true,  // 是否做页数的计算，12345 Next Last
      pageLoading: true, //启动后台加载分页数据，设置请求到后台从后台读取数据
      autoload: true, //自动加载，加载页面完成之后，自动的触发请求到后台读取数据
      controller: { // 请求后台的url和参数等的设置，类似ajax
        /*
        filter，JSGrid给后台的请求的参数，是一个json对象
        {
        pageIndex: 值
        pageSize: 值
        }
        */
        loadData: function(filter){
            filter["search"] = $("#search").val()
            return $.ajax({
                type: "post",
                url: "/menu/list/page",
                dataType: "json",
                data: filter
            })
        }
      },
      pageIndex: 1, // 当前页数，是第几页
      pageSize: 3, // 每页数据条数
      pageButtonCount: 10, // 最大展示可选页码数量
      pagePrevText: "上一页",
      pageNextText: "下一页",
      pageFirstText: "首页",
      pageLastText: "尾页",


      // data: db.clients, // 加载静态数据，由db.clients提供

      /*
       根据返回的json数组的元素组装表格
       name: "abc"，指定当前配置这一列展示什么数据，展示json中k是abc的值
       type: "text"，数据类型
       title: ""，表头的列名，如果不配置这个，默认取你的当前列对应的json的k
       */
      fields: [
          { title: "id", name: "id", type: "text", width: 10 },
          { title: "菜单编码", name: "menu_code", type: "text", width: 50 },
          { title: "菜单名称", name: "menu_name", type: "text", width: 50 },
          { title: "菜单级别", name: "menu_level", type: "text", width: 30 },
          { title: "父菜单", name: "parent_menu_name", type: "text", width: 30 },
          { title: "排序", name: "sort", type: "text", width: 20 },
          {
            title: "操作", name: "id", type: "text", width: 30,
            itemTemplate: function(value, item){
                // value当前的格的值，当前这行的json的id的key对应值
                // item就是当前这一行数据的json对象

                // return返回的值就是输出格的html内容
                return "<a href='javascript:void(0)' onclick='update(" + value + ")'>修改</a>"
                    + "&nbsp;&nbsp;&nbsp;&nbsp;<a href='javascript:void(0)' onclick='del(" + value + ")'>删除</a>"
            }
          }
      ]
  });
}

// 修改
var update = function(id){
    // 新增修改是一个页面，点击列表的修改按钮，在正文部分重新加载add页面
    /*
    加载html页面代码到指定的位置
    参数是json
    {
    "url": "xxx.html",  // 加载的html的路径
    "dom_id": "xxxxx",  // 想哪个元素块加载html代码，值就是这个dom元素的id
    "func": function(){}  // 在dom元素加载完html代码后，需要做的额外操作
    }
    */
    loadHtml({
        "url": "menu-add.html",
        "dom_id": "content",
        "func": function(){
            // 到了能执行func的阶段，必定已经加载完menu-add.html，获取menu-add页面的元素
            $("#id").val(id)
            // 现在是要做修改，新增的页面加载了，需要去先根据id查询要修改的数据
            // 把数据回填add页面相应的位置
            $.ajax({
                type: "post",
                url: "/menu/get/id",
                data: {"id": id},
                dataType: "json",
                success: function(data){
                    // 把获取的menu数据，填写add页面的表单元素
                    $("#menu_code").val(data.menu_code)
                    $("#menu_code").attr("readonly", "readonly")

                    $("#menu_name").val(data.menu_name)
                    $("#menu_url").val(data.menu_url)
                    $("#menu_level").val(data.menu_level)

                    $("#sort").val(data.sort)

                    /*
                    到这，menu-add.html已经加载了，包括menu-add.html中引用的js文件也加载完成
                    load_parent_menus属于menu-add.html中menu-add.js的方法
                    */
                    // 根据现在的menu_level下拉列表的回填选项，加载父菜单下拉列表
                    load_parent_menus($("#menu_level"))

                    /*
                    先加载父菜单下拉列表，然后才能设置父菜单的选中
                    ajax，默认是异步请求，load_parent_menus的主体就是一个ajax，组装父菜单下拉列表在回调函数中做的
                    在等待后台触发回调函数的过程中，js不会卡在ajax这走，会继续往下执行其他的js
                    直到回调函数被调用，相当于回调函数是单独开启一个线程执行
                    所以，在等待触发回调函数的时候，已经设置父菜单的选中
                    $("#parent_id").val(data.parent_id)和等待回调在两个线程中
                    看谁快，谁先执行
                    */
                    $("#parent_id").val(data.parent_id)

                }
            })
        }
    })
}

var del = function(id){
    // 可以在删除之前，先判断一下，这个菜单有没有下属菜单，有下属菜单就提示，有下属菜单是否删除，如果是就连在下属菜单一起删除
    // 删除下属菜单delete from menu where parent_id = id
    del_by_json({
        "prefix": "/menu/",
        "model_name": "菜单",
        "id": id
    })
}