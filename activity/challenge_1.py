def uncommon_from_sentences(sentences):
    word_count = {}
    
    words_in_sentences = [word for sentence in sentences for word in sentence.split()]

    for word in words_in_sentences:
        word_count[word] = word_count.get(word, 0) + 1

    return [word for word, count in word_count.items() if count == 1]