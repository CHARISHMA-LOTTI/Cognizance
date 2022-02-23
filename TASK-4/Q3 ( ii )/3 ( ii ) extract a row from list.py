atoms = [
    ['A00', 'A01', 'A02'],
    ['A10', 'A11', 'A12'],
    ['A20', 'A21', 'A22']
]
print("This list contains the atomic number and weight of an atom")
for r in range(3):
    atoms[r][0] = input('Enter name of atom : ')
    atoms[r][1] = input('Enter its atomic number : ')
    atoms[r][2] = input('Enter its atomic weight : ')
print('atomic_name ', 'atomic_number ', 'atomic_weight')
for atom in atoms:
    print(atom[0], (12-len(atom[0]))*" ", atom[1], (14-len(atom[1]))*" ", atom[2])
print("here is the list ")
row = input("which row do you want to extract ?")
r = int(row)
if r < 3:
    print(atoms[r-1][0], atoms[r-1][1], atoms[r-1][2])
else:
    print("row does not exist.there are only 3 rows")
input()

