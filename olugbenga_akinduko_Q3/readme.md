#  Geo Distributed LRU Cache with expiry

This project is a Naive implementation of Geo Distributed least recently used cache

## Brief description

The problem is to create a Geo distributed least recently used cache with expiry, which is meant to solve network latency issues between different application resources at Ormuco. The nature of the problem have inspired the design of this solutions architecture. 

This implementation leverage on the First in First out algorithm, and makes use of ordered dictionary , for effieciency and search performance. The cache stores events with keys, and every call to the cache returns and existing result if it exist in the cache, this will improve network calls tremendously between resources, if key is not in cache, it is added and immediately distributed across all geolocations. An ordinary dictionary was used as the storage for this as there won't be need to track order of insertion. The program allows a maximum cache size, so when the queue is full the least recently used resource will be popped out of the queue, and if the resource already exist in the queue it is moved to the start of the queue.

The solution is very simple to integrate to an existing project as it has exposed methods which will require only three lines of code in your project to get started.

Replication of data accross regions is near real time, hence making data available across all regions, 
and also up to date. The solution is resistant to network failures as it will be available at the location closest to you.

Every record has a time to live this ensures that the cache implementation is not resource intensive. This can be disabled if not needed by setting the appropriate flag on initialization.

The implementation is structured in such a way that every operation is available as a method to improve readibility and flexibility.

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
cache=lru_cache(geozones,max_size,ttl,expire)

where:
max_size: Type: integer , comment: maximum allowed queue size,required
ttl: Type: integer , comment: time in in milliseconds,required
expire: Type: Boolean, comment: determines expiry
geozones: Type List, comment: specifiy the allowed regions ,required
```

# retrieve the entire cache

```
cache.all() 
```

# check the cache by key and zone

```
cache.view(key,zone) 
```

```
where:
key: Type: Any , comment: cache key ,required
zone: Type: string , comment: Geolocation ,required
```



# update the cache

```
cache.update(key,value) 
```
```
where:
key: Type: Any , comment: cache key ,required
value: Type: Any , comment: Result from resource,required
```

# invalidate the cache to remove expired records

```
cache.expire() 
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

