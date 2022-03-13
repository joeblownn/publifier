import os, re
re.compile('[\W_]+', re.UNICODE)
cls = lambda: os.system('cls')
print('')
while True:
	full = ''
	line = ' '
	while line != '':
		line = input('»')
		if line != '':
			if not full:
				full = line
			else:
				full += f'\n{line}'
	full = re.sub('[\W_]+', ' ', full.lower(), flags=re.UNICODE)
	cls()
	print(f'\n{full}\n')
