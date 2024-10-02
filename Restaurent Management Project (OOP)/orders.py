class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity #jodi item ta alreay cart e thake taile plus hobe oitar sathe
        else:
            self.items[item] = item.quantity # jodi item ta na thake taile just oita add hobe 1 bar

    def remove(self, item): 
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())
    
    def clear(self):
        self.items = {}