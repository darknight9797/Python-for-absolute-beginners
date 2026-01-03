_string = "North Dakota"

print(_string.rjust(17))

print(_string.ljust(17,"*"))

centre_plus = _string.center(16,"+")
print(centre_plus)

print(_string.lstrip("North"))

print(centre_plus.rstrip("+"))

print(centre_plus.strip("+"))

print(_string.replace("North","South"))