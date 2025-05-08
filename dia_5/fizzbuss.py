def fizbuss():
   return [x for x in range(1,101)]

def validador():
   for numero in fizbuss():
      if numero % 3 == 0 and numero % 5 == 0:
         print("FIZZ BUZZ")
      elif numero % 3 == 0:
         print("FIZZ")
      elif numero % 5== 0:
         print("BUZZ")
      else:
         print(numero)

      

if __name__=="__main__":
    validador()