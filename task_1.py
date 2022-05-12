from arguments import nested_list


class FlatIterator:

    def __init__(self, nested_list):
        self.nested_list = nested_list

    def flat_list(self):
        new_list = []
        _index = 0
        while _index < len(self.nested_list):
            item = self.nested_list[_index]
            if isinstance(item, list):
                item_index = 0
                while item_index < len(item):
                    i = item[item_index]
                    new_list.append(i)
                    item_index += 1
                _index += 1
        return new_list

    def __iter__(self):
        self.new_index = 0
        self.len_new_list = len(self.flat_list())
        return self

    def __next__(self):
        if self.new_index == self.len_new_list:
            raise StopIteration
        else:
            item = self.flat_list()[self.new_index]
            self.new_index += 1
            return item


if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
