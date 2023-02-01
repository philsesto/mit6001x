import re

regex = re.compile(r'b(?=ob)')
print('Number of times bob occurs is: ' + str(len(regex.findall(s))))