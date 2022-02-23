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
print(" ")       # this command is given just to maintain space in the output
print('atomic_name ', 'atomic_number ', 'atomic_weight')
for atom in atoms:
    print(atom[0], (12-len(atom[0]))*" ", atom[1], (14-len(atom[1]))*" ", atom[2])
input()

