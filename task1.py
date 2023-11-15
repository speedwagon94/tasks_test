def generate_sequence(n):
    result = ""
    for i in range(1, n + 1):
        result += str(i) * i
    return result


def main():
    try:
        n = int(input("Введите количество элементов (n): "))
        if n < 1:
            print("Пожалуйста, введите положительное число.")
        else:
            sequence = generate_sequence(n)
            print("Последовательность:", sequence)
    except ValueError:
        print("Пожалуйста, введите целое число.")


if __name__ == "__main__":
    main()
