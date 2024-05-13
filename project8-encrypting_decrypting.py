import base64
# import maskpass

# secret = maskpass.askpass(mask="")
en_de = input("please enter your choice e for encrypt , d for decode \t")
secret = input("please enter the password \t ")

if en_de == "e":
    encode = base64.b64encode(secret.encode("utf-8"))
    print("encrypted : ", encode)
else:
    encode = base64.b64encode(secret.encode("utf-8"))
    decode = base64.b64decode(encode.decode("utf-8"))
    print("decrypted : ", decode)
