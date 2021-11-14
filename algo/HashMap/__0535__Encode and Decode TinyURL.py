class Codec:
    
    # Use hash function [92%]
    def __init__(self):
        self.shortToLong = {}
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        short = hash(longUrl)
        self.shortToLong[short] = longUrl
        return short
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
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