class Codec:
    
    # Use counter [92%]
    def __init__(self):
        print("Code3")
        self.counter = 0 
        self.shortToLong = {}
        self.longToShort ={}
    def encode(self, longUrl: str) -> str:
        if longUrl in self.longToShort:
            return longToShort[longUrl]
        shortUrl = str(self.counter)
        self.shortToLong[shortUrl] = longUrl
        self.longToShort[longUrl] = shortUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        if shortUrl in self.shortToLong:
            return self.shortToLong[shortUrl]
        return -1
    
class Codec2:
    
    # Use hash function [92%]
    def __init__(self):
        print("Code2")
        self.shortToLong = {}
    def encode(self, longUrl: str) -> str:
        short = hash(longUrl)
        self.shortToLong[short] = longUrl
        return short
        
    def decode(self, shortUrl: str) -> str:
        return self.shortToLong[shortUrl]

#======================================================
class Codec1:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        return longUrl 
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return shortUrl
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))