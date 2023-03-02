# -*- coding: utf-8 -*-
# author lby
from flask import Flask

from conf.settings import myConfig
from exts import db
from route.admin_route import admin
from route.menu_rute import menu
from route.role_route import role
from route.video_info_route import video_info
from route.video_route import video

app = Flask(__name__)


app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(menu, url_prefix="/menu")
app.register_blueprint(role, url_prefix="/role")
app.register_blueprint(video_info, url_prefix="/video-info")
app.register_blueprint(video, url_prefix="/video")

# 配置信息
app.config.from_object(myConfig["dev"])


# 初始化SQLAlchemy对象
db.init_app(app)


if __name__ == "__main__":
    app.run(port=8080,debug=True)