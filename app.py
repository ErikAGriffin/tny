from flask import Flask, abort, redirect
import redis as RedisConn

app = Flask(__name__)
redis = RedisConn.Redis(host='localhost', port=6379, db=0, decode_responses=True)

redis.set("test", "https://unitedmasters.com/")

@app.route("/")
def index():
    return "<h1>Tny.</h1><p>A URL shortener.</p>"

@app.route("/<string:url_hash>")
def resolve_url(url_hash):
    url = redis.get(url_hash)
    if url:
        return redirect(url)
    else:
        abort(404)
