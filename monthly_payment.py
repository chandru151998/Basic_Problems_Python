class MonthlyPayment:
    @staticmethod
    def monthly_payment(y, p, r1):
        n = 12 * y
        r = float(r1 / (12 * 100))
        denominator = float(1 - (pow((1 + r), (-n))))
        numerator = float(p * r)
        payment = float(numerator / denominator)
        return payment


if __name__ == '__main__':
    u = MonthlyPayment()
    P1 = float(input("Principal Loan Amount : "))
    Y1 = float(input("Years : "))
    R1 = float(input("Monthly Cent Interest : "))
    res = u.monthly_payment(Y1, P1, R1)
    print("Total Amount: ", res)
