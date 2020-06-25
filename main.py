# maak hier de hele enigma machine in python :D
alfabet = "abcdefghijklmnopqrstuvwxyz"
rotoren = [] 
Encryptedmessage = []

print("Welke boodschap wil je encrypten?")
tecoderenzin = input().lower

print("Welke setting zou je willen voor de rotoren")

while True:
  print("Setting voor rotor nummero 1") 
  settingrot1 = input()
  if settingrot1 <= 0 or settingrot1 >=25: 
    break 
  else: 
    print("He is niet zo moeilijk. Je hoeft alleen maar een nummer in te vullen en je mag zelfs nummer 1 tot 26 kiezen")

while True:
  print("Setting voor rotor nummero 2") 
  settingrot2 = input()
  if settingrot2 <= 0 or settingrot2 >=25: 
    break 
  else: 
    print("He is niet zo moeilijk. Je hoeft alleen maar een nummer in te vullen en je mag zelfs nummer 1 tot 26 kiezen")

while True:
  print("Setting voor rotor nummero 3") 
  settingrot3 = input()
  if settingrot3 <= 0 or settingrot3 >=25: 
    break 
  else: 
    print("He is niet zo moeilijk. Je hoeft alleen maar een nummer in te vullen en je mag zelfs nummer 1 tot 26 kiezen")

while True: 
  antwoord = input("Nog een boodschap encrypten? (Vul in ja of nee)")
  if antwoord.lower("ja"): 
    break 
  
  elif antwoord.lower("nee"): 
    print("Nou dan niet hoor, tieft dan maar een pleurisend op")
    exit 
