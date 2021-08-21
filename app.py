from flask import Flask, abort, redirect, request
import redis as RedisConn
import secrets
from os import environ
from dotenv import load_dotenv

load_dotenv()
for env_var in ['REDIS_HOST', 'REDIS_PORT', 'TNY_HOSTNAME']:
    if not environ.get(env_var):
        raise AssertionError(f"{env_var} environment variable must be set.\nPlease check your environment")

app = Flask(__name__)
redis = RedisConn.Redis(host=environ.get('REDIS_HOST'), port=environ.get('REDIS_PORT'), db=0, decode_responses=True)

@app.route("/")
def index():
    return "<h1>Tny.</h1><p>A URL shortener.</p>"

def store_url(url):
    while True:
        url_hash = secrets.token_urlsafe(5)
        if not redis.get(url_hash):
            redis.set(url_hash, url)
            return url_hash

@app.route("/api/create", methods=['POST'])
def create():
    url = None
    if request.form:
        url = request.form.get('url')
    elif request.is_json:
        url = request.get_json().get('url')
    if not url:
        abort(400)
    url_hash = store_url(url.rstrip())
    return {
        'short_url': f"{environ.get('TNY_HOSTNAME')}/{url_hash}"
    }

@app.route("/<string:url_hash>")
def resolve_url(url_hash):
    url = redis.get(url_hash)
    if url:
        return redirect(url)
    else:
        abort(404)
