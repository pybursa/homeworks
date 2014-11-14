import collections


def classification(dictionary):
    class_dict = collections.defaultdict(int)
    for value in dictionary.values():
        class_dict[type(value).__name__] += 1
    return dict(class_dict)

print classification({'a': 1, 3: [1,5], 'e': 'abc', '6': []})