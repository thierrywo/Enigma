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


tecoderenzin = input("Welke boodschap wil je encrypten?")

a = int(input("Welke setting wilt u voor rotor numero 1?")) # als je iets verkeerds invult crasht die, pff, die van mijn vorige commit was chiller maar kon daar abc niet in difine 
b = int(input("Welke setting wilt u voor rotor numero 2?"))
c = int(input("Welke setting wilt u voor rotor numero 3?"))

x = enigma(a, b, c)
encrypt = x.tekst_input(tecoderenzin)
print("Encrypte tekst:", encrypt)

#Afsluiting
while True: 
  antwoord = input("Nog een boodschap encrypten? (Vul in ja of nee)")
  if antwoord.lower() == "ja" : 
   continue 
  # hij moet nog returnen naar start
  elif antwoord.lower() == "nee" :
    print("Nou dan niet hoor, tieft dan maar een pleurisend op")
    exit() 
