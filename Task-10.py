def common_char(word_one, word_two):

    word_one = word_one.lower()
    word_two = word_two.lower()

    common = ''
    for character_one in word_one:

        for character_two in word_two:

            if character_one == character_two:
                common += character_one

       
    common_letters = ''
    for letters in common:
        if not letters in common_letters:
            common_letters += letters + ' '

    print("Common Letters : " + common_letters)
    
    
common_char("house", "computers")