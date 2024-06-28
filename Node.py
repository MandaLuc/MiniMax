from Position import Position
import pygame
class Node:
    def __init__(self,id,position,isOccupied):
        self.id=id
        self.position=position
        self.isOccupied=isOccupied

    def setId(self,id):
        self.id=id
    def getId(self):
        return self.id
    
    def setPosition(self,position):
        self.position=position
    def getPosition(self):
        return self.position
    
    def setVoisins(self,noeuds_voisin):
        self.noeuds_voisin=noeuds_voisin
    def getVoisins(self):
        return self.noeuds_voisin
    
    def setOccupied(self,isOccupied):
        self.isOccupied=isOccupied
    def getOccupied(self):
        return self.isOccupied

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.position.getX() * 30, self.position.getY() * 30, 30, 30))
        font = pygame.font.Font(None, 20)
        text_surface = font.render(str(self.getId()), True, (0,0,0))
        text_rect = text_surface.get_rect(center=((self.position.getX() + 0.5) * 30, (self.position.getY() + 0.5) * 30))
        screen.blit(text_surface, text_rect)