import helper

def parse_content(content):
    words = {}
    lines = content.split('\n')
    for line in lines[0:10]:
        split = line.split()
        words[split[0]] = int(split[1])
    return words

def add(word, original_word, freq, _dict):
    if len(word) == 0:
        #finished
        if("words" in _dict):
            _dict["words"].append({
                "original_word": original_word,
                "freq": freq
            })
        else:
            _dict["words"] = []
            _dict["words"].append({
                "original_word": original_word,
                "freq": freq
            })
    else:
        #proceed
        char0 = word[0]
        key = helper.get_key_for_char(char0)
        if(key in _dict):
            child = _dict.get(key)
        else:
            child = {}
            _dict[key] = child
        
        add(word[1::], original_word, freq, child)
        

def make_tree(words):
    trie = {}
    print(words)
    for word, freq in words.items():
        add(word, word, freq, trie)
    return trie

def words_in(tree):
    found = []
    def recurse(_tree):
        for key in _tree:
            if key == "words":
                for e in _tree["words"]:
                    found.append((e["original_word"], e["freq"]))
            else:            
                recurse(_tree[key]) 
    recurse(tree)
    return found

def predict(tree, numbers):
    if len(numbers) == 0:
        return words_in(tree)
    else:
        key0 = numbers[0]
        if key0 in tree:
            return predict(tree[key0], numbers[1::])
        else:
            return words_in(tree)


if __name__ == '__main__':
    content = helper.read_content(filename='nk.txt')
    words = parse_content(content)
    tree = make_tree(words)
    print(tree)
    
    
    while True:
        numbers = helper.ask_for_numbers()
        predictions = predict(tree, numbers)
        print(predictions)

        if not predictions:
            print('No words were found that match those numbers. :(')
        else:
            for prediction, frequency in predictions[:4]:
                print(prediction, frequency)

        response = input('Want to go again? [y/N] ')
        again = response and response[0] in ('y', 'Y')
        if not again:
            break
