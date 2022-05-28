#Implementation of the priority queue ADT, implemented as a max heap

from typing import List
from graphviz import Digraph
import imageio.v2 as imageio
import os
import glob

class Node:
    
    def __init__(self, priority: int, value):
        self.priority = priority
        self.value = value
    
    def __str__(self):
        return f"({self.priority}, {self.value})"

class MaxHeap:

    def __init__(self, base: List):
        self.heap  = base.copy()

    #Crates a visual representation of a the current heap and saves it in out/
    def display_heap(self, filename="max heap", dir="out", frame=1):
        gra = Digraph(filename)
        edges = []
        for i in range(len(self.heap)):
            gra.node(chr(i+95), str(self.heap[i].priority))

            if((2*i + 1) <(len(self.heap))):
                gra.node(chr((2*i + 1)+95), str(self.heap[(2*i + 1)]))
                edges.append(f"{chr(i+95)}{chr((2*i + 1)+95)}")
            
            if((2*i + 2) <(len(self.heap))):
                gra.node(chr((2*i + 2)+95), str(self.heap[(2*i + 2)]))
                edges.append(f"{chr(i+95)}{chr((2*i + 2)+95)}")

        gra.edges(edges)
        gra.attr(label=f"{frame}")

        gra.format = 'png'
        gra.render(directory=dir).replace('\\', '/')

    #animates the images in tmp/
    def animate(self, frames: int, name:str):
        files = [f"tmp/{i}.gv.png" for i in range(1,frames+1)]
        images = []
        for filename in files:
            images.append(imageio.imread(filename))
        imageio.mimsave(f'out/{name}.gif', images, fps=1)

        files = glob.glob('tmp/*')
        for f in files:
            os.remove(f)

    #Returns the the node with the highest priority
    def heapMaximum(self):
        return self.heap[0]
    
    #Change priority of node at <i> to <k>, (k>=i) 
    def heapIncreaseKey(self, i: int, k: int):
        x = 1

        self.display_heap(str(x),"tmp", x)
        self.heap[i].priority = k
    
        x += 1
        self.display_heap(str(x),"tmp", x)

        x = self._bubble_up(i, x)
            
        self.animate(x, "increase_key")


    def _bubble_up(self, i: int, x=0) -> int:
        while i > 0:
            if(self.heap[i].priority > self.heap[(i-1)//2].priority):
                print(i)
                self.heap[i].priority,self.heap[(i-1)//2].priority = self.heap[(i-1)//2].priority,self.heap[i].priority
                i = (i-1)//2
                
                if(x != 0):
                    x += 1
                    self.display_heap(str(x),"tmp", x)
            
            else:
                break
        
        return x

    def _bubble_down(self, i: int):
        pass

    def __str__(self):
        return str([str(e) for e in self.heap])

nums = [65,45,23,39,31,12,13,26,21]
lst = [Node(i,chr(i+65)) for i in nums]
# lst = [Node(i,chr(i+65)) for i in range(20,0, -1)]
print([str(e) for e in lst])

x = MaxHeap(lst)
x.display_heap()
x.heapIncreaseKey(7,50)
print(x)
x.display_heap("change")
