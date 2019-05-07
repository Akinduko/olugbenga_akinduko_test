from datetime import datetime,timedelta
import timeinterval

class lru_cache:

    # Constructor
    def __init__(self,max_size=2,ttl=(1000*3600),expire=True):
        self.cache = {}
        self.max_size = max_size
        self.ttl = ttl
        if expire:
            self.activate()
        
    def activate(self):
        # This will be the actual decorator,
        timeinterval.start(self.ttl,self.expire)

    def empty(self):
        # checking, whether cache is Empty
        return self.cache == {}

    def size(self):
        # Returns total size of cache
        return len(self.cache)

    def __contains__(self, key):
        # Returns Boolean value, whether key is in the cache
        return key in self.cache

    def all(self):
        return self.cache

    def view(self,key):
        # Returns cache dictionary
        cache = self.cache[key]
        if key in self.cache:
            self.shift_item(key,cache)
        if key not in self.cache:
            self.update(key,cache)
        # del cache['Added time']
        # del cache['expire_at']
        return cache

    def reposition(self,key):
        # Returns cache dictionary
        self.cache.pop(key)
        return self.cache  

    def expire(self):
        # Remove oldest item from cache
        timenow=datetime.now().timestamp()
        newcache={}
        for key in self.cache:
            if self.cache[key]['expire_at'] <= timenow:
                newcache[key]=self.cache[key]
        self.cache=newcache

    def update(self, key, value):
        #remove oldest item, when size reaches maximum
        if key not in self.cache and len(self.cache) == self.max_size:
            self.delete()
            self.cache = {
                **{
                    key:{
                        **value,
                        **{'Added time':datetime.now().isoformat()},
                        **{'expire_at': (datetime.now() + timedelta(seconds=self.ttl)).timestamp()}
                    }},
                    **self.cache}

        elif key not in self.cache:
            # Update cache if item doesn't exist in cache
            self.cache = {
                **{
                    key:{
                        **value,
                        **{'Added time':datetime.now().isoformat()},
                        **{'expire_at': (datetime.now() + timedelta(seconds=self.ttl)).timestamp()}
                    }},
                    **self.cache}
        else:
            # move item the front of queue if it exists in cache
            self.shift_item(key,value)

    def shift_item(self,key,value):
        cachevalue = { 
            **value,  
            **{ 'Added time':datetime.now().isoformat()},
            **{'expire_at': (datetime.now() + timedelta(seconds=self.ttl)).timestamp()}
            }
        oldcache=self.cache
        self.cache=  {**{key:cachevalue},**oldcache}
        self.cache[key]=cachevalue

    def delete(self):
        # Remove oldest item from cache
        old_entry = None
        for key in self.cache:
            if old_entry is None:
                old_entry = key
            elif self.cache[key]['Added time'] < self.cache[old_entry]['Added time']:
                old_entry = key
        self.cache.pop(old_entry)