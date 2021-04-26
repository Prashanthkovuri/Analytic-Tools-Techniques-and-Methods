
import matplotlib.pyplot as plots

file_reader = open("prash22.txt","r")
stringsList = []
for line in file_reader:
  stringsList += line.split()

file_reader.close()


for i in range(len(stringsList)):
    str_val = stringsList[i]
    position = i
    while (position  > 0 and stringsList[position -1] > str_val):
        stringsList[position ], stringsList[position -1] = stringsList[position -1], stringsList[position ]
        position  -= 1
    stringsList[position ] = str_val

print("String After Sorted", stringsList)

print(len(stringsList))

strings_lens = []
for i in range(len(stringsList)):
  strings_lens.append(len(stringsList[i]))

print(strings_lens)



strings_order = [x+1 for x in range(len(stringsList))]

plots.scatter(strings_order, strings_lens)
plots.title('Scatter Plot For Sorting Strings ')
plots.xlabel('length of the String')
plots.ylabel('Sorted String')
plots.show()

