my_file = open('/home/user/PycharmProjects/Images/filenames.txt', "r")
print(my_file.read())
my_file.close()
my_file = open('/home/user/PycharmProjects/Images/filenames.txt', "r")
print(my_file.readline())
my_file.close()

my_file = open('/home/user/PycharmProjects/Images/filenames.txt', "r")
with open('/home/user/PycharmProjects/Images/filenames.txt', "r") as f:
    for item in my_file:
        my_file.write('/home/user/PycharmProjects/Images/filenames.txt')
        my_file.read()

my_file = []
# lambda exp.
even_no = list(filter(lambda x: (x % 2 == 0), my_file))
print("Even numbers in the list :", even_no)

with open("/home/user/PycharmProjects/Images/filenames.txt", "r") as output:
    for row in my_file:
        output.write(str(row) + '\n')
