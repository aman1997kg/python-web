def palindrom_check(word):
    word = str(input())
    a = word[::-1]
    if word == a:
      print(" Это палиндром!")
    else:
      print("Это не палиндром!")
palindrom_check('bob')

