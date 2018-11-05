# Flask boilerplate code

![License](http://img.shields.io/:license-mit-blue.svg)

flask + nginx boilerplate. Mainly refer to MaxHalford/flask-boilerplate(https://github.com/MaxHalford/flask-boilerplate)

## Features

- [x] Python 3.x compliant.
- [x] Virtual environment example.
- [ ] Tests.
- [x] Logging.
- [ ] Configs compliant with Makefile

## Libraries

### Backend
- [Flask](http://flask.pocoo.org/), obviously.
- [structlog](http://structlog.readthedocs.io/en/stable/) for logging.
- [Flask-DebugToolBar](https://flask-debugtoolbar.readthedocs.io/en/latest/) for adding a performance toolbar in development.
- [gunicorn](http://gunicorn.org/) for acting as a reverse-proxy for Nginx.

## Structure

I did what most people recommend for the application's structure. Basically, everything is contained in the `app/` folder.

- There you have the classic `static/` and `templates/` folders. The `templates/` folder contains macros, error views and a common layout.
- I added a `views/` folder to separate the user and the website logic, which could be extended to the the admin views.
- I added a Makefile for setup tasks, it can be quite useful once a project grows.

## Setup

### Vanilla

- Install the requirements and setup the development environment.

	`make install && make dev`

- Run the application.

    ```sh
    docker-compose build
    docker-compose up -d
    ```
