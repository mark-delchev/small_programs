class Weather:
    def __init__(self):
        self.ans = ""

    def convert_temperature(self, celsius):
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        self.ans = [kelvin, fahrenheit]
        return self.ans
