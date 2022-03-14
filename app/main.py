import os, re
while True:
	print('')
	full = line = '\n'
	while not full.endswith('\n\n'):
		line = input('»')
		full += f'\n{line}'
	os.system('cls')
	print(re.sub('[\W_]+', ' ', full.lower(), flags=re.UNICODE))
