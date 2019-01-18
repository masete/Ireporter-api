# Ireporter-api
non persistent

# Badges

<<<<<<< HEAD
[![Build Status](https://travis-ci.org/masete/Ireporter-api.svg?branch=develop)](https://travis-ci.org/masete/Ireporter-api)  [![Maintainability](https://api.codeclimate.com/v1/badges/145fb1609a0dd36ba71a/maintainability)](https://codeclimate.com/github/masete/Ireporter-api/maintainability)   [![Coverage Status](https://coveralls.io/repos/github/masete/Ireporter-api/badge.svg?branch=feature)](https://coveralls.io/github/masete/Ireporter-api?branch=feature)
=======
[![Build Status](https://travis-ci.org/masete/Ireporter-api.svg?branch=develop)](https://travis-ci.org/masete/Ireporter-api) [![Maintainability](https://api.codeclimate.com/v1/badges/145fb1609a0dd36ba71a/maintainability)](https://codeclimate.com/github/masete/Ireporter-api/maintainability)   [![Coverage Status](https://coveralls.io/repos/github/masete/Ireporter-api/badge.svg?branch=feature)](https://coveralls.io/github/masete/Ireporter-api?branch=feature)
>>>>>>> 698ff605117103f58a3cab352b0d871fec4b6f02



## API Endpoints

| REQUEST | ROUTE | FUNCTIONALITY |
| ------- | ----- | ------------- |
| GET | /api/v1/redflag |Fetch all redflags|
| GET | api/v1/redflags/&lt;red_flag_id&gt; | Fetch a specific redflag |
| POST | /api/redflag/| Create a redflag|
| PUT | /api/v1/redflag_location | Edit redflag location |
| DELETE | /api/v1/redflag | Deletes a redflag |
| PUT | /api/v1/redflag_comment | Edit redflag comment |


**Getting started with the app**

**Modules and tools used to build the endpoints**

* [Python 3.6](https://docs.python.org/3/)

* [Flask](http://flask.pocoo.org/)


## Installation

Create a new directory and initialize git in it. Clone this repository by running
```sh
$ git clone URL   which in this case is https://github.com/masete/ireporter-api.git
```
Create a virtual environment. For example, with virtualenv, create a virtual environment named venv using
```sh
$ virtualenv venv
```
Activate the virtual environment
```sh
$ cd venv/scripts/activate
```
Install the dependencies in the requirements.txt file using pip
```sh

$ pip install -r requirements.txt
```
Populate the requirements.txt using

$ pip freeze  >  requirements.txt
```sh
Start the application by running
```
$ python run.py
```sh

 
The APP is hosted on heroku, checkout this Link: https://ireporter-a.herokuapp.com/

## Author
Masete Nicholas @masete


Hope you had a nice ride

