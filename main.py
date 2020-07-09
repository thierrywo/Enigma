alfabet = "abcdefghijklmnopqrstuvwxyz"

class enigma:
  Rotor_1 = 0
  Rotor_2 = 0
  Rotor_3 = 0

  def __init__(self, Rotor_1,Rotor_2,Rotor_3) :
    self.Rotor_a = Rotor_1
    self.Rotor_b = Rotor_2
    self.Rotor_c = Rotor_3

  def rotordraai(self, aantaldraaien):
   aantaldraaien = aantaldraaien % 26
   veranderde_alfabet = list(alfabet)
   for i in range(aantaldraaien):
      veranderde_alfabet.insert(0, veranderde_alfabet[-1])
      veranderde_alfabet.pop(-1)
   return veranderde_alfabet

  def volgende_letter(self, rotor, char) :
    veranderde_alfabet = self.rotordraai(rotor)
    letterIndex = alfabet.index(char)
    return veranderde_alfabet[letterIndex]


  def rotors_draaien(self, plaats) :
    self.Rotor_a = self.Rotor_a + 1

    if(plaats % 26 == 0):
      self.Rotor_b = self.Rotor_b + 1

    if(plaats % (26*26)==0):
      self.Rotor_c = self.Rotor_c + 1

  def tekst_input(self, tekst) :
    tekst = tekst.lower()
    gecodeerde_tekst = []
    plaats = 0


    for char in list(tekst) :
      if not char in alfabet :
        gecodeerde_tekst.append(char)
        continue

      gecodeerde_letter = self.volgende_letter(self.Rotor_a, char)
      gecodeerde_letter = self.volgende_letter(self.Rotor_b, gecodeerde_letter)
      gecodeerde_letter = self.volgende_letter(self.Rotor_c, gecodeerde_letter)


      gecodeerde_tekst.append(gecodeerde_letter)

      self.rotors_draaien(plaats)
      plaats = plaats + 1

    return str.join("", gecodeerde_tekst)

class renigma:
  Rotor_1 = 0
  Rotor_2 = 0
  Rotor_3 = 0

  def __init__(self, Rotor_1,Rotor_2,Rotor_3) :
    self.Rotor_a = Rotor_1
    self.Rotor_b = Rotor_2
    self.Rotor_c = Rotor_3

  def decode_rotordraai (self, aantaldraaien):
    veranderde_alfabet = list(alfabet)
    for i in range (aantaldraaien):
      veranderde_alfabet.append (veranderde_alfabet[0])
      veranderde_alfabet.pop(0)
    return veranderde_alfabet

  def volgende_letter(self, rotor, char) :
    veranderde_alfabet = self.decode_rotordraai(rotor)
    letterIndex = alfabet.index(char)
    return veranderde_alfabet[letterIndex]


  def rotors_draaien(self, plaats) :
    self.Rotor_a = self.Rotor_a + 1

    if(plaats % 26 == 0):
      self.Rotor_b = self.Rotor_b + 1

    if(plaats % (26*26)==0):
      self.Rotor_c = self.Rotor_c + 1

  def tekst_input2(self, tekst) :
    tekst = tekst.lower()
    gedecodeerde_tekst = []
    plaats = 0


    for char in list(tekst) :
      if not char in alfabet :
        gedecodeerde_tekst.append(char)
        continue

      gedecodeerde_letter = self.volgende_letter(self.Rotor_a, char)
      gedecodeerde_letter = self.volgende_letter(self.Rotor_b, gedecodeerde_letter)
      gedecodeerde_letter = self.volgende_letter(self.Rotor_c, gedecodeerde_letter)


      gedecodeerde_tekst.append(gedecodeerde_letter)

      self.rotors_draaien(plaats)
      plaats = plaats + 1

    return str.join("", gedecodeerde_tekst)

while True: 
  while True:     
    vraagzin = input("\nWil je een boodschap encrypten of decrypten?\n")
    if vraagzin.lower() == "encrypten":

      tecoderenzin = input("\nWelke boodschap wil je encrypten?\n")

      while True:
        try:
          a = int(input("\nWelke setting wilt u voor rotor numero 1?\n"))
          if 0 >= a or a <= 26:
            break
          else:
            print("Je moet een getal kiezen en niks anders. Kies dus een getal tussen 0 en 26")
        except ValueError:
          print("Dit is geen nummer hoor!")

      while True:
        try:
          b = int(input("\nWelke setting wilt u voor rotor numero 2?\n"))
          if 0 >= b or b <= 26:
            break
          else:
            print("Je moet een getal kiezen en niks anders. Kies dus een getal tussen 0 en 26")
        except ValueError:
          print("Dit is geen nummer hoor!")


      while True:
        try:
          c = int(input("\nWelke setting wilt u voor rotor numero 3?\n"))
          if 0 >= c or c <= 26:
            break
          else:
            print("Je moet een getal kiezen en niks anders. Kies dus een getal tussen 0 en 26")
        except ValueError:
          print("Dit is geen nummer hoor!")

      x = enigma(a, b, c)
      encrypt = x.tekst_input(tecoderenzin)
      print("\nEncrypte tekst:", encrypt)

    elif vraagzin.lower() == "decrypten":
      tedecoderenzin = input("\nWelke boodschap wil je decrypten?\n")

      while True:
        try:
          a = int(input("\nWelke setting had u voor rotor numero 1?\n"))
          if 0 >= a or a <= 26:
            break
          else:
            print("Dit was zeker niet het gekozen getal. Kies dus een getal tussen 0 en 26")
        except ValueError:
          print("Dit is geen nummer hoor!")

      while True:
        try:
          b = int(input("\nWelke setting had u voor rotor numero 2?\n"))
          if 0 >= b or b <= 26:
            break
          else:
            print("Dit was zeker niet het gekozen getal. Kies dus een getal tussen 0 en 26")
        except ValueError:
          print("Dit is geen nummer hoor!")


      while True:
        try:
          c = int(input("\nWelke setting wilt u voor rotor numero 3?\n"))
          if 0 >= c or c <= 26:
            break
          else:
            print("Dit was zeker niet het gekozen getal. Kies dus een getal tussen 0 en 26")
        except ValueError:
          print("Dit is geen nummer hoor!")

      y = renigma(a, b, c)
      decrypt = y.tekst_input2(tedecoderenzin)
      print("\nDecrypte tekst:", decrypt)

    else: 
      print("\nJe kan alleen kiezen uit encrypten of decrypten. Typ dus het woord 'encrypten' om te encrypten en het woord 'decrypten' om te decrypten!!! ")
      break

    while True:
      antwoord = input('\nWil je nog een boodschap encrypten of decrypten? (ja of nee): \n')
      if antwoord.lower() == "ja":
        break

      elif antwoord.lower() == "nee":
        print("Nou dan niet hoor, tieft dan maar een pleurisend op")
        quit()

      else: print('Potverjandriedubbeltjes, je kan alleen ja of nee invullen, niks anders!!!')
