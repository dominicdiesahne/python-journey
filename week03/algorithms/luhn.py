# Luhn Algorithm from FreeCodeCamp.org
def verify_card_number(card_number):
    digits = card_number.replace('-', '').replace(' ', '')

    total = 0
    for index, char in enumerate(reversed(digits)):
        digit = int(char)
        if index % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    return 'VALID!' if total % 10 == 0 else 'INVALID!'