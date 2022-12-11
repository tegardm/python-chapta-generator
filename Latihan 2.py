import random
import os
numbers = [1,2,3,4,5,6,7,8,9,0]
letters = ["a","b","c","d","e","f","g","h","i","j","g",'h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['!','@','$','%','&']


askIsRepeat = 'Ya'

while askIsRepeat == 'Ya':
	os.system('cls')
	print("\n\t\t= = = = = Chapta Generator = = = = =\t\t")
	print("\t\tSilahkan Masukan Kesulitan Password Yang Anda Inginkan (Easy/Medium/Advance) : \t\t")
	levels = ["Easy","Medium","Advance"]
	level = ''


	while level not in levels:
		level = input("\t\tMasukan Kesulitan Level = ")

	lengthChap = ''
	while lengthChap.isdigit() == False:
		lengthChap = input("\t\tMasukan Panjang Chapta = ")

	lengthChap = int(lengthChap)




	types = ["n",'l','s']


	def easy(x):
		chapta = ''
		for i in range(x):
			randEach = ''
			randEach = (random.choice(letters))
			chapta += randEach
		return chapta


	def medium(x):
		chapta = ''
		types.pop(2)
		for i in range(x):
			randType = random.choice(types)
			randEach = ''
			if randType == 'n':
				randEach = str( random.choice(numbers))
			elif randType == 'l':
				randEach = random.choice(letters)
			chapta += randEach
		return chapta


	def hard(x):
		chapta = ''
		for i in range(x):
			randType = random.choice(types)
			randEach = ''
			if randType == 'n':
				randEach = str( random.choice(numbers))
			elif randType == 'l':
				randEach = random.choice(letters)
			elif randType == 's':
				randEach = random.choice(symbols)
			chapta += randEach


		return chapta



	if level == levels[0]:
		print("\t\tChapta = "+easy(lengthChap))
	elif level == levels[1]:
		print("\t\tChapta = "+medium(lengthChap))
	elif level == levels[2]:
		print("\t\tChapta = "+hard(lengthChap))


	askIsRepeat = input("\t\tUlang ? (Ya / Tidak) =  ")

