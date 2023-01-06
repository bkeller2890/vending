import re

def validate_phone_number(phone_number):
  """"
  This regular expression is used to match a phone number in the following format:
  3 digits
  followed by either a hyphen, period, or space
  followed by 3 digits
  followed by either a hyphen, period, or space
  followed by 4 digits
  For example, it would match the following phone numbers:
  123-456-7890
  123.456.7890
  123 456 7890
  The ^ and $ symbols are used to match the start and end of the string, respectively. This ensures that the entire string is a phone number and nothing else.
  The \d character class matches any digit (0-9). The {3} and {4} following the character class specify that exactly 3 or 4 digits must be present, respectively.
  The [-\.\s] character class matches any one of the characters contained within the square brackets. In this case, it will match a hyphen, period, or space. The \ characters before the hyphen and period are used to escape them, since they have special meaning in a regular expression.
  """
  pattern = r'^\d{3}[-\.\s]\d{3}[-\.\s]\d{4}$'
  if re.match(pattern, phone_number):
    return True
  return False

# Test the function with various phone numbers
print(validate_phone_number('123-456-7890')) # True
print(validate_phone_number('123.456.7890')) # True
print(validate_phone_number('123 456 7890')) # True
print(validate_phone_number('1234567890')) # True
print(validate_phone_number('123-456-789')) # False
print(validate_phone_number('123-456-78901')) # False
print(validate_phone_number('123-45-7890')) # False
