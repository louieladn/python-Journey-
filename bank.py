# promt user 
msg = input("Greeting: ").strip().lower()
# statement for hello
    # if greetings is hello 0$
    # if greetings start with h 20$
    # if greetings doesnt compliment above statement 100$
if msg == "hello":
    print("$0")
elif msg[0] == "h":
    print("$20")
else:
    print("$100")