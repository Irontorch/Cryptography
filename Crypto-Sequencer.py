##       \\===========//
##       || IRONTORCH ||
##       //===========\\
## Cryptographic Sequencer Ver.I

from random import seed, choice, randint, shuffle
from os import system

def main():
	system('cls')
	key_init = \
	['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J',
	'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 
	'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', '1', '2', '3', '4', '5', 
	'6', '7', '8', '9', '0', '@', '#', '$', '%', '&', '!', '?', ' ', "'", '.', ',', '-', '\n', '"',
	'-', '—', ';', ':', '/', '\\']
	
	encrypt = input('Enter key: ')
	seed(encrypt)
	print()
	
	key_shfl = key_init.copy()
	shuffle(key_shfl)

	user_select = input('[E]ncrypt or [U]nencrypt?: ')
	print()
	
	if user_select == 'E':
		
		file_in = open('Input.txt', 'r')
		file_out = open('Output.txt', 'w')
		print('Input:')
		for line in file_in:
			for char in line:
				print(char, end='')
				i = key_init.index(char)
				file_out.write(key_shfl[i])
	
	if user_select == 'U':
	
		file_in = open('Input.txt', 'r')
		file_out = open('Output.txt', 'w')
		print('Input:')
		for line in file_in:
			for char in line:
				print(char, end='')
				i = key_shfl.index(char)
				file_out.write(key_init[i])
				
	file_in.close()
	file_out.close()
	print()
	input()
	main()
main()		


	