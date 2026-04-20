class Inventory:
    def __init__(self):
        self._items = {}

    def __str__(self):
        return f'Inventory: {self._items}'

    def __len__(self):
        count = 0
        for value in self._items.values():
            count += value
        return count

    # def __contains__(self, item):
    #     return item in self._items

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

    # def __iadd__(self, other):
    #     self._items.append(other)
    #     return self
    #
    # def __eq__(self, other):
    #     if not isinstance(other, Inventory):
    #         return False
    #     return self._items == other._items

    def __iter__(self):
        # return iter(self._items.items())
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
inv.add("sword")
inv.add("shield")


inv2 = inv + "potion"

inv.add(inv2)

