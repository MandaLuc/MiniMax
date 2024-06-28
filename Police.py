from Entity import Entity
import pygame

class Police(Entity):
    def __init__(self, node):
        super().__init__(node)
    
    def MiniMax (self,p,d,isMax):
        if d == 0:
            return len(p.getPlayer().getOpenWays())
        else:
            if isMax:
                initial = p.getPlayer().getNode()
                v = float("-inf")
                for way in p.getPlayer().getOpenWays():
                    p.getPlayer().moveTo(way)
                    v = max(v,self.MiniMax(p,d-1,False))
                    p.getPlayer().moveTo(initial)
                return v
            else: 
                initial = self.getNode()
                v = float("inf")
                for way in self.getOpenWays():
                    self.moveTo(way)
                    v = min(v,self.MiniMax(p,d-1,True))
                    self.moveTo(initial)
                return v

    def draw(self, screen):
        entity_color = (55, 55, 255)
        pygame.draw.circle(screen, entity_color, ((self.getNode().getPosition().getX()+0.5) * 30, (self.getNode().getPosition().getY()+0.5) * 30), 30 // 2)
