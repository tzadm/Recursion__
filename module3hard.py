def calculate_structure_sum(*args):
    sum = 0
    for thing in args:
        if isinstance(thing, list):
            for elem in thing:
                sum += calculate_structure_sum(elem)
        if isinstance(thing, tuple):
            for elem in thing:
                sum += calculate_structure_sum(elem)
        if isinstance(thing, set):
            for elem in thing:
                sum += calculate_structure_sum(elem)
        if isinstance(thing, dict):
            for key, value in thing.items():
                sum += calculate_structure_sum(key, value)
        if isinstance(thing, str):
            sum += len(thing)
        if isinstance(thing, int):
            sum += thing
    return sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
