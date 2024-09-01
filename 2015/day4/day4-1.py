import hashlib

input = open('input.txt', 'r').readlines()[0].rstrip()
num = 1

while True:
    key = input + str(num)
    hash = hashlib.md5(key.encode('utf-8')).hexdigest()
    print(hash)

    if hash[:5] == '00000':
        print('num: ' + str(num))
        break

    num += 1
