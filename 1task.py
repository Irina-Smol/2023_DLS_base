file = open("out.txt", "w")
for i in range(5):
    file.write(str(i))
file.close()

file = open("out.txt", "w")
for i in range(5, 10):
    file.write(str(i))
    
file.close()

# >>> 56789
# при повторном открытии с буковкой 'w'
# file = open("out.txt", "w")
# содержимое файла удаляется и переписывается все по новой
