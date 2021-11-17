import collections

def even_items(iterable):
    return [v for i, v in enumerate(iterable, start=1) if not i % 2]


def displayMatrix( mat, N ):
     
    for i in range(0, N):
         
        for j in range(0, N):
             
            print (mat[i][j], end = ' ')
        print ("")


def myAtoi(s):
    s = s.strip()
    for i, value in enumerate(s):
        if not value.isnumeric():
            if i == 0 and value != "-":
                return 0
            elif i > 0:
                s = s[:i]
    s = int(s)
    if s > (2**31 - 1):
        return 2**31-1
    elif s < -2**31:
        return -2**31
    else:
        return s 

def myAtoi2(s):
    s = s.lstrip()           # case 1, remove ONLY leading white space
    num = "0"
    neg = 1
    print(s)
    for i in range(len(s)): 
        print(i)
        if s[i] == "+" and i == 0:
            neg = 1
        elif s[i] == "-" and i == 0:
            neg = -1
        elif not s[i].isnumeric():
            break
        else:
            num = num + s[i]
    num = int(num) * neg
    if num > (2**31 - 1):
        return 2**31-1
    elif num < -2**31:
        return -2**31
    else:
        return num 


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        print(n)
        if n == 1:
            print("DONE")
            return "1"
        return self.count(self.countAndSay(n - 1))
        
    def count(self , s):
        return s + s


def yield_test():
    for i in "test":
        yield i


if __name__ == '__main__':
    
    test = [1,2,3]
    print(test.index(0))

    #k = Solution()
    #print(k.countAndSay(3))

    """
    favorites = {"pet": "dog", "color": "blue", "language": "Python"}
    favorites.get("fruit", "apple")
    print(favorites)
    print(favorites.get("sdfo") is None)
    """
    #matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    #print(len(matrix))
    #len_val = len(matrix)
    #displayMatrix(matrix, len_val)    
    #len_val = len(matrix)
    
    """
    for i in range(0, len_val//2):
        for j in range(i, len_val-1):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[i][len_val-j-1]
            matrix[i][len_val-j-1] = matrix[len_val-i-1][len_val-j-1]
            matrix[len_val-i-1][len_val-j-1] = matrix[len_val-i-1][j]
            matrix[len_val-i-1][j] = tmp
            displayMatrix(matrix, len_val)
    """


#print(int(5.325235))
#print(int(0+-+-4))

