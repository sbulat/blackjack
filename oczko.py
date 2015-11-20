# -*- coding: utf-8 -*-

def make_deck():
	deck = []
	# c - karo, k - kier, p - pik, t - trefl
	colours = ['c', 'k', 'p', 't']
	values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
	for c in colours:
		for v in values:
			tmp = (v, c)
			deck.append(tmp)

	return deck

def get_value(v):
	if v>=2 and v<=10:
		return v
	elif v == 'J':
		return 2
	elif v == 'Q':
		return 3
	elif v == 'K':
		return 4
	elif v == 'A':
		return 11

def print_upper_line(card):
	return '|' + str(card[0]) + str(card[1]) + ('  |' if card[0]==10 else '   |')

def print_lower_line(card):
	return ('|  ' if card[0]==10 else '|   ') + str(card[1]) + str(card[0]) + "|"

def print_cards(cards):
	toPrint = []
	for i in range(len(cards)):
		toPrint.append("+-----+")
	for card in cards:
		toPrint.append(print_upper_line(card))
	for i in range(len(cards)*2):
		toPrint.append("|     |")
	for card in cards:
		toPrint.append(print_lower_line(card))
	for i in range(len(cards)):
		toPrint.append("+-----+")

	for i in range(len(toPrint)):
		print toPrint[i],
		if ((i+1)%len(cards))==0:
			print

def sum_values(cards):
	total = 0
	for card in cards:
		total += get_value(card[0])
	return total

def is_end(val):
	if val[0]<21 and val[1]<21:
		return 0
	elif val[0]==21:
		return 1
	elif val[1]==21:
		return 2
	elif val[0]>21:
		return -1
	else:
		return -2

def is_persian(hand):
	if len(hand)==2 and hand[0][0]==hand[1][0]:  # czy na rece są dwa asy
		return 1
	else:  # przegrana
		return 0

# def final_status(val):
# 	if val==2:
# 		return "No cóż..."
# 	elif val<10:
# 		return "Zawsze mogło być gorzej :)"
# 	elif val<15:
# 		return "Nieźle, próbuj dalej! :)"
# 	elif val<20:
# 		return "Świetnie, coraz bliżej! :)"
# 	else:
# 		return "Najgorzej, co?"

def who_win(plyr, comp):
	if plyr[0] > comp[0]:
		return "Gratulacje, wygrałeś!"
	elif comp[0] > plyr[0] and comp[0]<22:
		return "Przegrałeś! :("
	else: # jeśli remis porównuje pierwszą karte na ręce
		if get_value(plyr[1]) > get_value(comp[1]):
			return "Gratulacje, wygrałeś!"
		elif get_value(comp[1]) > get_value(plyr[1]):
			return "Przegrałeś! :("
		else:
			return "REMIS!"

def menu_draw_pass():
	print "p - pasuj"
	print "d - dobierz"
	print "Co chcesz zrobić?"
	return raw_input().lower()

def menu_quit():
	print "Czy chcesz zagrać jeszcze raz?(t/n)"
	return raw_input().lower()

import random
deck = make_deck()      #utworz talie
random.shuffle(deck)    #i ja potasuj
plyrHand = []		    #karty na rece gracza
compHand = []
compHand.append(deck.pop())
plyrSum = 0		    #suma wartosci kart gracza
compSum = 0
plyrFold = False
compFold = False
legalOpFirstLoop = 'pd' #menu "pas - dobierz"
legalOpSecLoop = 'tn'   #menu po grze, jeszcze raz: "tak - nie"

#glowna petla gry
while 1:
	if plyrFold==False:
		plyrHand.append(deck.pop())

	print "Oto Twoje karty:\n"
	print_cards(plyrHand)  # wyświetlanie kart gracza
	plyrSum = sum_values(plyrHand)  # sprawdzanie sumy kart na rece gracza
	print "Suma wartości Twoich kart wynosi: " + str(plyrSum)

	print "\n"

	print "Oto karty przeciwnika:\n"
	print_cards(compHand)  # wyświetlenie kart komputera
	compSum = sum_values(compHand)  # sprawdzanie sumy kart na rece komputera
	print "Suma wartości kart przeciwnika wynosi: " + str(compSum)

	isEnd = is_end( (plyrSum, compSum) )  # sprawdzam sume wart gracza w porównaniu do 21
	if isEnd:  # jeśli >=21 to koniec gry
		if isEnd>0:  # wygrana
			if isEnd==1:
				print "OCZKO! Wygrałeś, gratulacje!"
			else:
				print "Komputer zdobył OCZKO! Przegrałeś :("
		else:  # przegrana lub perskie oczko
			if isEnd==-1:
				if is_persian(plyrHand):  # czy na rece ma dwa asy
					print "PERSKIE OCZKO! Wygrałeś, gratulacje!"
				else:  # przegrana
					print "Niestety, przegrałeś! :("
			else:
				if is_persian(compHand):  # czy na rece ma dwa asy
					print "Komputer zdobył PERSKIE OCZKO! Niestety, przegrałeś!"
				else:  # przegrana
					print "Komputer przekroczył 21, wygrałeś!"

		#menu po skonczeniu gry
		act = menu_quit()
		while legalOpSecLoop.find(act)<0:
			print "Niepoprawna opcja"
			act = menu_quit()
		else:
			if act=='t':  # gra jeszcze raz, zerowanie: sumy, kart na rece; tworzenie talii od nowa
				plyrSum = compSum = 0
				plyrFold = compFold = False
				plyrHand = []
				compHand = []
				isEnd = 0

				deck = make_deck()
				random.shuffle(deck)
				compHand.append(deck.pop())
				continue
			else:
				break

	if compFold==False:
		if compSum>plyrSum and plyrFold==True:
			compFold=True
		elif compSum>17 and compSum>plyrSum:
			compFold=True
		elif compSum<plyrSum and compSum<21:
			compHand.append(deck.pop())
		elif compSum>18:
			compFold=True
		else:
			compHand.append(deck.pop())
	
	if compFold==True and plyrFold==True:
		print who_win( (plyrSum, plyrHand[0][0]), (compSum, compHand[0][0]) )
		act = menu_quit()
		while legalOpSecLoop.find(act)<0:
			print "Niepoprawna opcja"
			act = menu_quit()
		else:
			if act=='t':
				plyrSum = compSum = 0
				plyrFold = compFold = False
				plyrHand = []
				compHand = []
				isEnd = 0

				deck = make_deck()
				random.shuffle(deck)
				compHand.append(deck.pop())
				continue
			else:
				break

	if plyrFold==True:
		continue

	act = menu_draw_pass()
	while legalOpFirstLoop.find(act)<0:
		print "Niepoprawna opcja"
		act = menu_draw_pass()
	else:
		if act=='p':
			plyrFold = True
			if compFold==True:
				print who_win( (plyrSum, plyrHand[0][0]), (compSum, compHand[0][0]) )
				#menu po spasowaniu - po skonczeniu gry
				act = menu_quit()
				while legalOpSecLoop.find(act)<0:
					print "Niepoprawna opcja"
					act = menu_quit()
				else:
					if act=='t':
						plyrSum = compSum = 0
						plyrFold = compFold = False
						plyrHand = []
						compHand = []
						isEnd = 0

						deck = make_deck()
						random.shuffle(deck)
						compHand.append(deck.pop())
						continue
					else:
						break
			else:
				pass
		else:
			pass

print "Dziekuję za grę! Do zobaczenia"