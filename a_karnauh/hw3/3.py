input_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quis lorem ut libero malesuada feugiat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum congue leo eget malesuada. Cras ultricies ligula sed magna dictum porta."
def reverse_chars(text):
	changed_text = ""
	word = ""
	for char in text:
		if char != " " and char !="." and char != ",":
			word += char
		else:
			word = word[::-1]
			changed_text += word + char
			word = ""
	return changed_text

def reverse_words(text):
	changed_text = ""
	sentence = []
	word = ""
	for char in text:
		if char != ".":
			word += char
		if char == " ":
			sentence.append(word)
			word = ""
		if char == ".":
			sentence.append(word + " ")
			word = ""
			sentence.reverse()
			changed_text += "".join(sentence)
			changed_text = changed_text.strip() + char + " "
			sentence = []
	return changed_text

def reverse_sentences(text):
	changed_text_list = []
	sentence = ""
	for char in text:
		sentence += char
		if char == ".":
			changed_text_list.append(sentence.strip() + " ")
			sentence = ""
	changed_text_list.reverse()
	return "".join(changed_text_list)

print reverse_sentences(reverse_words(reverse_chars(input_string)))