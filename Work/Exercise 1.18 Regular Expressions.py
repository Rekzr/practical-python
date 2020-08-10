text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'
import re
##re.findall(r'\d+/\d+/\d+', text)
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

s = 'hello world'
#print(dir(s))
#print(help(s.upper))