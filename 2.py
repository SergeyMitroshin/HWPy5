# Создайте программу для игры в ""Крестики-нолики"".

board = list(range(1,10))

def draw(board):
   for i in range(3):
      print(board[0+i*3], board[1+i*3], board[2+i*3])


def inp(player_token):
   valid = False
   while not valid:
      ans = input("Куда поставить " + player_token+"? ")
      try:
         ans = int(ans)
      except:
         print("Некорректный ввод!")
         continue
      if ans >= 1 and ans <= 9:
         if(str(board[ans-1]) not in "XO"):
            board[ans-1] = player_token
            valid = True
         else:
            print("Клетка занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def checkboard(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw(board)
        if counter % 2 == 0:
           inp("X")
        else:
           inp("O")
        counter += 1
        if counter > 4:
           tmp = checkboard(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw(board)
main(board)
