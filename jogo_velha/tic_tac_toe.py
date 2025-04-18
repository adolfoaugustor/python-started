import random
import os

class ticTacToe:
   def __init__(self):
      self.reset()

   def print_board(self):
      print("")
      print(" " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2])
      print("-----------")
      print(" " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2])
      print("-----------")
      print(" " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2])

   def reset(self):
      self.board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
      self.done = ""

   def check_win_or_draw(self):
      dict_win = {}
      for i in ["X", "0"]:
         # Horizontais
         dict_win[i] = (self.board[0][0] == i and self.board[0][1] == i and self.board[0][2] == i)
         dict_win[i] = (self.board[1][0] == i and self.board[1][1] == i and self.board[1][2] == i) or dict_win[i]
         dict_win[i] = (self.board[2][0] == i and self.board[2][1] == i and self.board[2][2] == i) or dict_win[i]
         # Verticais
         dict_win[i] = (self.board[0][0] == i and self.board[1][0] == i and self.board[2][0] == i) or dict_win[i]
         dict_win[i] = (self.board[0][1] == i and self.board[1][1] == i and self.board[2][1] == i) or dict_win[i]
         dict_win[i] = (self.board[0][2] == i and self.board[1][2] == i and self.board[2][2] == i) or dict_win[i]
         # Diagonais
         dict_win[i] = (self.board[0][0] == i and self.board[1][1] == i and self.board[2][2] == i) or dict_win[i]
         dict_win[i] = (self.board[2][0] == i and self.board[1][1] == i and self.board[0][2] == i) or dict_win[i]
      
      if dict_win["X"]:
         self.done = "X"
         print("X ganhou!")
         return

      elif dict_win["0"]:
         self.done = "0"
         print("0 ganhou!")
         return
      
      c = 0
      for i in range(3):
         for j in range(3):
            if self.board[i][j] != " ":
               c+=1
               break

      if c == 0:
         self.done = "d"
         print("Deu velha!")
         return

   def get_player_move(self):
      invalid_mode=True

      while invalid_mode:
         try:
            print("Digite a linha do seu proximo movimento:")
            x = int(input())

            print("Digite a coluna do seu proximo movimento:")
            y = int(input())

            if x > 2 or x < 0 or y > 2 or y < 0:
               print("Movimento inválido!")
               continue

            if self.board[x][y] != " ":
               print("Posição já preenchida.")
               continue
         except Exception as e:
            print("e")
            continue

         invalid_mode = False
      self.board[x][y] = "X"
   
   def make_move(self):
      list_moves=[]

      for i in range(3):
         for j in range(3):
            if self.board[i][j] == " ":
               list_moves.append((i,j))
      if len(list_moves) > 0:
         x,y = random.choice(list_moves)
         self.board[x][y] = "0"      

self = ticTacToe()
self.print_board()
next = 0

while next ==0:
   os.system("cls")
   self.print_board()
   while self.done == "":
      self.get_player_move()
      self.make_move()
      os.system("cls")
      self.print_board()
      self.check_win_or_draw()

   print("digite um pra sair ou 0 pra jogar de novo")
   next = int(input())
   if next == 1:
      break
   elif next == 0:
      self.reset()
      next = 0