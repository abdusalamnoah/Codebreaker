import random
code = [random.randint(0,9) for x in range(4)]
for t in range(5):
   y = 0
   user = int(input("Guess the 4-digit code: "))
   guess = [int(x) for x in str(user)]
   code_used = [False] * 4
   guess_used = [False] * 4


   if guess == code:
       print("You've got it!")
       break
   else:
       while y < len(code):
           if guess[y] == code[y]:
               print(f"The #{y+1} digit is in the right place")
               code_used[y], guess_used[y] = True, True
           y+=1
       print(code_used)
       for i in range(4):
           if not guess_used[i]:
               for j in range(4):
                   if not code_used[j] and guess[i] == code[j]:
                       print(f"The #{i + 1} digit you guessed is in the code but in the wrong place")
                       code_used[j] = True
                       break
               else:
                   print(f"The #{i + 1} digit is not in the code")
print(f"My code was: {code}")