
print('''
=======================================
|               Menu                  |
| 1. Search last name in address book |
| 2. Add person to address book       |
| 3. Quit                             |
=======================================
''')

y = input()
y = int(y)

class newPerson:

        def __init__(self, name, housenumber, road, town, county, postcode, landline, mobile, notes):
            self.name = name
            self.housenumber = housenumber
            self.road = road
            self.town = town
            self.county = county
            self.postcode = postcode
            self.landline = landline
            self.mobile = mobile
            self.notes = notes

        def adressinput(self, name, housenumber, road, town, county, postcode, landline, mobile, notes):


            x = [name, housenumber, road, town, county, postcode, landline, mobile, notes]
            for foo in range(0, 8):
                print(x[foo], ": ")
                x = input()



if y == 1:
        print("test")
elif y == 2:
   newPerson.adressinput()
else:
    quit()








