import csv

f = open('followers.csv', 'r', encoding='utf-8')
reader = csv.reader(f)
for row in reader:
    username = row[1]
    print(username)
    with open('my_followers.txt', 'a', encoding='utf-8') as f:
        f.write(username + '\n')



