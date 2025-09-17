import base64
txt = "Hello$World"
txt_bytes = txt.encode("utf-8")
print(txt_bytes)
base64_bytes = base64.b64encode(txt_bytes)
print(base64_bytes)
base64_string = base64_bytes.decode("utf-8")
print(base64_string)