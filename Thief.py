from Entity import Entity
import pygame

class Thief(Entity):
    def __init__(self, node):
        super().__init__(node)
        self.center_counter = 0

    def draw(self, screen):
        entity_color = (255, 0, 0)
        node_size = 30  
        pygame.draw.circle(screen, entity_color, ((self.getNode().getPosition().getX()+0.5) * node_size, (self.getNode().getPosition().getY()+0.5) * node_size), node_size // 2)

    def incrementCenterCounter(self):
        self.center_counter += 1

    def getCenterCounter(self):
        return self.center_counter