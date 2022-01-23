english_words_small = set((
    "open",
    "peon",
    "nope",
    "stone",
    "notes",
    "onset",
    "tones",
    "cone",
    "pots",
    "post",
    "stop",
    "opts",
    "tops",
))

def get_canon(w):
    return "".join(sorted(w))
        
def find_anagrams(letters, words):
    hash = {}
    for word in words:
        canon = get_canon(word)
        if(canon in hash):
            hash[canon].add(word)
        else:
            hash[canon] = set()
            hash[canon].add(word)
    return hash.get(get_canon(letters), set())
    
    
if __name__ == '__main__':
    print(find_anagrams("eston", english_words_small))

