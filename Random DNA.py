from random import randint

length = int(input("Input the length of the random DNA: "))
f = open("DNA.txt", "w")
possibilities = {
    0:"A",
    1:"T",
    2:"C",
    3:"G"
}
for i in range(length):
    f.write(possibilities[randint(0,3)])
