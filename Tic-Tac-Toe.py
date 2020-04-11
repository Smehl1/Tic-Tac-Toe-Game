class Tic_Tac_Toe():

  def __init__(self):
    self.is_Playing = True
    self.board = ["0","1","2",
                  "3","4","5",
                  "6","7","8"]

  def play_Game(self):
    while self.is_Playing == True:
      answer = input ("What would you like to do? ")

      if answer == ("Quit"):
        self.is_Playing = False
      elif answer == ("Fill square"):
        index = input ("Which square would you like to fill? ")
        letter = input ("Which player will fill the square? ")

        self.fill_Square(int(index), letter)
        self.print_Board()
      
      self.detect_Winner()

  def fill_Square(self, index, letter): 
    if index > (8) and index < (0):
      print("Please enter a number between 0 and 8.")
      return
    if letter != ("o") and letter != ("x"):
      print ("Please use the letters _o_ or _x_ ")
      return
    if self.board[index] == "o" or self.board[index] == "x":
      print ("That space is already taken.")
      return
    
    self.board[index] = letter

  def clear_Board(self):
    self.board = ["0","1","2",
                  "3","4","5",
                  "6","7","8"]

  def print_Board(self):
    for x in range(0,9):
      print (self.board[x] + "|" , end =" ")
      if ((x + 1) % 3) == 0:
        print ()
    print()
  
  def display_Winner(self,value):
    print ("The winner is " + (value))
    self.is_Playing = False

  def detect_Winner(self):
    if self.board[0] == self.board[1] and self.board[1] == self.board[2]:
      self.display_Winner(self.board[0])
    elif self.board[3] == self.board[4] and self.board[4] == self.board[5]:
      self.display_Winner(self.board[3])
    elif self.board[6] == self.board[7] and self.board[7] == self.board[8]:
      self.display_Winner(self.board[6])
    elif self.board[0] == self.board[3] and self.board[3] == self.board[6]:
      self.display_Winner(self.board[0])
    elif self.board[1] == self.board[4] and self.board[4] == self.board[7]:
      self.display_Winner(self.board[1])
    elif self.board[2] == self.board[5] and self.board[5] == self.board[8]:
      self.display_Winner(self.board[2])
    elif self.board[0] == self.board[4] and self.board[4] == self.board[8]:
      self.display_Winner(self.board[0])
    elif self.board[2] == self.board[4] and self.board[4] == self.board[6]:
      self.display_Winner(self.board[4])
  
Game = Tic_Tac_Toe()

Game.print_Board()

Game.play_Game()
