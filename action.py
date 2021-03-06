class Action:
    instances = []

    def __init__(self, action):
        self.name = action[0]
        self.price = float(action[1])
        self.profit_per_cent = float(action[2])
        self.profit = (self.price * self.profit_per_cent) / 100
        self.instances.append(self)

    def convert_to_cents(self):
        self.price = int(self.price * 100)
        self.profit = int(self.profit * 100)
        return self

    def convert_to_usd(self):
        self.price = self.price / 100
        self.profit = self.profit / 100
        return self

    def __repr__(self):
        return f'Nom de l\'action: {self.name} - ' \
               f'Prix d\'achat: {self.price} - ' \
               f'Benefice en %: {self.profit_per_cent} - ' \
               f'Benefice apres deux ans: {self.profit}\n'
