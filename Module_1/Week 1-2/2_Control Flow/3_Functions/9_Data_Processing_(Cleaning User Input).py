def clean_input(user_input):
    """Cleans user input by removing extra spaces and converting it to lowercase."""
    cleaned_data = user_input.strip().lower()
    return cleaned_data

# Real-world example:
name = "   John Doe   "
email = "  EXAMPLE@Email.com  "

print("Cleaned Name:", clean_input(name))  
print("Cleaned Email:", clean_input(email)) 
