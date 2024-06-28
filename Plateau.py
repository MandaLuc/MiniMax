from Node import Node
from Police import Police
from Thief import Thief
from Entity import Entity
from Position import Position
import pygame
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
class Plateau:                    
    def __init__(self,player,nodes,cops,cops_turn=False):
        self.nodes=nodes
        self.player=player
        self.cops=cops
        self.cops_turn=cops_turn
        pygame.init()
        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.play(-1)
       
     

    def setCopsTurn(self,cops_turn):
        self.cops_turn=cops_turn

    def getCopsTurn(self):
        return self.cops_turn

    def setPlayer(self,player):
        self.player=player
    
    def getPlayer(self):
        return self.player
    
    def setCops(self,cops):
        self.cops=cops

    def getCops(self):
        return self.cops

    def setNodes(self,nodes):
        self.nodes=nodes

    def getNodes(self):
        return self.nodes    
    
    def bestMove(self):
        b_cop = None
        b_node = None
        minScore = float("inf")
        for cop in self.getCops():
            initial_node = cop.getNode()
            for node in cop.getOpenWays():
                cop.moveTo(node)
                score = cop.MiniMax(self, 10, True)  
                cop.moveTo(initial_node)
                if score < minScore:
                    minScore = score
                    b_cop = cop
                    b_node = node        
        b_cop.moveTo(b_node)
        self.setCopsTurn(False)
    
    def draw(self, screen):
        for y, row in enumerate(grid_data):
            for x, cell in enumerate(row):
                color = (0, 100, 255)  
                pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def drawAll(self,screen):
        self.draw(screen)
        for node in self.getNodes():
            node.draw(screen)
        for cop in self.getCops():
            cop.draw(screen)         
        self.getPlayer().draw(screen)
    
    def moveToNode(self, x, y):
        for node in self.getPlayer().getOpenWays():
            node_position = node.getPosition()
            node_x = node_position.getX()
            node_y = node_position.getY()
            node_width = 30 
            node_height = 30  
            left_boundary = node_x * 30
            right_boundary = (node_x ) * 30+node_width
            top_boundary = node_y * 30
            bottom_boundary = (node_y ) * 30+node_height
            if left_boundary <= x < right_boundary and top_boundary <= y < bottom_boundary:
                print("left"+" "+str(left_boundary))
                return node
        return None

    def catch(self):
        screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
        running = True
        count=0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    print(mouse_x)
                    print(mouse_y)
                    clicked_node = self.moveToNode(mouse_x, mouse_y)
                    if clicked_node and not self.getCopsTurn():
                        print("Clicked on Node:", clicked_node.getId())
                        self.getPlayer().moveTo(clicked_node)
                        self.setCopsTurn(True)
                        self.bestMove()
                        count=count+1                
            screen.fill((0,0,0))
            self.updateNode()
            self.drawAll(screen)
            pygame.display.flip()
            if self.check_game_over() or count==50:
                self.resetGame()
                count=0

        pygame.quit()
    def check_game_over(self):
        if len(self.getPlayer().getOpenWays()) == 0:
            print("No more moves for the thief. Police wins!")
            return True

        return False

    def updateNode(self):
        for node in self.getNodes():
            node.setOccupied(False)
            for cop in self.getCops():
                if cop.getNode() == node:
                    node.setOccupied(True)
                    break
            if self.getPlayer().getNode() == node:
                node.setOccupied(True)

    def resetGame(self):
        self.getPlayer().moveTo(self.getNodes()[10])
        self.getCops()[0].moveTo(self.getNodes()[5])
        self.getCops()[1].moveTo(self.getNodes()[9])
        self.getCops()[2].moveTo(self.getNodes()[11])
