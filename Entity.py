import pygame
from abc import ABC, abstractmethod
class Entity:
    def __init__(self,node):
        self.node = node
    
    def setNode(self,node):
        if not node.getOccupied():
            cur_node=self.getNode()
            cur_node.setOccupied(False)
            node.setOccupied(True)
            self.node=node

    def getNode(self):
        return self.node 
     
    def moveTo(self,node):
        self.setNode(node)
    
    def getOpenWays(self):
        nodesOpen=[]
        openNode=self.getNode().getVoisins()
        for node in openNode:
            if node.getOccupied()==False:
                nodesOpen.append(node)
        return nodesOpen
    
    @abstractmethod
    def draw(self, screen):
        pass