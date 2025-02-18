def count_world_occurrences(sentence):

    worlds = sentence.split()

    word_count = {}

    for word in words:

        word = word.lower()

        if word in word_count:
            word_count[word] += 1
    else:
                word_count[word] = 1

    returnword_count

    sentence = input("enter a sentence: ")

    word_count = count_word_occurrences(sentence)

    print("word occurrences:")
    for word, count in word_count items():
        print(f"'{word}':{count}")
