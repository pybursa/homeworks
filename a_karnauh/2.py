input_string = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada."
word = ""
max_word = []
max_length = 0
for char in input_string:
	if char != " " and char !=".":
		word += char
	else:
		if max_length <= len(word):
			max_length = len(word)
			max_word.append(word)
		word = ""
for i in max_word:
	if len(i) == max_length:
		print i
	





