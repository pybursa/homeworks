def aaa(text):
    vowels_and_punct = ('a', 'e', 'i', 'o', 'u', 'y', ' ', '.', ',')
    total = 0
    for number, letter in enumerate(text):
        try:
            if letter == 'a' and text[number - 1] not in vowels_and_punct \
               and text[number + 1] not in vowels_and_punct:
                total += 1
        except IndexError:
            pass
    return total

text = '''
Cras ultricies ligula sed magna dictum porta. Vivamus magna justo, lacinia eget consectetur sed, 
convallis at tellus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere 
cubilia Curae; Donec velit neque, auctor sit amet aliquam vel, ullamcorper sit amet ligula. 
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, 
consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Curabitur aliquet quam id dui posuere blandit. Quisque velit nisi, pretium ut lacinia in, 
elementum id enim. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed porttitor 
lectus nibh.
'''
print aaa(text)
