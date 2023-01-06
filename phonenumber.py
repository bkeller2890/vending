import re

def validate_phone_number(phone_number):
  # Use a regular expression to match the phone number in the following formats: 123-456-7890, 123.456.7890, 123 456 7890, and 1234567890.
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
