from time import sleep 

count_to = 3

for count in range(1, count_to):
    print(count, end='', flush=True)
    for x in range(3):
        print('.', end='', flush=True)
        sleep(1)
    print('.', flush=True)

print("{count_to}!".format(count_to=count_to))    

#We could write our output to S3 here as well, or anywhere, if we want to store it
