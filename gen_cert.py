#! /usr/bin/env python3

from mitmproxy.certs import CertStore
import OpenSSL
import os

CA_DIR = './cert'

if not os.path.exists(CA_DIR):
    os.makedirs(CA_DIR)

certstore = CertStore.from_store(CA_DIR, 'myca')

cert, pkey, ca_path = certstore.get_cert(b'music.163.com', [b'music.163.com'])

with open(os.path.join(CA_DIR, 'music.163.com.cert.pem'), 'wb') as f:
    f.write(cert.to_pem())

with open(os.path.join(CA_DIR, 'music.163.com.key.pem'), 'wb') as f:
    f.write(OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, pkey))

print("Success!!")
