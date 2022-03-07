def four_word():

    with open("D:\\Python pgrms\\file\\data.txt", 'r') as f:
        words=f.read().split()
        print(words)
        for word in words:
            if len(word)==4:
                print(word,end=" ,")

print(four_word())