import streamlit as st
import hashlib

def display_hashing_page():
    st.subheader("Hashing")
    
    # Algorithm selection on the main page
    algorithm = st.selectbox("Select an algorithm:", ("MD5", "SHA-1", "SHA-224", "SHA-256", "SHA-384", "SHA-512", "SHA3-256", "SHA3-512"))
    
    # Input field for the data to be hashed
    data_to_hash = st.text_area("Enter the data to be hashed:")
    
    # Function to perform hashing based on the selected algorithm
    def perform_hashing(data, algorithm):
        if data:
            if algorithm == "MD5":
                return hashlib.md5(data.encode()).hexdigest()
            elif algorithm == "SHA-1":
                return hashlib.sha1(data.encode()).hexdigest()
            elif algorithm == "SHA-224":
                return hashlib.sha224(data.encode()).hexdigest()
            elif algorithm == "SHA-256":
                return hashlib.sha256(data.encode()).hexdigest()
            elif algorithm == "SHA-384":
                return hashlib.sha256(data.encode()).hexdigest()
            elif algorithm == "SHA-512":
                return hashlib.sha256(data.encode()).hexdigest()
            elif algorithm == "SHA3-256":
                return hashlib.sha3_256(data.encode()).hexdigest()
            elif algorithm == "SHA3-512":
                return hashlib.sha3_512(data.encode()).hexdigest()
    
    # Perform hashing when the user clicks the "Hash" button
    if st.button("Hash"):
        if not data_to_hash:
            st.error("Please enter data to hash.")
        else:
            hashed_result = perform_hashing(data_to_hash, algorithm)
            st.code(f"Hashed data using {algorithm}: {hashed_result}", language="")

if __name__ == "__main__":
    display_hashing_page()