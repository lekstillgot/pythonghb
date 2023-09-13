numbers = [-1, 2, 3, 4, 5]
print(numbers)
print(numbers[3])
print(numbers[-1])
print(numbers[-2])
print(numbers[1:3])
print(numbers[:3])
print(numbers[1:])
print(numbers[:])
print(numbers[::2])
print(numbers[::-1])


persons = ['john', 'jay', 'joe', 'jack']

# loop person
for person in persons:
    print(person)

    # เพิ่มสมาชิก append()
persons.append('jim')
print(persons)

persons[0] = 'johny'
print(persons)

persons.remove('johny')
print(persons)
persons.pop(1)
print(persons)

print(len(persons))
