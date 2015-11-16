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

def win_or_lose(val):
	if val<21:
		return 0
	elif val==21:
		return 1
	else:
		return -1

def final_status(val):
	if val==2:
		return "No cóż..."
	elif val<10:
		return "Zawsze mogło być gorzej :)"
	elif val<15:
		return "Nieźle, próbuj dalej! :)"
	elif val<20:
		return "Świetnie, coraz bliżej! :)"
	else:
		return "Najgorzej, co?"

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
hand = []			    #karty na rece gracza
valuesSum = 0		    #suma wartosci kart gracza
legalOpFirstLoop = 'pd' #menu "pas - dobierz"
legalOpSecLoop = 'tn'   #menu po grze, jeszcze raz: "tak - nie"

#glowna petla gry

while 1:
	hand.append(deck.pop())
	print "Oto Twoje karty:\n"
	print_cards(hand)
	
	valuesSum = sum_values(hand)
	print "Suma wartości Twoich kart wynosi: " + str(valuesSum)
	
	isEnd = win_or_lose(valuesSum)
	if isEnd:
		if isEnd>0:
			print "OCZKO! Wygrałeś, gratulacje!"
		else:
			print "Niestety, przegrałeś! :("

		#menu po skonczeniu gry
		act = menu_quit()
		while legalOpSecLoop.find(act)<0:
			print "Niepoprawna opcja"
			act = menu_quit()
		else:
			if act=='t':
				valuesSum = 0
				hand = []
				deck = make_deck()
				random.shuffle(deck)
				continue
			else:
				break
	
	act = menu_draw_pass()
	while legalOpFirstLoop.find(act)<0:
		print "Niepoprawna opcja"
		act = menu_draw_pass()
	else:
		if act=='p':
			print "Pasujesz. Do oczka brakowało Ci: " + str(21 - valuesSum) + ". " + final_status(valuesSum)
			#menu po spasowaniu - po skonczeniu gry
			act = menu_quit()
			while legalOpSecLoop.find(act)<0:
				print "Niepoprawna opcja"
				act = menu_quit()
			else:
				if act=='t':
					valuesSum = 0
					hand = []
					deck = make_deck()
					random.shuffle(deck)
					continue
				else:
					break
		else:
			pass

print "Dziekuję za grę! Do zobaczenia"
