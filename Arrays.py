def main():
    print("Hexadecimal Converter: Type a hex number:")

    while True:
        hex_input = input("Enter a hexadecimal number:").strip().upper()

        if hex_input == "STOP":
            print("Goodbye")
            break

        if len(hex_input) > 2 or not all(c in "0123456789ABCDEF" for c in hex_input):
            print("Invalid input. Try again")
            continue

        decimal_value = int(hex_input, 16)
        binary_value = bin(decimal_value)[2:] 

        print(f"{hex_input} -> Decimal: {decimal_value}, Binary: {binary_value}")

if __name__ == "__main__":
    main()































