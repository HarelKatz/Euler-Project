import itertools

f = open("042_words.txt", "r").read()
common_words = f.replace('"', "").split(",")
x = []
for word in common_words:
    temp = 0
    for letter in word:
        temp += ord(letter) - 64
    # print(temp)

    for i in itertools.count():

        # print("t, "+str(i*(i+1)/2))
        if temp == i * (i + 1) / 2:

            # print(word, temp, i * (i + 1) / 2, i)
            x.append(word)
            break

        elif temp < i * (i + 1) / 2:

            break

print(x)
print(len(x))
