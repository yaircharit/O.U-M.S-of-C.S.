# Created By Yair Charit 207282955 #

words = ['adopt','bake','beam','cook','time','grill', 'waved','hire']
res =  [word if word[-2:].lower() == 'ed' else f'{word}d' if word[-1].lower() == 'e' else f'{word}ed' for word in words]
print(res)