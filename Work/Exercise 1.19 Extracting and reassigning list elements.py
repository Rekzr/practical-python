symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'

symlist = symbols.split(',')
symlist[1] = 'Beau'
mysyms = []
mysyms.append('GOOG')
print(mysyms)
print(symlist)
print(symlist[-2:])

symlist[-2:] = mysyms
print(symlist)