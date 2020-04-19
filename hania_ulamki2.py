# -*- coding: utf-8 -*-

def nwd(a, b): return nwd(b, a%b) if b else a

print("hania + ulamki🦄🎉🎶")
class Ulamek:
	def __init__(self, licznik=0, mianownik=0):
		self.licznik = licznik
		self.mianownik = mianownik 

	def wypisz(self):
		print(" " + str(self.licznik))
		print("---")
		print(" " + str(self.mianownik))

	def wprowadz(self):
		self.licznik = input("wpisz licznik")
     		self.mianownik = input("wpisz mianownik") 
  
	def skroc(self):
		#return
		najwiekszy_wspolny_mianownik_i_licznik_na_swiecie = nwd(self.licznik, self.mianownik)
		self.licznik = self.licznik / najwiekszy_wspolny_mianownik_i_licznik_na_swiecie 
		self.mianownik = self.mianownik / najwiekszy_wspolny_mianownik_i_licznik_na_swiecie

ulamek1 = Ulamek()
ulamek1.wprowadz()

dzialanie=raw_input("wpisz+lub-")

ulamek2 = Ulamek()
ulamek2.wprowadz()

ulamek1.wypisz()
print(dzialanie)
ulamek2.wypisz()
print("=")

wspolny_mianownik = ulamek1.mianownik * ulamek2.mianownik 

if dzialanie == "+":
	nowy_licznik = (ulamek1.licznik*ulamek2.mianownik) + (ulamek2.licznik*ulamek1.mianownik)

if dzialanie == "-":
	nowy_licznik = (ulamek1.licznik*ulamek2.mianownik) - (ulamek2.licznik*ulamek1.mianownik)

kotek = Ulamek(nowy_licznik, wspolny_mianownik)
kotek.skroc()
kotek.wypisz()

