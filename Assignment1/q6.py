import hashlib
import base64

def generate_check(sentence):

    result = hashlib.md5(sentence.encode())
    print("The hex equivalent of hash is : ", end ="") 
    return result.hexdigest()

#st = generate_check('GeeksforGeeks')
#print(st)

