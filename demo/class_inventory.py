class Inventory:
    def __init__(self):
        self._items = []

    def __str__(self):
        return f'Inventory: {self._items}'

    def __len__(self):
        return len(self._items)


    def __contains__(self, item):
        return item in self._items

    def __add__(self, new_item):
        new_inv = Inventory()
        new_list = self._items.copy()
        new_list.append(new_item)
        new_inv._items = new_list
        return new_inv

    def __iadd__(self, other):
        self._items.append(other)
        return self

    def __eq__(self, other):
        if not isinstance(other, Inventory):
            return False
        return self._items == other._items

    def __iter__(self):
        return iter(self._items)

    def add(self, item):
        self._items.append(item)


inv = Inventory()
inv.add("sword")
inv.add("shield")

print(inv)              # Inventory: ['sword', 'shield']
print(len(inv))         # 2
print("sword" in inv)   # True

inv2 = inv + "potion"

print(inv)              # старый не изменился
print(inv2)             # новый с potion

inv += "ring"
print(inv)

for item in inv:
    print(item)

print(inv == inv2)      # False