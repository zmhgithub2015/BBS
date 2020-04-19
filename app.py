# encoding: utf-8

from flask import Flask

import config
from exts import db
from apps.cms import cms_bp
from apps.common import common_bp
from apps.front import front_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(cms_bp)
    app.register_blueprint(common_bp)
    app.register_blueprint(front_bp)

    db.init_app(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
