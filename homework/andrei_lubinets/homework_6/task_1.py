text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")

text = text.split(" ")
new_text = []

for word in text:
    if word.endswith(',') or word.endswith('.'):
        word = word[:-1] + 'ing' + word[-1:]
    else:
        word += 'ing'
    new_text.append(word)
print(' '.join(new_text))
