Show API
========

A simple API to store shows and venues.

Requirements
------------

If you are first setting up, run:

```bash
$ mkvirtualenv show_api
$ pip install -r requirements.txt
$ cd shows
$ npm install
$ cd ../
```

If returning and updating requirements, run:

```bash
$ workon show_api
$ pip install -r requirements.txt
$ cd shows
$ npm install
$ cd ../
```

Running the server
------------------

```
$ workon show_api
$ ./manage.py runserver
```

Running the page
----------------
```
$ workon show_api
$ cd shows
$ npm start
```