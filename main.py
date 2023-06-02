
import random
#jackpot main
print("==>Welcome this is a jackpot machine<==\n"
"*more info: if you win you'll get 10 points and if you lose you won't recieve any points!!")
print("1 player or 2 players?")
a = input("1 or 2?")
firstwheel=0
secondwheel=0
thirdwheel=0
stake = 0
if a =="1" :
 while True:
    import cal
    firstWheel = print(random.randint(0,9))
    secondWheel = print(random.randint(0,9))
    thirdWheel = print(random.randint(0,9))
    result=print(cal.printScore())
    print("---continue?{yes,no}")
    e = input("1/2?")
    if e =="2" :
      print("SEE YOU NEXT TIME")
      break
if a=="2":
  while True:
    import cal
    firstWheel = print(random.randint(0,9))
    secondWheel = print(random.randint(0,9))
    thirdWheel = print(random.randint(0,9))
    result=print(cal.printScore())
    print("...waiting for other player...")
    player2 = 0
    firstwheel1=0
    secondwheel1=0
    thirdwheel1=0
    firstWheel1 = print(random.randint(0,9))
    secondWheel1 = print(random.randint(0,9))
    thirdwheel1=print(random.randint(0,9))
    result=print(cal.printScore1())
    print("---continue?{yes,no}")
    e = input("1/2?")
    if e == "2" :
     print("SEE YOU NEXT TME")
     break

#cal.py #module
firstwheel=0
secondwheel=0
thirdwheel=0

def printScore():
 if firstwheel=="0" and secondwheel=="0 "and thirdwheel=="0":
    print("YOU WON THE JACKPOT!!!")
 elif firstwheel=="1" and secondwheel=="1" and thirdwheel=="1":
   print("YOU WON THE JACKPOT!!!")
 elif firstwheel=="2" and secondwheel=="2" and thirdwheel=="2":
   print("YOU WON THE JACKPOT!!!")
 elif firstwheel=="3" and secondwheel=="3" and thirdwheel=="3":
   print("YOU WON THE JACKPOT!!!")
 elif firstwheel=="4" and secondwheel=="4" and thirdwheel=="4":
   print("YOU WON THE JACKPOT!!!")
 elif firstwheel=="5" and secondwheel=="5" and thirdwheel=="5":
    print("YOU WON THE JACKPOT!!!")
 elif firstwheel=="6" and secondwheel=="6" and thirdwheel=="6":
    print("YOU WON THE JACKPOT!!!")
 elif firstwheel=="7" and secondwheel=="7" and thirdwheel=="7":
   print("YOU WON THE JACKPOT!!!")
 elif firstwheel=="8" and secondwheel=="8" and thirdwheel=="8":
    print("YOU WON THE JACKPOT!!!")
 elif firstwheel=="9" and secondwheel=="9 "and thirdwheel=="9":
    print("YOU WON THE JACKPOT!!!")
 else:
    print("SORRY,YOU LOST")

def printScore1():
 if firstwheel=="0" and secondwheel=="0 "and thirdwheel=="0":
    print("YOU WON THE JACKPOT!!!")
 elif firstwheel=="1" and secondwheel=="1" and thirdwheel=="1":
   print("YOU WON THE JACKPOT!!!")
 elif firstwheel=="2" and secondwheel=="2" and thirdwheel=="2":
   print("YOU WON THE JACKPOT!!!")
 elif firstwheel=="3" and secondwheel=="3" and thirdwheel=="3":
   print("YOU WON THE JACKPOT!!!")
 elif firstwheel=="4" and secondwheel=="4" and thirdwheel=="4":
   print("YOU WON THE JACKPOT!!!")
 elif firstwheel=="5" and secondwheel=="5" and thirdwheel=="5":
    print("YOU WON THE JACKPOT!!!")
 elif firstwheel=="6" and secondwheel=="6" and thirdwheel=="6":
    print("YOU WON THE JACKPOT!!!")
 elif firstwheel=="7" and secondwheel=="7" and thirdwheel=="7":
   print("YOU WON THE JACKPOT!!!")
 elif firstwheel=="8" and secondwheel=="8" and thirdwheel=="8":
    print("YOU WON THE JACKPOT!!!")
 elif firstwheel=="9" and secondwheel=="9 "and thirdwheel=="9":
    print("YOU WON THE JACKPOT!!!")
 else:
    print("SORRY,YOU LOST" )