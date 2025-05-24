class Rettangolo:
    def __init__(self, base, altezza, colore):
        self.base = base
        self.altezza = altezza
        self.colore = colore

    def area(self):
        area = self.base * self.altezza
        return area
    def stampa_info(self):
        return "base: " + self.base + ", altezza: " + self.altezza + ", colore: " + self.colore + "area: " + str(self.area())