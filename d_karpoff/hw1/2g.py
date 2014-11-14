text = str(raw_input("Input text:  "))
gl = "AaEeIiOoUu"
gl = sum(1 for t in text if t in gl)
print gl
