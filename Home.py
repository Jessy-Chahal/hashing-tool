import streamlit as st

# Main content area
st.title("Hashing Tool")
st.write("This web app allows you to hash data using various algorithms.")

# Description for the home page
description = """
**Hashing Tool**

Welcome to the Hashing Tool, your go-to web application for secure data hashing. This tool empowers you to transform your data into a fixed-length string of characters using various robust hashing algorithms. Hashing is a fundamental technique in cryptography and data security, and our application makes it easy for you to perform this process effortlessly.

**Why Hashing Matters**

Hashing is essential for protecting sensitive information, such as passwords and personal data. When you hash data, it becomes nearly impossible to reverse-engineer the original content, ensuring the privacy and security of your information. The result is a unique hash that represents your data, making it ideal for storage and data integrity verification.

**Explore Multiple Algorithms**

With our Hashing Tool, you can explore a range of hashing algorithms, including MD5, SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, SHA3-256, and SHA3-512. Each algorithm offers varying levels of security and output length, catering to your specific needs.

**How to Use**

1. Select an Algorithm: Choose from the list of available algorithms based on your requirements.
2. Enter Data: Input the data you want to hash in the provided text area.
3. Hash It: Click the "Hash" button, and our tool will generate the hashed result for you.

**Secure Your Data**

Whether you're looking to securely store passwords, verify data integrity, or simply understand the concept of hashing, the Hashing Tool is your trusted companion. It simplifies the process of data transformation while ensuring the confidentiality of your information.

Start exploring the world of data security with our Hashing Tool today!
"""

st.markdown(description)
