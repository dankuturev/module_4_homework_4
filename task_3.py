from arguments import nested_list


def flat_iterator(input_list):
    stack = [iter(input_list)]
    new_list = []
    while stack:
        i = stack.pop()
        try:
            while True:
                data = next(i)
                if isinstance(data, list):
                    stack.append(i)
                    i = iter(data)
                else:
                    new_list.append(data)
        except StopIteration:
            pass
    return new_list


for item in flat_iterator(nested_list):
    print(item)
