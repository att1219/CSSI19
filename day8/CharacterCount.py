def CharacterCount (search):
    word = raw_input("Enter a word")
    d = {}
    for i in word: 
        if d.has.key(i):
            d[i]=d[i]+1
        else:
            d[i]=1           
print CharacterCount(search)