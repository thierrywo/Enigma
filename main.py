alfabet = "abcdefghijklmnopqrstuvwxyz"
rotoren = [] 
Encryptedmessage = []

def Rotorsettings():
  print("Voer de standen van de rotoren in.")
  for x in range(3):
    while True:
      print("Welke setting wilt u voor rotor numero {}?".format(x+1))
      try:
       rotoren.append([alfabet,int(input())]) #hij pakt nu oook getallen boven 26
       break
      except:
        print("Het is niet zo moeilijk. Je hoeft alleen maar een nummer in te vullen en je mag zelfs nummer 1 tot 26 kiezen")

print("Welke boodschap wil je encrypten?")
tecoderenzin = input().lower

Rotorsettings()




#Afsluiting
while True: 
  antwoord = input("Nog een boodschap encrypten? (Vul in ja of nee)")
  if antwoord.lower() == "ja" : 
   continue 
  # hij moet nog returnen naar start
  elif antwoord.lower() == "nee" :
    print("Nou dan niet hoor, tieft dan maar een pleurisend op")
    break 
