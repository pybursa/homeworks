__author__ = 'andrey'

text = "Cras ultricies ligula sed magna dictum porta. Vivamus magna justo, lacinia eget consectetur sed, convallis" \
       " at tellus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec " \
       "velit neque, auctor sit amet aliquam vel, ullamcorper sit amet ligula. Lorem ipsum dolor sit amet, " \
       "consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor " \
       "sit amet, consectetur adipiscing elit. Curabitur aliquet quam id dui posuere blandit. Quisque velit nisi," \
       " pretium ut lacinia in, elementum id enim. Lorem ipsum dolor sit amet, consectetur adipiscing elit. " \
       "Sed porttitor lectus nibh."

volwes = "A, E, I, O, U, Y"

count = 0
for i in range(len(text)):
    if text[i] in volwes.lower():
        if text[i - 1] is not volwes.lower() and text[i + 1] is not volwes.lower() and text[i - 1] is not " " \
                and text[i + 1] is not " ":
            print text[i]
            count += 1
print count
