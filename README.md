# NASA APOD

A simple GET endpoint that combines NASA Astrological Photo Of the Day with wikipedia links to help explain the photo.


### Setup

Virtual Env:

`python3 -m venv project`

`source ./project/bin/activate`


Install Deps

`pip install -r requirements.txt`

Database:

`cd outside`

`./manage.py migrate`

Start Server:

`./manage.py runserver`

Tests:

`./manage.py test`