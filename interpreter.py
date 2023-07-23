# promt in the UI
x,y,z = input("Experssion: ").split(" ")
x = float(x)
z = float(z)
# statement note : the x and z are integer and z is operation 
if y == "+":
    answer = x + z
elif y == "-":
    answer = x - z
elif y == "/":
    answer = x / z
elif y == "*":
    answer = x * z
print(answer)