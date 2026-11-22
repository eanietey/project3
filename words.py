import numpy as np

def num_letters(num_rows, num_columns):
    return 2*(num_rows-2)+(num_columns*2)
        
assert num_letters(3, 4) == 10
assert num_letters(6, 7) == 22
assert num_letters(6, 4) == 16
assert num_letters(4, 4) == 12
assert num_letters(13, 4) == 30

print("done")

data = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding = 'utf8')

words = []
num_rows, num_columns = data.shape

for f in range(num_columns):
    words.append(str(data[0,f]))

for s in range(1,num_rows):
    words.append(str(data[s,num_columns-1]))

for t in range(2, num_columns):
    words.append(str(data[num_rows-1, -t]))

for fo in range(0,num_rows):
    words.append(str(data[-fo,0]))

print(words)

#assert len(words) == num_letters(num_rows, num_columns)

data = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding = 'utf8')

letters=[]
words1=[]
for f in range(num_columns):
    letters.append(str(data[0,f]))

for s in range(1,num_rows):
    letters.append(str(data[s,num_columns-1]))

for t in range(2, num_columns):
    letters.append(str(data[num_rows-1, -t]))

for fo in range(1,num_rows):
    letters.append(str(data[-fo,0]))

for i in range(len(letters)-1):
    word=letters[i]+letters[i+1]
    words1.append(word)

last_letter = words[-1]+words[0]
words1.append(str(last_letter))

print(words1)
