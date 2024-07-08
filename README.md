# NASA APOD

A simple GET endpoint that combines NASA Astronomy Photo Of the Day with wikipedia links to help explain the photo.


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

## Usage
Note: NASA's APOD API returns videos sometimes. You'll need to handle `media_type: 'video'` when making requests.


GET http://127.0.0.1:8000/nasa/apod?date=2024-07-01

Response:
```
{
    "date": "2024-07-01",
    "title": "Time Spiral",
    "description": "What's happened since the universe started? The time spiral shown here features a few notable highlights. At the spiral's center is the Big Bang, the place where time, as we know it, began about 13.8 billion years ago. Within a few billion years atoms formed, then stars formed from atoms, galaxies formed from stars and gas, our Sun formed, soon followed by our Earth, about 4.6 billion years ago.  Life on Earth begins about 3.8 billion years ago, followed by cells, then photosynthesis within a billion years.  About 1.7 billion years ago, multicellular life on Earth began to flourish.  Fish began to swim about 500 million years ago, and mammals began walking on land about 200 million years ago. Humans first appeared only about 6 million years ago, and made the first cities only about 10,000 years ago.  The time spiral illustrated stops there, but human spaceflight might be added, which started only 75 years ago, and useful artificial intelligence began to take hold within only the past few years.   Explore Your Universe: Random APOD Generator",
    "url": "https://apod.nasa.gov/apod/image/2407/TimeSpiral_Budassi_960.jpg",
    "media_type": "image",
    "extra_info": "{'source': 'Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Time_Spiral'}"
}