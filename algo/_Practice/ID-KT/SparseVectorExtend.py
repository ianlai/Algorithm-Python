import SparseVector
import math
class SparseVectorExtend(SparseVector.SparseVector):
    def add(self, v):
        print("Add:", self, "+", v)
        if self.capacity != v.capacity:
            raise Exception("length mismatch")
        res = []
        for i in range(self.capacity):
            res.append(self.get(i) + v.get(i))
        return res

    def dot(self, v):
        print("Dot:", self, "*", v)
        if self.capacity != v.capacity:
            raise Exception("length mismatch")
        res = 0
        for i in range(self.capacity):
            res += self.get(i) * v.get(i)
        return res

    def cos(self, v):
        print("Cos:", self, ",", v)
        if self.capacity != v.capacity:
            raise Exception("length mismatch")
        return self.dot(v) / self.norm() / v.norm()        

    def norm(self):
        res = 0
        for i in range(self.capacity):
            res += self.get(i) ** 2
        return math.sqrt(res)

print("SparseVectorExtend")
v1 = SparseVectorExtend(10)
v1.set(0, 4)
v1.set(8, 14)
v1.set(2, 6)
print(v1)
print(v1.toString())

v2 = SparseVectorExtend(10)
# v2.set(2, 2)
# v2.set(5, 5)
# v2.set(4, 4)
# v2.set(3, 3)
v2.set(2, 9)
v2.set(0, 6)
v2.set(8, 1)
v2.set(8, 21)
print(v2)
print(v2.toString())

print(v1.add(v2))
print(v1.dot(v2))
print(v1.cos(v2))
