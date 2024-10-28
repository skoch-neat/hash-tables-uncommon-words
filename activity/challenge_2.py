def uncommon_from_sentences(sentences):
    word_count = {}

    for sentence in sentences:
        words_in_sentence = set(sentence.split())
        for word in words_in_sentence:
            word_count[word] = word_count.get(word, 0) + 1

    return [word for word, count in word_count.items() if count == 1]