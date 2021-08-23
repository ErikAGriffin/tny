from flask import Blueprint, abort, redirect
import redis as RedisConn
from os import environ

main = Blueprint('main', __name__)

redis = RedisConn.Redis(
    host=environ.get('REDIS_HOST'),
    port=environ.get('REDIS_PORT'),
    db=0,
    decode_responses=True
)

@main.route("/")
def index():
    return "<h1>Tny.</h1><p>A URL shortener.</p>"

@main.route("/<string:url_hash>")
def resolve_url(url_hash):
    url = redis.get(url_hash)
    if url:
        return redirect(url)
    else:
        abort(404)
