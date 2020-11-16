from os import system, name
import random
import time

board = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
] 

position = [1,2,3,4,5,6,7,8,9]

def clear():
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')

def printBoard():
  for i in range(len(board)):
    for j in range(len(board)):
      if j != 2:
        print(str(board[i][j]) + " | ", end='')
      elif i != 2:
        print(str(board[i][j]) + "\n- - - - -\n", end='')
      else:
        print(str(board[i][j]))

def resetBoard():
  x = 1
  for i in range(len(board)):
    for j in range (len(board)):
      board[i][j] = x
      x += 1

def playGame():
  turn = 0
  played = 0
  pos = 0
  playing = True
  win = False
  x = "X"
  o = "O"
  
  clear()
  while playing:
    printBoard()

    win = checkWin()

    # if win:
    #   if turn % 2 == 0:
    #     print('O has won the match')
    #     break
    #   else:
    #     print('X has won the match')
    #     break
    # elif win == False and pos == 9:
    #   print('The match is a draw')
    #   break
    # if turn % 2 == 0:
          
    ai = random.choice(position)
    print(f'chose {ai}')

    for i in range(len(board)):
      for j in range(len(board)):
        if turn % 2 == 0:
          if ai == board[i][j]:
            print(f'turn {turn}')
            position.remove(ai)
            board[i][j] = x
            turn += 1
            time.sleep(2)
        else:
          turn += 1
    print('\n')
 
    played += 1
    if played > 5:
      break
  print(position)

def checkWin():
  row = 0
  column = 0

  for i in range(len(board)):
    for j in range(len(board)):
      if board[row][column] == board[row][column+1] and board[row][column] == board[row][column+2]:
        return True

      elif board[row+1][column] == board[row+1][column+1] and board[row+1][column] == board[row+1][column+2]:
        return True

      elif board[row+2][column] == board[row+2][column+1] and board[row+2][column] == board[row+2][column+2]:
        return True
      
      elif board[row][column] == board[row+1][column] and board[row][column] == board[row+2][column]:
        return True

      elif board[row][column+1] == board[row+1][column+1] and board[row][column+1] == board[row+2][column+1]:
        return True
      
      elif board[row][column+2] == board[row+1][column+2] and board[row][column+2] == board[row+2][column+2]:
        return True
      
      elif board[row][column] == board[row+1][column+1] and board[row][column] == board[row+2][column+2]:
        return True
      
      elif board[row][column+2] == board[row+1][column+1] and board[row][column+2] == board[row+2][column]:
        return True
      return False

def playAgain():
  input('Enter to play again')
  clear()
  playGame()

if __name__ == '__main__':
  playGame()