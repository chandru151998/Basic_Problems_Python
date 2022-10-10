def decimal_to_binary(num):
    if num >= 1:
        decimal_to_binary(num // 2)
    print(num % 2, end='')


if __name__ == '__main__':
    dec_val = int(input("Enter a number : "))

    decimal_to_binary(dec_val)
