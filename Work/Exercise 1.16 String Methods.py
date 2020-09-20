symbols = 'AAPL,IBM,MSFT,THOO,SCO'
name = '         IBM     \n'

print(symbols.lower())
print(symbols.find(','))
print('!'.join(symbols))
print(symbols.split())
print(symbols.split(','))
print(symbols[13:17])
print(symbols.replace('SCO','DOA'))
print(name.strip())