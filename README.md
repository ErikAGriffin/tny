# Tny
A URL shortener.

## Installation
1. Install [Redis](https://redis.io/topics/quickstart) and ensure the server is running.
(On Mac homebrew is an easy way to install and manage the service)
2. Install python3 and pip3
3. Install [pipenv](https://pipenv.pypa.io/en/latest/install/)
```
$ pip install --user pipenv
```
4. Create '.venv' directory.  This ensures that dependencies installed with pipenv are installed in the same folder as this repository.
```
$ mkdir .venv
```
5. Install project dependencies
```
$ pipenv install
```

## Running Server
1. Activate project's virtualenv:
```
$ pipenv shell
```
2. Start server
```
$ flask run
```

## Usage and API

**To create a shortened URL:**
Send a POST request to `/api/urls` with the following request body:
```
{ "url": "http://urltobeshorten.ed" }
```
Response:
```json
{ "short_url": "http://<host>/dJ32ms" }
```
Note that the string after the `/` in the short url is case sensitive.

**To activate a shortened URL:**
Visit the short_url in the address bar of your browser.

**To retrieve the original url as a string:**
Send a GET request to `/api/urls` with the following request body:
```
{ "url": "http://<host>/dj32ms" }
```
Response:
```json
{ "original_url": "http://urltobeshorten.ed" }
```

# Brief Thoughts on the Project
I enjoyed using this project as an opportunity to become more familiar with Flask and structuring Python applications.  Given more time, I would like to read through the Flask documentation more thoroughly and get the configuration and structure of the application more refined.

In particular, once I split the application out of a single server file into blueprints, I was having trouble sharing config throughout the app in the way I thought Flask would allow me.  A way around this would be to create factory methods for the blueprint modules that I then pass the app's configuration into.

Also, I currently instantiate a Redis instance in each of the blueprints.  I would have liked to find a nice way either to have the redis connection available globally, or again use the factory method pattern to instantiate Redis when the app initializes and pass the dependency into the blueprints via the factory method.

As far as the actual service, some next steps would be to add a frontend to simplify the creation of short urls via a web interface.  Then looking into how Flask handles concurrent requests and making sure I'm utilizing available threads efficiently.

## Time Spent on Project
The first night I spent an hour or so reviewing Python, looking into the Flask documentation, and setting up my
environment and testing a Flask server.  On Saturday I spent about 2 hours building a working copy of the shortening service, and
then on Sunday I spent 1-2 hours looking up examples of more robust Flask projects and splitting the application from a
single file into a more modular and extensible structure using blueprints.
