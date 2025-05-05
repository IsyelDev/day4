
print("Welcome")
try:
    lado = int(input("right is 0 or left is 1 \n" ))
    if lado == 1:
       nadar = int(input("swing is 0 or wait is 1 \n" ))
       if nadar == 1:
           door = int(input("blue is 0 or red is 1 or 2 yellow or game over \n" ))
           if door==0:
              print("Eaten by beast Game over")
           elif door ==1:
              print("Eaten by beast Game over")
           elif door==2:
              print("Wing")
           else:
              print("Game Over")
       else:
          print("Fall into a hole Game Over")
    else:
      print("Fall into a hole Game Over")
except ValueError:
   print("invalid input")
#if __name__=="__main__":
    #print(validacion())
