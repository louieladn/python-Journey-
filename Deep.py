# make prompt to the user
msg = input("What is the Answer to the Great Question og Life, the Univerese, and Everything?")

if msg.strip() == "42" or msg.strip().lower() == "forty-two" or msg.strip().lower() == "forty two":
    print("Yes")
else:
    print("that would not be the answer to the question of life")