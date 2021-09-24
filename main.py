import os



class Game:
  def __init__(self):
    global exit
    self.tomon = 0   # to'g'riga
    self.postion = ["to'gri","o'ng","ortqa","chap"]
  

  def start_game(self):
    isExit = False
    global inp_position

    while not isExit:
      os.system("clear")

      print("Qaysi tomonga va necha marta burilish kerak")
      inp_position = "".join((map(str, input("Kiriting: ")))).strip(",.;:#@ ").split()

      if inp_position[0].lower() == "right":
        self.turn_right(int(inp_position[1]))
      elif inp_position[0].lower() == "left": 
        self.turn_left(int(inp_position[1]))
      elif inp_position[0].lower() == "back": 
        self.turn_back(int(inp_position[1]))
      elif inp_position[0].lower() == "exit":
        isExit=True
    

    print(self.postion[self.tomon])

    

  def turn_right(self, pos):
    self.tomon =(self.tomon+pos) % 4
    
  def turn_left(self, pos):
    tomonlar = [2,3,0,1]
    
    self.tomon = tomonlar[(self.tomon+pos)%4]
    
  def turn_back(self, pos):
    if self.tomon == 0:
      qarshi = [0,2]
    elif self.tomon == 1:
      qarshi = [1,3]  
    elif self.tomon == 2:
      qarshi = [2,0]
    elif self.tomon == 3:
      qarshi = [3,1]

    self.tomon = qarshi[(self.tomon+pos)%2]


game = Game()

game.start_game()


