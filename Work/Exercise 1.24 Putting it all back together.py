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

symlist.sort()
print(symlist)

a = ','.join(symlist)
print(a)

b = ':'.join(symlist)
print(b)

c = ''.join(symlist)
print(c)