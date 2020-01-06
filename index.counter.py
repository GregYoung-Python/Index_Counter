vowels = 0
consonants = 0
punctuations = 0
spaces = 0


for letter in "Hello World! + =":
    if letter.lower() in "aeiou":
        vowels = vowels + 1

    elif letter in '''"!@#$%&()-+={}[]:";',.?/\"''':
            punctuations = punctuations + 1

    elif letter == " ":
                spaces = spaces + 1

    else:
        consonants = consonants + 1

index_total = vowels + consonants + punctuations + spaces
                    
print("There are {} vowels.".format(vowels))
print("There are {} punctuations.".format(punctuations))
print("There are {} spaces.".format(spaces))
print("There are {} consonants.".format(consonants))
print("There are {} total indexes in this paragraph.".format(index_total))
