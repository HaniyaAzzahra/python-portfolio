# questions link https://datalemur.com/questions/python-base-13-conversion



# 1ST APPROACH - string based
def convertToBase13(num):
  if num == 0 :
    return "0"
    
  # digits for base 13
  base13digits = "0123456789ABC"
  digits = ""
  positive = abs(num)
  
  # the core logic
  while positive>0:
    digits += base13digits[positive%13]
    positive = positive // 13
  
  # reversed the digit 
  reversed_digits = digits[::-1] # to make it backwards
  
  # accomodate the negative
  if num < 0:
    return "-" + reversed_digits
  else: 
    return reversed_digits


# 2nd APPROACH - list based
def convertToBase13(num):
    if num == 0:
        return "0"
    
    base13_digits = "0123456789ABC"
    digits_arr = []
    positive = abs(num)
    
    while positive > 0:
        # Append to list
        digits_arr.append(base13_digits[positive % 13])  
        positive = positive // 13
    
    reversed_digits = digits_arr[::-1]
    # Join list into a string
    result = ''.join(reversed_digits)  
    
    if num < 0:
        return "-" + result
    else:
        return result

# 3rd Approach - recursive calls
def convertToBase13(num):
    base13_digits = "0123456789ABC"
    
    def convertPositiveToBase13(positive_number):
        if positive_number < 13:
            return base13_digits[positive_number]  # Return single digit
        else:
            return convertPositiveToBase13(positive_number // 13) + base13_digits[positive_number % 13] # refer to the base digit so the output is string
    
    if num < 0:
        return "-" + convertPositiveToBase13(abs(num))
    else:
        return convertPositiveToBase13(num)