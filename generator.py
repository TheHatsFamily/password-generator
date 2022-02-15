#!/usr/bin/python3
import random

passwds = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0',',','.','@','#','_','&','-','+','(',')','/','*','"',"'",':',';','!','?','~','`','|','÷','$','=','{','}','\\','%','[',']','<','>','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'

while True:
	try:
		passLength = int(input(f'{blue}Password Length (10-100): {green}'))
		if passLength > 9 and passLength < 101:
			pass
		else:
			print(f'{red}Password Length Must Be Greater Than 10 And Less Then 100')
			continue
	except ValueError:
		print(f'{red}Entered Any Integer [eg:- 5] And Minimum Password Length Is 6')
		continue
	else:
		while True:
			try:
				passTimes = int(input(f'{blue}How Much Passwords Do You Want: {green}'))
				if passTimes > 0:
					pass
				else:
					print(f'{red}Minimum Value Is 1')
					continue
			except ValueError:
				print(f'{red}Entered Any Integer [eg:- 5]')
			else:
				break
		break

for times in range(1, passTimes+1):
	print('\n')
	print(f'{yellow}[{green}+{yellow}] {yellow}Password is: {green}',end='')
	for i in range(1, passLength+1):
		print(random.choice(passwds), end='')
print('\n')
