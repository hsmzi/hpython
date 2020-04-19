# -*- coding: utf-8 -*-
import random 
print("Hani losowanie🌹🌺")
kotekipiesek=0
while True:
	liczba1=random.randint(0,1000)
	liczba2=random.randint(0,1000)


	print("masz (%d)  punktow. ile to jest (%d + %d) " % (kotekipiesek,liczba1,liczba2))


	kotek = input("wpisz wynik 😀:")


	if kotek==liczba1+liczba2:
		print("🎉dobra robota🎉")
		kotekipiesek=kotekipiesek+1
	else:
		print("😣zła robota😣. dobry wynik to %d" % (liczba1+liczba2))
		break 




