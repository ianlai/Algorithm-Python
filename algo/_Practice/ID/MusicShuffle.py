# artist | album | title | track #
# -------+-------+-------+--------
#   A    | "1st" | X     | 1         #0
#   A    | "1st" | W     | 2         #1
#   B    | "1st" | Y     | 6         #2
#   B    | "4th" | Z     | 3         #3


# [∞] shuffle
# WXYZ
# XWYZ
# It's possible to have 4! = 24 different orders

# out of album: shuffle 
# in album: based on track number
# track number: 1~20 


# [A∞] Album shuffle
# (WX)(Y)(Z)
# (Y)(WX)(Z)
# (Z)(WX)(Y)


# With Python 3 type hinting
from typing import List
import collections
class Song:
    def __init__(self, artist: str, album: str, title: str, track: int) -> None:
        self.artist = artist
        self.album = album
        self.title = title
        self.track = track
def album_shuffle(songs: List[Song]) -> List[Song]:
    # do album shuffle
    albumToTracks = collections.defaultdict(list)
    '''
    {
        "A", "1st" -> [0,1] #sorted by track   #0
        "2nd" -> [2]  #1
        "4th" -> [3]  #2
    }    
    '''
    # TC = O(N) //depends on randInt
    # SC = 
    def getRandom(arr):  #[2,0,1]
        res = []
        used = set()
        
        rand(n) -> 
        for _ in range(len(arr)):
            while idx in used:
                idx = random.randInt(0, len(arr))  #0, 1, 2 
                continue
            used.add(idx)
            res.append(idx)
        return res
    # O(N)
    for idx, song in enumerate(songs):
        albumToTracks[(song.author, song.album)].append(idx)
        
    randIdxList = getRandom()  #[2,0,1]
    
    res = []  #res=[3,0,1,2]
    #O(N* MlogM) M is up to 20  
    for idx in randIdxList:  #idx = 0
        originalIdxArray = sorted(list(albumToTracks.keys())[idx])   # [0,1] 
        for j in originalIdxArray: #3
            res.append(songs[j])       [#[1st, 2nd, 4th]
    return res 
'''
{
    "1st" -> [0,1] #sorted by track   #0
    "2nd" -> [2,4]  #1
    "4th" -> [3]  #2
}    
''' 
1.
Input:  [s0, s1, s2, s3, s4]
Output: [(s2, s4), s3, (s0, s1)] [(s2, s4) (s0, s1), s3] 
Goal:   


'''
{
    "1st" -> [1] 
    "2nd" -> [2] 
    "4th" -> [0]  
}    
'''
