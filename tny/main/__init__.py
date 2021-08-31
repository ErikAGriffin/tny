from flask import Blueprint, abort, redirect
import redis as RedisConn

def create_main_blueprint(config, redis):
    main = Blueprint('main', __name__)

    @main.route("/")
    def index():
        return "<h1>Tny.</h1><p>A URL shortener.</p>"

    @main.route("/<string:url_hash>")
    def resolve_url(url_hash):
        print(f"url hash: {url_hash}")
        url = redis.get_url(url_hash)
        print(f"redis response: {url}")
        if url:
            return redirect(url)
        else:
            abort(404)

    return main
