age = 36
txt = f"My name is John, I am {age}"
print(txt)    """
              To specify a string as an f-string,
              simply put an f in front of the string literal,
              and add curly brackets {} as placeholders for variables and other operations.
              """
price = 59
txt = f"The price is {price} dollars"
print(txt)  #placeholder can include variables, operations, functions, and modifiers

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt) # to display the price with 2 decimals

txt = f"The price is {20 * 59} dollars"
print(txt) #math operation in the placeholder
                    
