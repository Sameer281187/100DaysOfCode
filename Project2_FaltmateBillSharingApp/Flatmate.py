class Flatmate:
    def __init__(self, days_in_house, name):
        self.name = name
        self.days_in_house = days_in_house

    def calculate_share_amount(self, bill, other_flatmate):
        weight = self.days_in_house / (self.days_in_house + other_flatmate.days_in_house)
        return round(weight * bill.amount, 2)