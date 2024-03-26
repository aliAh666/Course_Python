# --------------------
# --  Control Flow  --
# -- If, Elif, Else --
# -- Make Decisions --
# --------------------

uName = "Osama"
# uCountry = "Kuwait"
uCountry = "Syria"
cName = "Python Course"
cPrice = 100

if uCountry == "Egypt":

  print(f"The Orginal Course \"{cName}\" Price Is: ${cPrice}")
  print(f"Hello {uName} Because You Are From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 80}")

elif uCountry == "KSA":
  print(f"The Orginal Course \"{cName}\" Price Is: ${cPrice}")
  print(f"Hello {uName} Because You Are From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 60}")

elif uCountry == "Kuwait":
  print(f"The Orginal Course \"{cName}\" Price Is: ${cPrice}")
  print(f"Hello {uName} Because You Are From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 50}")

else:
  print(f"The Orginal Course \"{cName}\" Price Is: ${cPrice}")
  print(f"Hello {uName} Because You Are From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 30}")