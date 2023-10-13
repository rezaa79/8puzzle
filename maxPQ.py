#reza mehdipour

#     0   1   2   3   4   5   6   7   8   9
#   null  T   S   R   P   N   O   A   E   I
#
#                           1 | T
#                         /       \                  This arragement allows us 
#                        /         \                 find the parent of each leaf 
#                   2 | S           3 | R            using integer division
#                  /     \         /     \           for example  6//2 = 3 , 7//2 = 3,  
#                 /       \       /       \          the entries 6 and 7 have 3 as its paren 
#            4 | P    5 | N      6 | O     7 | A
#          /       \
#         /         \
#    8 | E          9 | I
#        
#        A heap-ordered complete binary three


class MaxPQ(object):
    def __init__(self):
        self.pq = [0]
        self.N = 0
    
    def delMax(self):
        if(self.N == 0): raise Exception("Underflow")      
        max_el = self.pq[1]       
        try:self.pq[1] = self.pq.pop()
        except: pass
        self.N -= 1       
        self.__sink(1)     
        return max_el
    def max(self):
        return self.pq[self.N]
    def insert(self,x):
        self.N += 1
        self.pq.append(x)
        self.__swim(self.N)
    def size(self):
        return self.N    
    def __sink(self,k):
        N = self.N
        while(2*k <= N): 
            j = 2*k
            if(j < N and self.__less(j,j+1)): j += 1            
            if(not self.__less(k,j)): break
            self.__exch(j,k)
            k = 2*k

    def __swim(self, k):
        while(k>1 and self.__less(k//2,k)): 
            self.__exch(k//2,k)
            k = k//2

    def __less(self, i, j):
        return self.pq[i] <= self.pq[j]

    def __exch(self, i, j):
        temp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = temp
        

pq = MaxPQ()

pq.insert(2)
pq.insert(20)
pq.insert(200)
pq.insert(100)
pq.insert(245)
pq.insert(1)
print(pq.delMax())
print(pq.delMax())
print(pq.delMax())
print(pq.delMax())
print(pq.delMax())
print(pq.delMax())
