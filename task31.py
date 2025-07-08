def count_letters(text: str) -> dict[str, int]:
    result = {}
    for ch in text:
        if ch.isalpha(): 
            if ch in result:
                result[ch] += 1
            else:
                result[ch] = 1
    return result

text = "assalomu alaykum"
print(count_letters(text))
