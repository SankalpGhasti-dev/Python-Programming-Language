
letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>", "Sankalp").replace("<|Date|>", "6th June 2025"))

# In first step <|Name|> will be replaced by "Sankalp" in that string and then in this string <|Date|> will be replaced by "6th June 2025".
# This method is called Chained Method.

