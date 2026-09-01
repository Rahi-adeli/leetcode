address = "255.100.50.0"

def defangIPaddr(address):

    replacing = address.replace("." , "[.]")

    return replacing


result = defangIPaddr(address)
print (result)