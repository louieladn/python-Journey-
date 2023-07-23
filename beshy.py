# user promt
beshy = input("Put beshy words: ")

print("your beshy: ", end="" )

for word in beshy: 
    if word.isspace():
        print("🤸 " , end="")

    else: 
        print(word, end="")
print()