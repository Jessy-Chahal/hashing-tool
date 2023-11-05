import streamlit as st
import random
import string

# Streamlit App Title
st.title("Password Generator")

# Function to generate a password
def generate_password(length, use_special_chars, use_uppercase, use_lowercase, use_numbers):
    characters = string.ascii_letters
    if use_special_chars:
        characters += string.punctuation
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input options
length = st.slider("Select password length:", 4, 50, 12)
use_special_chars = st.checkbox("Include special characters")
use_uppercase = st.checkbox("Include uppercase letters")
use_lowercase = st.checkbox("Include lowercase letters")
use_numbers = st.checkbox("Include numbers")

# Generate password button
if st.button("Generate Password"):
    if not (use_special_chars or use_uppercase or use_lowercase or use_numbers):
        st.error("Please select at least one option.")
    else:
        password = generate_password(length, use_special_chars, use_uppercase, use_lowercase, use_numbers)
        st.code("Generated Password: " + password, language="")
  