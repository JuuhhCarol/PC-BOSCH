from typing import List
from Kernel import Kernel, init
import random as rd


def filter_function(image: List[List[int]], kernel: List[List[int]]):
    stride = (1,1)
    filtered = image[:]
    
    for i in range(len(image)):          
        for j in range(len(image[i])): 
            #filtered[i][j] = rd.randint(0,255)
            for k in range (len(kernel)):
                for l in range (len(kernel[k])):
                    filtered[i][j] += image[i][j] * kernel[k][l]

    return filtered


        

        
Kernel = Kernel("minion.png", filter_function)

init()