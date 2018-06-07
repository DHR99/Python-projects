def definition2():
    w = input("Enter a word: ").lower()
    try:
        return data[w]
    
    except KeyError:
        if w.title() in data:
            return data[w.title()]
        else:
            print("This word is not in the dictionary")
            proposed_w = get_close_matches(w, data.keys(), n = 1, cutoff = 0.8)
            if len(proposed_w) > 0:
                propose = input("Maybe you meant {}, if yes press Y, if no press N".format(proposed_w[0]))
                if propose == 'Y':
                    return data[proposed_w[0]]
                elif propose == 'N':
                    definition()
                else:
                    print("We dont understand your query")
            else:
                print("This word does not exists")
