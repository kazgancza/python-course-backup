def validateEmail(mail):
    atIndex = mail.find("@")
    dotIndex = mail[atIndex:len(mail)].find(".")
    if atIndex != -1 and dotIndex != -1:
        return True
    else: return False

print(validateEmail("asia@example.com"))
print(validateEmail("karol@domena"))
print(validateEmail("user.com"))
