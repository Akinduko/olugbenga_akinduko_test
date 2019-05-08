from datetime import datetime,timedelta
from collections import OrderedDict
import timeinterval

class lru_cache:

    # Constructor
    def __init__(self,zones=['zone1','zone2'],max_size=2,
    ttl=(1000*3600),expire=True):
        self.cache = OrderedDict()
        self.max_size = max_size
        self.ttl = ttl
        self.geozones={}
        self.defaultzone= zones[0]
        self.zones=zones
        self.initialize()
        if expire:
            self.setinterval()
        
    # This will expire cache at intervals,
    def setinterval(self):
        timeinterval.start(self.ttl,self.expire)

    # This distribute cache
    def distribute_cache(self):
        for each in self.zones:
            self.geozones[each]=self.cache
    
    # setup the cache
    def initialize(self):
        for each in self.zones:
            self.geozones[each]=self.cache

    # Returns total size of cache
    def size(self):
        return len(self.cache)

    # Returns all cache dictionary
    def all(self):
        return self.geozones

    def view(self,key,zone=None):
        # Returns cache dictionary
        cache = self.geozones[self.defaultzone] if zone==None else self.geozones[zone]
        if key in cache:
            self.shift_item(key,cache[key])
            return cache[key]
        else:
            self.update(key,cache[key])
            return cache[key]

    def expire(self):
        # Remove oldest item from cache
        timenow=datetime.now().timestamp()
        newcache=OrderedDict()
        for key in self.cache:
            if self.cache[key]['expire_at'] <= timenow:
                newcache[key]=self.cache[key]
        self.cache=newcache

    def update_cache(self,key,value):
        self.cache = {
            **{
                key:{
                }},
                **self.cache
                }
        self.cache[key]={
                    **value,
                    **{'expire_at': (datetime.now() + timedelta(seconds=self.ttl)).timestamp()}
                }  
        self.cache=OrderedDict(self.cache)
        #distributes the cache across all regions immediately
        self.distribute_cache()

    def update(self, key, value):
        #remove oldest record, when size reaches maximum
        if key not in self.cache and len(self.cache) == self.max_size:
            self.delete()
            self.update_cache(key, value)   
        # Update cache if record doesn't exist in cache
        elif key not in self.cache:
            self.update_cache(key, value)   
        # move record to the front of queue if it exists in cache
        else:
            self.shift_item(key,value)

    #method moves an existing record to the beginning of queue
    def shift_item(self,key,value):
        self.cache[key]={
                    **value,
                    **{'expire_at': (datetime.now() + timedelta(seconds=self.ttl)).timestamp()}
                }  
        self.cache=OrderedDict(self.cache)
        self.cache.move_to_end(key,False)
        self.distribute_cache()

    #method removes the oldest record from cache
    def delete(self):
        self.cache.popitem()