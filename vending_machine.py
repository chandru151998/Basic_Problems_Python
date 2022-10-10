class VendingMachine:
    @staticmethod
    def vending_machine(amount):
        notes = [1000, 500, 200, 100, 50, 10, 5, 2, 1]
        note_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        print("Your Currency Count is given Below: ")
        for i, j in zip(notes, note_counter):
            if amount >= i:
                j = amount // i
                amount = amount - j * i
                print(i, "  : ", j)


if __name__ == '__main__':
    vm = VendingMachine()
    amount1 = int(input("Enter the amount in Rs:"))
    a = list()
    a = a.append(vm.vending_machine(amount1))
    print(a)
