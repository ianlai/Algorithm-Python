class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a 
        a = a[::-1]
        b = b[::-1]
        carry = 0
        res = []
        for i in range(len(a)):
            if i < len(b):
                s = int(a[i]) + int(b[i]) + carry 
            else:
                s = int(a[i]) + carry 

            sum_digit = 1 if s % 2 == 1 else 0 
            carry = 1 if s >= 2 else 0
            res.append(str(sum_digit))
            # if s == 3:
            #     carry = 1
            #     res.append('1')
            # elif s == 2:
            #     carry = 1
            #     res.append('0')
            # elif s == 1:
            #     carry = 0
            #     res.append('1')
            # else:
            #     carry = 0
            #     res.append('0')
        if carry == 1:
            res.append('1')
        return ''.join(res[::-1])
