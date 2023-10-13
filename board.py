import random
#  @author REZA MEHDIPOUR
#******************************************************************************/

class Board(object):
    # Constructor
    def __init__(self,blocks):
        self.n = len(blocks)
        self.board = []        
        self.Manhattan = 0
        self.chakosh = 0
        for i in range(self.n):
            for j in range(self.n):
                enter = blocks[i][j]
                self.board.append(enter) 
                if (enter!=0):
                    self.Manhattan += abs(i-(enter-1)//self.n) + abs(j-((enter-1)%self.n))
                    if (enter != self.n*i + j + 1): self.chakosh+=1

    
    def dimension(self):
        '''Size of the board game'''
        return self.n

    def manhattan(self):
        '''Manhattan distance'''
        return self.Manhattan
    def chakosh(self):
        '''chakosh distance'''
        return self.chakosh

    def inversions(self):
        pass
    def is_goal(self):
        '''Determine when a given board is the goal board'''
        for i in range(0,self.n*self.n - 1):
            if(self.board[i] != i+1): return False
        return True

    def __get_board(self):
        return self.board
    
    def __swap(self,Idx,nIdx):
        '''Swap one valid place the blank tile'''
        neighbour = [[self.board[i*self.n + j] for j in range(self.n)] for i in range(self.n)]
        i, j =  Idx // self.n , Idx % self.n
        l, m = nIdx // self.n,  nIdx % self.n
        temp = self.board[nIdx]
        neighbour[i][j] = temp
        neighbour[l][m] = 0
        return neighbour

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False
        # if(self == other): return True
        # if(other == None): return False
        # if(not isinstance(other, Board)): return False
        # other_board = other.__get_board()
        # for i in range(self.n*self.n):
        #     if(self.board[i] != other_board[i]): return False
        # return True

    # Iterate through the possibles bottom, up, left and right blank tiles moves (we called them neighbors)
    def neighbors(self):
        '''Return the neighbors of a given board'''
        #search where the blank space is placed
        idx = self.board.index(0)
        #create a neighboard list
        L = []
        if(idx // self.n != 0):                                 L.append(Board(self.__swap(idx, idx - self.n)))  #up neighbour
        if((idx + 1)//self.n == idx//self.n):                   L.append(Board(self.__swap(idx, idx + 1 )))      #right neighbour
        if(idx + self.n < self.n**2):                           L.append(Board(self.__swap(idx, idx + self.n)))  #botton neighopur
        if((idx - 1)//self.n == idx//self.n and idx - 1 >= 0):  L.append(Board(self.__swap(idx, idx - 1)))       #left neighbour

        while(len(L) != 0):   
            yield L.pop()

    def __str__(self):
        s = "\n".join('  '.join([str(self.board[i*self.n + j]) for j in range(self.n)]) for i in range(self.n))
        return s + "\n"
# n = 3
# a = list(random.sample(range(n*n),n*n))

# blocks1 = [[a[n*i+j] for j in range(n)] for i in range(n) ]

# blocks2 = [[a[n*i+j] for j in range(n)] for i in range(n) ]
# temp = blocks2[1][2] 
# blocks2[1][2] = blocks2[2][1]
# blocks2[2][1] = temp
# s = "\n".join(' '.join([str(blocks[i][j]) for j in range(3)]) for i in range(3))

# n = 4
# a = list(random.sample(range(n*n),n*n))

# blocks1 = [[a[n*i+j] for j in range(n)] for i in range(n) ]

# blocks2 = [[a[n*i+j] for j in range(n)] for i in range(n) ]
# temp = blocks2[1][2] 
# blocks2[1][2] = blocks2[2][1]
# blocks2[2][1] = temp
# s = "\n".join(' '.join([str(blocks[i][j]) for j in range(4)]) for i in range(4))


# board1 = Board(blocks1)
# board2 = Board(blocks2)
# print(board1)
# print()
# print(board2)
# print()
# print(board1 == board2)
# print()
# print(board1.is_goal())
# print()
# print(board1.is_goal())
# print()
# for neighbour in board1.neighbors():
#     print(neighbour)
#     print('Manhattan distannce: ' + str(neighbour.manhattan()))
#     print('chakosh distance: ' + str(neighbour.chakosh()))
#     print()
















