import datetime
from time import sleep

# a+ as second argument lets you append to a string
for i in range(5):
    file_builder = open("logger.txt", "a+")
    file_builder.write(f'{datetime.datetime.now()}\n')
    file_builder.close()

    print("file created")

    sleep(1)
