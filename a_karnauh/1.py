input_string = "Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada."
vowels = "aeiouy"
input_string.lower()
count = 0
max_count = 0
for char in input_string:
	count += vowels.count(char)
	if max_count < count:
		max_count = count
	if char == " ":
		count = 0
print max_count