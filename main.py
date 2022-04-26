print("Ievadi divu kubu šķautnes izmeri: ")
a = int(input('Pirmais kubs: '))
b = int(input('Otrais kubs: '))
if a == b:
  print("Kubi ir vienādi")
elif a > b:
  c = a*a*a
  print("Pirma kuba ir vislielākais tilpums: ", c)
else:
  c = b*b*b
  print("Otra kuba ir vislielākais tilpums: ", c)