f = open("math-class.in", "r")
toEvaluate = f.readline().split(" ")
f.close()
f = open("math-class.out", "w")

if toEvaluate[0] == "add":
    f.write(str(abs(int(toEvaluate[1]) + int(toEvaluate[2]))) + "\n")
else:
    f.write(str(abs(int(toEvaluate[1]) - int(toEvaluate[2]))) + "\n")
f.flush()
f.close()
