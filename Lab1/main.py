import re
import statistics


def sentences_count():
    file = open('text.txt', 'r')
    text = file.read()
    sentences = text.split('.')
    while "" in set(sentences):
        sentences.remove("")
    print("Number of sentences:", len(sentences))


def words_count():
    print("Text:\n")
    frequency = {}
    file = open('text.txt', 'r')
    for sentence in file:
        print(sentence)
    file = open('text.txt', 'r')
    text_string = file.read().lower()
    match_pattern = re.findall(r'\b[a-z]{2,15}\b', text_string)
    for word in match_pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1
    frequency_list = frequency.keys()
    for words in frequency_list:
        print(words, frequency[words])


def open_file():
    f = open('text.txt', 'r')
    f = f.read().lower()
    text = f.replace('?', '.').replace('!', '.').replace('...', '.')
    return text


def average_count_words():
    text = open_file()
    sentences = text.split(' ')
    count = text.count('.')
    print("Average count words: ", round(len(sentences) / count))


def median_count_words():
    text = open_file()
    print("Median count words: ", round(statistics.median([len(sentence.split()) for sentence in text.split(".")])))


def top_k(ngram_dict, k):
    ngram_dict = {k: ngram_dict[k] for k in sorted(ngram_dict, key=ngram_dict.get, reverse=True)}
    tmp_k = 0
    for words in ngram_dict:
        if tmp_k < k:
            print(words, ngram_dict[words])
            tmp_k += 1


def n_gram(n, k):
    words_dict = {}
    ngram_dict = {}
    print("n =", n, "k =", k)
    text = open_file()
    text = text.replace('.', ' ').replace(',', ' ').replace(':', ' ').replace('-', ' ')
    split_text = text.split()
    for word in split_text:
        count = words_dict.get(word, 0)
        words_dict[word] = count + 1
    for word in words_dict.keys():
        if len(word) >= n:
            tmp_word = word
            count = 0
            end = n
            for i in range(len(word) - end + 1):
                ngram = tmp_word[count:end]
                if ngram in ngram_dict.keys():
                    ngram_dict[ngram] += words_dict[word]
                else:
                    ngram_dict[ngram] = words_dict[word]
                count += 1
                end += 1
    top_k(ngram_dict, k)


def input_values():
    print("Default values N = 4 and K = 10? (y/n)")
    check = input()
    if check == 'y':
        n = 4
        k = 10
        n_gram(n, k)
    else:
        n = input("Enter n: ")
        k = input("Enter k: ")
        n = int(n)
        k = int(k)
        n_gram(n, k)


def main():
    words_count()
    sentences_count()
    average_count_words()
    median_count_words()
    input_values()


if __name__ == "__main__":
    main()
