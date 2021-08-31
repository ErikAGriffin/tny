from flask import Blueprint, abort, request
import secrets
import re

def create_api_blueprint(config, redis):
    print('running create api')
    api = Blueprint('api', __name__)

    def store_url(url):
        while True:
            url_hash = secrets.token_urlsafe(5)
            if not redis.get_url(url_hash):
                redis.set_url(url_hash, url)
                return url_hash

    def get_url(short_url):
        prefix_regex = re.compile(f"(https?://)?{config.TNY_HOSTNAME}/+",re.I)
        url_hash = prefix_regex.sub('', short_url)
        return redis.get_url(url_hash)

    # print('importing api routes')
    # from . import routes
    # ..did not work, trying inline
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
            'short_url': f"http://{config.TNY_HOSTNAME}/{url_hash}"
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

    print('returning api')
    return api
