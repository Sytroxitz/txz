import txz

while True:
    text = input("txz >>> ")
    result, error = txz.run('<stdin>', text)
    if error: print(error.as_string())
    else: print(result)