import pygame
import random

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
yellow   = ( 255,   255, 0)
purple   = ( 255,   0, 255)


class caterpillar:
    def __init__(self,screen):
        self.screen=screen
        self.moulted=False
        x = random.randrange(0,1000)
        self.face_xcoord = x
        self.face_ycoord = 250
        self.body = segment_queue()
        self.food = food_list()
        t = random.randrange(0,2)
        self.consumption=0
        if t == 0:
            self.travel_direction = 'left'
        else:
            self.travel_direction = 'right'
        
    def draw_caterpillar(self, screen):

        self.draw_body(screen)
        self.draw_food(screen)
        self.draw_face(screen)

    def draw_face(self, screen):
        x = self.face_xcoord 
        y = self.face_ycoord
        pygame.draw.ellipse(screen,red,[x, y, 40, 45])
        pygame.draw.ellipse(screen,black,[x+6, y+10, 10, 15])
        pygame.draw.ellipse(screen, black, [x + 24, y + 10, 10, 15])
        pygame.draw.ellipse(screen, black, [x + 13, y + 30, 15, 10])
        pygame.draw.line(screen,black, (x+11, y), (x+9, y-10), 3)
        pygame.draw.line(screen,black, (x+24, y), (x+26, y-10), 3)
        
    def draw_body(self, screen):
        #traverse the segment queue
        current_node = self.body.head
        while current_node is not None:
            if(self.consumption<30):
                current_node.draw_segment(screen,self.consumption >= 15)

            elif(self.consumption>=30):
                self.moult(current_node)

            current_node = current_node.next 
           
    def draw_food(self, screen):
        #traverse the segment queue
        current_node = self.food.head
        while current_node is not None:
            current_node.draw_fooditem(screen) 
            current_node = current_node.next
           
    def grow(self):
        if(self.body.length==0):
            if(self.travel_direction== 'left'):
                self.body.addSegment(self.face_xcoord+ 30,self.face_ycoord)
            elif(self.travel_direction=='right'):
                self.body.addSegment(self.face_xcoord -  30, self.face_ycoord)
        else:
            if (self.travel_direction == 'left'):
                self.body.addSegment(self.body.head.xcoord + 30, self.face_ycoord)
            elif (self.travel_direction == 'right'):
                self.body.addSegment(self.body.head.xcoord - 30, self.face_ycoord)
        print(self.body.length)

        return


    def move_forward(self):
        if(not(self.body.isEmpty())):
            if (self.travel_direction == 'left'):
                self.body.moveall(-2)
                self.face_xcoord+=-2
                if(self.face_xcoord<0):
                    self.reverse()
            elif (self.travel_direction == 'right'):
                self.body.moveall(2)
                self.face_xcoord += 2
                if(self.face_xcoord>960):
                    self.reverse()

        # traverse the segment queue
        current_node = self.food.head
        temp=self.food.head
        while current_node is not None:
            #if(self.travel_direction=='left'):
            if((current_node.xcoord - self.face_xcoord<5 and current_node.xcoord - self.face_xcoord>-5 and self.travel_direction=='left')or(current_node.xcoord - (self.face_xcoord+40) < 5 and current_node.xcoord - (self.face_xcoord+40) > -5 and self.travel_direction=='right')):


                self.consumption += 1
                print(self.consumption)
                if(self.consumption>=30):
                    self.moulted=True
                #print(self.consumption)
                self.food.length -= 1
                if(current_node==self.food.head):
                    self.food.head=current_node.next
                else:
                    temp.net = current_node.next

            temp=current_node
            current_node = current_node.next




    def reverse(self):
        # print(self.body.head.xcoord)
        if (self.travel_direction == 'left'):
            self.travel_direction = 'right'
            self.face_xcoord = self.body.head.xcoord + 30
        elif (self.travel_direction == 'right'):
            self.travel_direction = 'left'
            self.face_xcoord = self.body.head.xcoord-40
        self.body.reverse()
    

                
    def drop_food(self):
        self.food.addfood()
        return
        
    def moult(self,node):
        node.drawmoult(self.screen)
        return
    
class segment_queue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None
      
    def isEmpty(self):
        return self.length == 0
      
    def addSegment(self, x, y):
        node = body_segment(x,y)
        self.length+=1;
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        return


    def moveall(self,dif):
        current_node = self.head
        while current_node is not None:

            current_node.xcoord+=dif;
            current_node = current_node.next


    def reverse(self):

        end = None

        node = self.head
        while node != None:
            temp = node.next
            node.next = end
            end = node
            node = temp

        self.last = self.head
        self.head = end





class body_segment:
    def __init__(self, x, y):
        self.xcoord = x
        self.ycoord = y
        self.next = None
        
    def draw_segment(self, screen,bloom):
        x = self.xcoord
        y = self.ycoord
        if(not(bloom)):
            pygame.draw.ellipse(screen,green,(x, y, 35, 40))

        else:
            pygame.draw.ellipse(screen, yellow, (x, y, 35, 40))
        pygame.draw.line(screen, black, (x + 8, y + 35), (x + 8, y + 45), 3)
        pygame.draw.line(screen, black, (x + 24, y + 35), (x + 24, y + 45), 3)
        #print("draw_segment")

    def drawmoult(self,screen):
        x = self.xcoord
        y = self.ycoord
        pygame.draw.ellipse(screen, black, (x, y, 45, 45))
        pygame.draw.line(screen, black, (x+8 , y + 35), (x + 8, y + 50), 3)
        pygame.draw.line(screen, black, (x + 34, y + 35), (x + 34, y + 50), 3)


class food_list:
    def __init__(self):
        self.length = 0
        self.head = None

    def addfood(self):
        node = food_item(random.randrange(0,980), 250,1)
        self.length += 1;
        if self.head == None:
            self.head = node

        else:
            node.next = self.head
            node.next.prev = node
            self.head = node
        return






class food_item:
    def __init__(self, x, y, kind):
        self.xcoord = x
        self.ycoord = y
        self.next = None   
        
    def draw_fooditem(self, screen):
        x = self.xcoord
        y = self.ycoord
        pygame.draw.ellipse(screen,yellow,[x, y, 15, 15])


