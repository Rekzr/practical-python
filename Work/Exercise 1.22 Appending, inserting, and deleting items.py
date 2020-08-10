symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'

symlist = symbols.split(',')
symlist[1] = 'Beau'
mysyms = []
mysyms.append('GOOG')
##print(mysyms)
##print(symlist)
##print(symlist[-2:])

##symlist[-2:] = mysyms
##print(symlist)

symlist.append('RHT')
symlist.insert(1,'AA')
symlist.remove('MSFT')
symlist.append('YHOO')

print(symlist.index('YHOO'))
print(symlist.count('YHOO'))
symlist.remove('YHOO')
print(symlist.count('YHOO'))