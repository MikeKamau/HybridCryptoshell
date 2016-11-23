FUNCTION
============
This script employs both asymmetric and symmetric encryption to encrypt its traffic.
It initially generates and RSA tunnel(assymetric encryption) and transmits a randomly generated AES key that is then used to encrypt subsequent traffic through symmetric encryption.
Incase you'd wish to use other RSA keys, other than the ones provided in the scripts, you can use the keygen.py script to generate them, just run "python keygen.py".

PREREQUISITES
=============
You should have python 2.7 and the pycrypto 2.6 installed.

MODIFICATIONS
=============
Feel free to fork this script and modify it to your heart's content.

