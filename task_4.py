from arguments import nested_list


def flat_generator(input_list):
    for item in input_list:
        if isinstance(item, list):
            yield from flat_generator(item)
        else:
            yield item


if __name__ == '__main__':
    for item in flat_generator(nested_list):
        print(item)
    flat_list = [item for item in flat_generator(nested_list)]
    print(flat_list)
