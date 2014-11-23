text = "Cras ultricies ligula sed magna dictum porta. Vivamus magna justo, lacinia eget consectetur sed, convallis at tellus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec velit neque, auctor sit amet aliquam vel, ullamcorper sit amet ligula. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur aliquet quam id dui posuere blandit. Quisque velit nisi, pretium ut lacinia in, elementum id enim. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed porttitor lectus nibh."

def is_vowel(char):
	if "aeiouy".count(char):
		return True
	return False

def is_consonant(char):
	if "aeiouy".count(char) or "., ".count(char):
		return False
	return True

count = 0
for i in range(len(text)-1):
	if is_vowel(text[i]) and is_consonant(text[i-1]) and is_consonant(text[i+1]):
		count += 1
print count


