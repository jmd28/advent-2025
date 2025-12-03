from inp import INPUT

def find_next_digit(bank, digits_remaining):
    # viable digits must come from the start of the bank
    # otherwise there won't be enough to the right to make
    # the n digit number
    viable_digits = bank[:(len(bank) - digits_remaining) + 1]
    best_digit = max(viable_digits)
    digit_index = bank.index(best_digit)
    return best_digit, digit_index

def max_joltage(bank, n_digits):
    result = ""
    digits_remaining = n_digits
    viable_digits = bank
    while digits_remaining > 0:
        best_digit, index = find_next_digit(viable_digits, digits_remaining)
        result += str(best_digit)
        # look east of the returned digit
        viable_digits = viable_digits[index + 1:]
        digits_remaining -= 1
    return int(result)

banks = [list(map(int, bank)) for bank in INPUT.split("\n")]
print(sum(max_joltage(bank, 2) for bank in banks))
print(sum(max_joltage(bank, 12) for bank in banks))
