import pygame
from Node import Node
from Police import Police
from Position import Position
from Thief import Thief
from Plateau import Plateau

GRID_WIDTH = 21
GRID_HEIGHT = 21
CELL_SIZE = 30
grid_data = [
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    ]
def setAllNodes():
    i=1
    allnodes=[]
    for y, row in enumerate(grid_data):
        for x, cell in enumerate(row):
            if cell==1:
                allnodes.append(Node(i,Position(x,y),False))
                i=i+1
    return allnodes

allnodes=setAllNodes()

n1=allnodes[0]
n2=allnodes[1]
n3=allnodes[2]
n4=allnodes[3]
n5=allnodes[4]
n6=allnodes[5]
n7=allnodes[6]
n8=allnodes[7]
n9=allnodes[8]
n10=allnodes[9]
n11=allnodes[10]
n12=allnodes[11]
n13=allnodes[12]
n14=allnodes[13]
n15=allnodes[14]
n16=allnodes[15]
n17=allnodes[16]
n18=allnodes[17]
n19=allnodes[18]
n20=allnodes[19]
n21=allnodes[20]
n1.setVoisins([n2,n4,n5])
n2.setVoisins([n1,n3,n4])
n3.setVoisins([n2,n4,n7])
n4.setVoisins([n1,n2,n3,n6])
n5.setVoisins([n1, n8, n9])
n6.setVoisins([n4,n10,n11,n12])
n7.setVoisins([n3,n13,n14])
n8.setVoisins([n5,n9,n15])
n9.setVoisins([n5,n8,n15,n10])   
n10.setVoisins([n9,n6,n11,n16])
n11.setVoisins([n6,n10,n12,n16])
n12.setVoisins([n6,n13,n11,n16])
n13.setVoisins([n7,n12,n14,n17])
n14.setVoisins([n7,n13,n17])
n15.setVoisins([n8,n9,n19])
n16.setVoisins([n10,n11,n12,n18])
n17.setVoisins([n13,n14,n21])
n18.setVoisins([n16,n19,n20,n21])
n19.setVoisins([n15,n18,n20])
n20.setVoisins([n18,n19,n21])
n21.setVoisins([n17,n18,n20])
cop1=Police(n6)
cop2=Police(n10)
cop3=Police(n12)
thief=Thief(n11)

plateau=Plateau(thief,allnodes,[cop1,cop2,cop3],False)
plateau.catch()

