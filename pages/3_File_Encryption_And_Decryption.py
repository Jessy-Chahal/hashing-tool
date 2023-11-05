import streamlit as st
from cryptography.fernet import Fernet
import os
import secrets

def write():
    st.title("File Encryption and Decryption")

    st.markdown(
        """
        The encryption and decryption of files can lead to data loss if not used correctly.
        The authors and maintainers of this application are not responsible for any data loss,
        damage, or misuse of this application.
        
        Please be cautious when using this application and ensure you have proper backups of
        your data before proceeding with any file encryption or decryption.
        """
    )

    # Function to generate random Fernet keys as sample keys
    def generate_sample_keys(count):
        sample_keys = [Fernet.generate_key() for _ in range(count)]
        return sample_keys

    # Encryption function
    def encrypt_file(file_path, key):
        try:
            with open(file_path, 'rb') as f:
                data = f.read()
            fernet = Fernet(key)
            encrypted = fernet.encrypt(data)
            with open(file_path, 'wb') as f:
                f.write(encrypted)
            st.success("File encrypted successfully!")
        except Exception as e:
            st.error(f"Encryption error: {str(e)}")

    # Decryption function
    def decrypt_file(file_path, key):
        try:
            with open(file_path, 'rb') as f:
                data = f.read()
            fernet = Fernet(key)
            decrypted = fernet.decrypt(data)
            with open(file_path, 'wb') as f:
                f.write(decrypted)
            st.success("File decrypted successfully!")
        except Exception as e:
            st.error(f"Decryption error: {str(e)}")

    # UI for uploading file and entering key
    uploaded_file = st.file_uploader("Choose a file to encrypt/decrypt")
    if uploaded_file is not None:
        st.write("Selected file:", uploaded_file.name)
        operation = st.radio("Select operation", ("Encrypt", "Decrypt"))
        key = st.text_input("Enter key (32 bytes long and encoded in a URL-safe base64 format) to encrypt/decrypt the file")

        if operation == "Encrypt":
            sample_keys = generate_sample_keys(5)
            st.markdown("Sample keys you can use:")
            for i, sample_key in enumerate(sample_keys):
                st.text(f"{i + 1}. {sample_key.decode()}")

        if st.button("Submit"):
            if not key:
                st.error("Please enter a valid key.")
            else:
                try:
                    file_path = uploaded_file.name
                    with open(file_path, 'wb') as f:
                        f.write(uploaded_file.getbuffer())

                    if operation == "Encrypt":
                        encrypt_file(file_path, key.encode())
                    else:
                        decrypt_file(file_path, key.encode())
                except Exception as e:
                    st.error(f"File operation error: {str(e)}")

if __name__ == "__main__":
    write()
