import pickle


def makePairs(ind_words):
    for i in range(len(ind_words) - 1):
        yield (ind_words[i], ind_words[i + 1])


data = open('data.txt', encoding='utf8').read()

ind_words = data.split()
pair = makePairs(ind_words)
word_dict = {}
for word_1, word_2 in pair:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

with open('words_dict.pickle', 'wb') as f:
    pickle.dump(word_dict, f)
with open('bag_of_words.pickle', 'wb') as f:
    pickle.dump(ind_words, f)
