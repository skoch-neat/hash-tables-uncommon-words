def uncommon_from_sentences(s1, s2):
    word_count = {}

    words_in_sentences = s1.split() + s2.split()

    for word in words_in_sentences:
        word_count[word] = word_count.get(word, 0) + 1

    return [word for word, count in word_count.items() if count == 1]