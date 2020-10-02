serial = input("Enter serial: ")
modified = ""
for c in serial:
    if c != ' ':
        modified += c
    else:
        pass

print(modified)
input("Press Enter to exit")