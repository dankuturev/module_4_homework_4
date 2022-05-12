from arguments import nested_list
from iteration_utilities import deepflatten


def flat_generator(input_list):
    new_list = list(deepflatten(input_list))
    for i in new_list:
        yield i


if __name__ == '__main__':
    for item in flat_generator(nested_list):
        print(item)
    flat_list = [item for item in flat_generator(nested_list)]
    print(flat_list)










