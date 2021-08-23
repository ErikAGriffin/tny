from flask import Blueprint, abort, request
import redis as RedisConn
from dotenv import load_dotenv
from os import environ
import secrets
import re

load_dotenv()

api = Blueprint('api', __name__)

redis = RedisConn.Redis(
    host=environ.get('REDIS_HOST'),
    port=environ.get('REDIS_PORT'),
    db=0,
    decode_responses=True
)

def store_url(url):
    while True:
        url_hash = secrets.token_urlsafe(5)
        if not redis.get(url_hash):
            redis.set(url_hash, url)
            return url_hash

def get_url(short_url):
    prefix_regex = re.compile(f"(https?://)?{environ.get('TNY_HOSTNAME')}/+",re.I)
    url_hash = prefix_regex.sub('', short_url)
    return redis.get(url_hash)

@api.route("/urls", methods=['POST'])
def create():
    url = None
    http_regex = re.compile(r"^https?://", re.I)
    url_regex = re.compile(r"^(http(s)?://.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)", re.I)
    if request.form:
        url = request.form.get('url')
    elif request.is_json:
        url = request.get_json().get('url')
    if not url or not url_regex.match(url):
        abort(400)
    if not http_regex.match(url):
        url = "http://" + url
    url_hash = store_url(url.rstrip())
    return {
        'short_url': f"http://{environ.get('TNY_HOSTNAME')}/{url_hash}"
    }

@api.route("/urls")
def return_url():
    short_url = None
    if request.form:
        short_url = request.form.get('url')
    elif request.is_json:
        short_url = request.get_json().get('url')
    if not short_url:
        abort(400)
    long_url = get_url(short_url)
    if not long_url:
        abort(404)
    return { 'original_url': long_url }
