def cleanText(text):
    swearWords = ["JavaScript", "java", "php", "html", "css"]
    for i in swearWords:
        wordPlace = text.find(i)
        print(wordPlace)
        if wordPlace != -1:
            word = text[wordPlace : wordPlace + len(i)]
        else: continue
        wordCensoured = "*" * len(word)
        text = text.replace(word, wordCensoured)
    return text

example = "Programowanie zacząłem z językiem php, następnie poznałem: html i css, ale obecnie skupiam się na JavaScript"

print(cleanText(example))
