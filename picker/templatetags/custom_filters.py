from django import template
# import re

# myapp/templatetags/custom_filters.py


register = template.Library()

@register.filter
def slice_from_dollar(value):
    if '$' in value:
        return value[value.index('$'):]
    return value




# register = template.Library()

# @register.filter
# def extract_number(value):
#     # Find the portion after '='
#     match = re.search(r'=\s*\$([\d,\.]+)', value)
#     if match:
#         number_str = match.group(1)  # Get the numeric part
#         # Remove commas and convert to float
#         return float(number_str.replace(',', ''))
#     return 0

# @register.filter
# def subtract(value, arg):
#     try:
#         return value - arg
#     except (ValueError, TypeError):
#         return 0


# register = template.Library()

# @register.filter
# def extract_parts(value):
#     # Define regex patterns to capture alphabetic and numeric parts
#     alpha_pattern = r'[A-Za-z]+'
#     numeric_pattern = r'\$([\d,\.]+)'  # Adjust if different numeric formats are needed
    
#     # Find all alphabetic and numeric matches in the input string
#     alpha_matches = re.findall(alpha_pattern, value)
#     numeric_matches = re.findall(numeric_pattern, value)
    
#     # Convert numeric matches to floats
#     numbers = [float(match.replace(',', '')) for match in numeric_matches]
    
#     return {
#         'alphabets': alpha_matches,
#         'numbers': numbers
#     }
