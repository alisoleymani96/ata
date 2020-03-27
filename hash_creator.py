import hashlib


def hash_creator(*numbers):

    container_dict = {}

    for number in numbers:
        hashed_number_object = hashlib.sha256(str(number).encode())
        container_dict[number] = hashed_number_object.hexdigest()

    return container_dict


tuple_of_random_numbers = (1205, 5482, 3542, 1256, 0000, 4168, 9999)

results = hash_creator(*tuple_of_random_numbers)
print(results)
