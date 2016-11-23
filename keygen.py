from Crypto.PublicKey import RSA

#Generate new key that's 4096 bits long
new_key = RSA.generate(4096)

#Export the key in PEM format
public_key = new_key.publickey().exportKey("PEM")
private_key = new_key.exportKey("PEM")
print private_key
print public_key
