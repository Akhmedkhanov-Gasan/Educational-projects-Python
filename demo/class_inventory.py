class Inventory:
    # version 0.4
    def __init__(self):
        self._items = {}

    def __str__(self):
        return f'Inventory: {self._items}'

    def __len__(self):
        count = 0
        for value in self._items.values():
            count += value
        return count

    def __contains__(self, item):
        return item in self._items

    def __add__(self, new_item):
        new_inv = Inventory()
        new_list = self._items.copy()
        if isinstance(new_item, str):
            if new_item in new_list:
                new_list[new_item] += 1
            else:
                new_list[new_item] = 1
        elif isinstance(new_item, Inventory):
            for key, value in new_item._items.items():
                if key in new_list:
                    new_list[key] += value
                else:
                    new_list[key] = value
        new_inv._items = new_list
        return new_inv

    def __sub__(self, item):
        new_inv = Inventory()
        new_list = self._items.copy()
        if isinstance(item, str):
            if item not in new_list:
                new_inv._items = new_list
                return new_inv
            if item in new_list and new_list[item] >= 2:
                new_list[item] -= 1
            else:
                new_list.pop(item)
        elif isinstance(item, Inventory):
            for key, value in item._items.items():
                if key not in new_list:
                    continue
                new_element = new_list[key] - value
                if new_element > 0:
                    new_list[key] = new_element
                elif new_element <= 0:
                    new_list.pop(key)
        new_inv._items = new_list
        return new_inv

    def __iadd__(self, other):
        if isinstance(other, str):
            if other in self._items:
                self._items[other] += 1
            else:
                self._items[other] = 1

        elif isinstance(other, Inventory):
            for key, value in other._items.items():
                if key in self._items:
                    self._items[key] += value
                else:
                    self._items[key] = value
        return self

    def __eq__(self, other):
        if not isinstance(other, Inventory):
            return False
        return self._items == other._items

    def __iter__(self):
        for key, value in self._items.items():
            for _ in range(value):
                yield key

    def add(self, item):
        if isinstance(item, str):
            if item in self._items:
                self._items[item] += 1
            else:
                self._items[item] = 1

        elif isinstance(item, Inventory):
            for key, value in item._items.items():
                if key in self._items:
                    self._items[key] += value
                else:
                    self._items[key] = value


inv = Inventory()
inv += "sword"

inv2 = Inventory()
inv2 += "sword"
inv2 += "sword"

print(list(inv - inv2))