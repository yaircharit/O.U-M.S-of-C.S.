# Created By Yair Charit 207282955 #

words = ['adopt','bake','beam','cook','time','grill', 'waved','hire']
words = [word.lower() for word in words]
res =  [word if word[-2:] == 'ed' else f'{word}d' if word[-1] == 'e' else f'{word}ed' for word in words]
print(res)