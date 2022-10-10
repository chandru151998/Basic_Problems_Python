class Temperature:
    @staticmethod
    def convert_to_fahrenheit(temp):
        result = float((9 * temp) / 5 + 32)
        return result

    @staticmethod
    def convert_to_celsius(temp):
        result = float((temp - 32) * 5 / 9)
        return result


if __name__ == '__main__':
    input_temp = float(input("Input temperature in celsius: "))
    temp1 = Temperature()
    print(temp1.convert_to_fahrenheit(input_temp))

    input_temp = float(input("Input temperature in fahrenheit: "))
    temp1 = Temperature()
    print(temp1.convert_to_celsius(input_temp))
