def salutation(nom, age):
    return f"Bonjour '{nom}', vous avez actuellement {age} an{'s' if age != '1' else ''}."# on peut dire 1 ans?

# test
if __name__ == "__main__":
    result1 = salutation('mohamed', '21')
    print(result1)
  
    result2 = salutation('gamin', '1')
    print(result2)
