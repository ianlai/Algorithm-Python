class Encrypter:

    # 2022/04/03 Contest
    # Generate the encryptCount in the first place [56%]
    
    # O(dictionary size)
    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.keys = keys
        self.values = values 
        self.encryptCount = collections.defaultdict(int)
        for ori in dictionary:
            self.encryptCount[self.encrypt(ori)] += 1

    # O(input word length)
    def encrypt(self, word1: str) -> str:
        res = ""
        for ch in word1:
            idx = self.keys.index(ch)
            res += self.values[idx]
        return res

    # O(1)
    def decrypt(self, word2: str) -> int:
        return self.encryptCount[word2]


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)