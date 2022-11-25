

def short_word(n: str) -> int:
    stroka = n.replace(",", "")
    #print(stroka) -> hello world lo love story market
    spl = stroka.split()
    #print(spl)-> ['hello', 'world', 'lo', 'love', 'storry', 'market']
    sum = [len(i) for i in spl]
    #print(sum)  -> [5, 5, 2, 4, 6, 6]
    return min(sum) #-> 2

print(short_word("hello, world, lo, love, story, market"))
        
    
    
    
    









