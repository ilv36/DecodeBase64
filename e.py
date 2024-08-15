import base64

encoded_code = ""  # code base64 
decoded_code = base64.b64decode(encoded_code).decode('utf-8')
print(decoded_code)
