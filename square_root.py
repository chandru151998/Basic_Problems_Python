class SquareRoot:
    @staticmethod
    def newton_sqrt(n):
        approx = 0.5 * n
        better = 0.5 * (approx + n / approx)
        while better != approx:
            approx = better
            better = 0.5 * (approx + n / approx)
        return approx


if __name__ == '__main__':
    num = int(input("Enter a number : "))
    square_root = SquareRoot()
    print(square_root.newton_sqrt(num))
