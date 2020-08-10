symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'

symlist = symbols.split(',')
##symlist[1] = 'Beau'
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

symlist.sort(reverse=True)

nums = [101, 102, 103]
items = ['spam', symlist, nums]
print(items)
print(items[0])
print(items[0][0])
print(items[1])
print(items[1][0])
print(items[2])
print(items[2][1])