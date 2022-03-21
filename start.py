#!/usr/bin/env python3

import sys  
import os

def decript(encoded):
	alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	encoded = encoded
	encoded = encoded.upper()
	shift = 0
	print(encoded.upper())
	for x in range(0, len(alphabet)):
		shift += 1
		shifted_set = ""
				
		for index in range(shift, len(alphabet)):
			shifted_set += alphabet[index]
			
		for index in range(0, shift-1):
			shifted_set += alphabet[index]
	
		decoded = ""
		
		for letter in encoded:
			index = shifted_set.find(letter)
			decoded += alphabet[index]	
				
		print(decoded)
def main():
	while 1:
		print("\nWaiting for message........")
		os.system('tshark -i eth0 -f "tcp port 45" -Y "tcp.port == 45 and tcp.payload" -T fields -e tcp.payload>aux.txt -c 1')
		file1 = open('aux.txt', 'r')
		lines = file1.readlines()
		for line in lines:
				bytes_array = bytes.fromhex(line)
				myline=bytes_array.decode()
				words= myline.split()
				print("Decriptare:")
				cont=1
				for word in words:
					print("Word {}:".format(cont))
					decript(word)
					cont+=1
if __name__ == '__main__':
	main()
