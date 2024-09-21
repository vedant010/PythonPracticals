def check_validity(text: str):
    bracket_counts = {'(': 0, ')': 0, '{': 0, '}': 0, '[': 0, ']': 0, '<': 0, '>': 0}

    for char in text:
        if char in bracket_counts:
            bracket_counts[char] += 1

    for opening, closing in [('(', ')'), ('{', '}'), ('[', ']'), ('<', '>')]:
        if bracket_counts[opening] != bracket_counts[closing]:
            return "Invalid: mismatched brackets"

    return "Valid"

def get_valid_invalid_text_count(texts):
    valid_count = 0
    invalid_count = 0

    for item in texts:
        if isinstance(item, str):
            result = check_validity(item)
            if result == "Valid":
                valid_count += 1
            else:
                invalid_count += 1

    return (valid_count, invalid_count)

texts = ['[{(', [45, ("()"), ]]
print(get_valid_invalid_text_count(texts))
