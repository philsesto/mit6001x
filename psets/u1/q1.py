import re

regex = re.compile(r'a|e|i|o|u')
print('Number of vowels: ' + str(len(regex.findall(s))))