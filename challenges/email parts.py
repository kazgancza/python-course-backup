def getMailParts(email):
    atPosition = email.find("@")
    if atPosition != -1:
        user = email[0 : atPosition]
    else: return None

    dotPosition = email.find(".")
    if dotPosition != -1:
        domainName = email[atPosition + 1 : dotPosition]
    else: return None

    domainExt = email[dotPosition + 1:]

    result = {
        "user": user,
        "domainName": domainName,
        "domainExt": domainExt
    }

    return result

print(getMailParts("ola@domena.eu"))