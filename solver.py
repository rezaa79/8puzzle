import minPQ
from board import Board 
import random
from heapq import heappop, heappush
from pathlib import Path

#  You can build your own board of size n x n using the following example:
#  
#  3
#  9  7  3
#  4  5  6
#  1  2  0

class Solver(object):
    def __init__(self, boardGame):
        self.board = boardGame
        self.moves = 0             
        self.solutions = []        
        self.__solve()              
                                   
    def __solve(self): 
        state = 0
        search_node =  self.SearchNode(self.board,state,None)  
        seeker_node = self.aStar(search_node)                  
       
        pq = []                  
        heappush(pq,seeker_node)  
        i = 0
        while(True): 
           
            seeker_node = heappop(pq)    
            search_node = seeker_node.get_Search_Node()
            old_search_node = search_node        
            state = old_search_node.state + 1   
            
            if(search_node.link == None): predecessor = None   
            else: predecessor = search_node.link.current      
                
            for neighbour in search_node.current.neighbors():
                if(not (neighbour == predecessor)):  
                    
                    search_node = self.SearchNode(neighbour,state,old_search_node)
                    branch = self.aStar(search_node)
                    heappush(pq,branch)  
            i += 1
            if(old_search_node.current.is_goal()): break

        self.moves = state      
        search_node = search_node.link 
        while(search_node != None):          
            self.solutions.append(search_node.current)
            search_node = search_node.link

         
    def isSolvable(self):
        pass

    def __iter__(self):
        while(len(self.solutions) > 0):
            yield self.solutions.pop()

    def number_of_moves(self):
        return self.moves - 1

    class SearchNode(object):
        def __init__(self, current, state, link):
            self.current = current
            self.state = state
            self.link = link
    class aStar(object):
        def __init__(self, searchNode):
            self.sn = searchNode
            self.heuristic_distance = searchNode.current.manhattan()
            self.state = searchNode.state
            self.cost_function = self.heuristic_distance + searchNode.state

        def get_Search_Node(self):
            return self.sn
        
        def get_priority(self):
            return self.cost_function

        def __lt__(self, other):
            return (self.cost_function, self.heuristic_distance) < (other.cost_function, other.heuristic_distance)

        def __eq__(self, other):
            return self.cost_function == other.cost_function 
data_folder = Path("source_data/")
file_to_open = data_folder / "puzzle04.txt"
f = open(file_to_open)
n = int(f.readline())
blocks = [[ int(el) for el in line.split()] for line in f ]

board = Board(blocks)
solver = Solver(board)
print("# of move to solve the board: "+  str(solver.number_of_moves()))
for solutions in solver:
    print(solutions)