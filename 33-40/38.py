# ----------------
# -- User Input --
# ----------------

fName = input('What\'s Is Your First Name?')
mName = input('What\'s Is Your Middle Name?')
lName = input('What\'s Is Your Last Name?')

fName = fName.strip().capitalize()  #strip and cap.. منشان ازالة الفراغات والحرف الاول يكون كبير
lName = lName.strip().capitalize()  #strip and cap.. منشان ازالة الفراغات والحرف الاول يكون كبير
mName = mName.strip().capitalize()  #strip and cap.. منشان ازالة الفراغات والحرف الاول يكون كبير

print(f"Hello {fName} {mName:.1s} {lName} Happy To See You.")