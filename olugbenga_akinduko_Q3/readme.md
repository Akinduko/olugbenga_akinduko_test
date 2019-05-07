#  Geo Distributed LRU Cache

This project is a Naive implementation of Geo Distributed least recently used cache 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. The cache program is available at olugbenga_akinduko_Q3.py, with methods exposed for ease of integration. To demo the integration a flask app was implemented in main.py to test the cache.


## Features

```
1. Cache size is dynamic and can be set by user
2. least recently used item is removed when cache is full.
3. An Item is moved to the begining of the queue if it exist in queue and its revisited
4. Cache is invalidated after a set time determined by the user, its 1 hr by default.
```

## Dependencies

```
flask
flask_restful
timeinterval
```

## Integration

```

# place olugbenga_akinduko_Q3.py in your project

# install dependencies

```
pip3 install -r requirements.txt
``` 

# Import the library into your project

```
from olugbenga_akinduko_Q3 import lru_cache
```

# initialize the cache

```
cache=lru_cache(max_size,ttl,expire)

where:
max_size: Type: integer , comment: maximum allowed queue size
ttl: Type: integer , comment: time in in milliseconds
expire: Type: Boolean, comment: determines expiry
```

# retrieve the cache

```
cache.all() 
```

# update the cache

```
cache.update(key,value) 
```

# invalidate the cache

```
cache.expire(key,value) 
```

```


### Demo

Install dependencies using requirements file

```
pip3 install -r requirements.txt
``` 

## Deployment

Start app (Make sure to enter a valid website to an existing website)

```
python3 main.py
``` 

Example of valid queries

```
http://127.0.0.1:5000/cache/cache : to retrieve the cache dictionary

Valid routes
http://127.0.0.1:5000/cache/Elvin
http://127.0.0.1:5000/cache/Nicholas
http://127.0.0.1:5000/cache/Jass
```


### Missing functionalities

- Missing functionalities : Geo distributed methods and functions 
