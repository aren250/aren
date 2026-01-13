def to_spongecase(text):
    """
    Converts input text into spongecase (alternating uppercase and lowercase letters).
    Non-alphabetic characters remain unchanged.
    """
    spongecase_text = []
    
    i = 0
    for char in text:
        if char.isalpha():
           
            if i % 2 == 0:
                spongecase_text.append(char.lower())
            else:
                spongecase_text.append(char.upper())
            i += 1
        else:
            
            spongecase_text.append(char)

    return "".join(spongecase_text)

# Example Usage:
input_string = "Hello World! This is a test."
output_string = to_spongecase(input_string)
print(f"Original: {input_string}")
print(f"Spongecase: {output_string}")

input_string_two = "Spongecase is the best casing!"
output_string_two = to_spongecase(input_string_two)
print(f"Original: {input_string_two}")
print(f"Spongecase: {output_string_two}")