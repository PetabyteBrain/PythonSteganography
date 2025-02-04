import tkinter as tk
from tkinter import filedialog, messagebox, StringVar, OptionMenu
from PIL import Image
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import os

# Global variables
key_directory = ""
private_key = None
public_key = None

# Set the directory for saving/loading keys
def set_key_directory():
    global key_directory
    key_directory = filedialog.askdirectory(title="Select Directory for Keys")
    if key_directory:
        with open(os.path.expanduser("~/.steganography_key_dir"), "w") as f:
            f.write(key_directory)
        messagebox.showinfo("Success", f"Key directory set to:\n{key_directory}")

# Load key directory on startup
if os.path.exists(os.path.expanduser("~/.steganography_key_dir")):
    with open(os.path.expanduser("~/.steganography_key_dir"), "r") as f:
        key_directory = f.read().strip()

# Generate public/private keys and save them to the directory
def generate_and_save_keys():
    global private_key, public_key

    if not key_directory:
        messagebox.showerror("Error", "Please set the key directory first.")
        return

    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    private_key_path = os.path.join(key_directory, "private_key.pem")
    public_key_path = os.path.join(key_directory, "public_key.pem")

    # Save private key
    with open(private_key_path, "wb") as private_file:
        private_file.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )
        )

    # Save public key
    with open(public_key_path, "wb") as public_file:
        public_file.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )

    messagebox.showinfo("Success", f"Keys generated and saved to:\n{key_directory}")

# Encrypt a message using RSA
def encrypt_message(message, key):
    return key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

# Encrypt a message using steganography
def encrypt_with_public_key():
    image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not image_path:
        return

    message = message_entry.get()
    if not message:
        messagebox.showerror("Error", "Please enter a message to hide.")
        return

    if not public_key:
        messagebox.showerror("Error", "Public key not found. Please generate keys first.")
        return

    try:
        encrypted_message = encrypt_message(message, public_key)
        binary_message = ''.join(format(byte, '08b') for byte in encrypted_message) + '1111111111111110'
    except Exception as e:
        messagebox.showerror("Error", f"Encryption failed: {e}")
        return

    method = stego_method_var.get()
    img = Image.open(image_path).convert("RGB")
    data = list(img.getdata())
    new_data = []
    data_index = 0

    for pixel in data:
        if data_index < len(binary_message):
            new_pixel = (pixel[0] & ~1 | int(binary_message[data_index]), pixel[1], pixel[2])
            new_data.append(new_pixel)
            data_index += 1
        else:
            new_data.append(pixel)

    img.putdata(new_data)
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        img.save(save_path)
        messagebox.showinfo("Success", "Message hidden successfully!")

# Decrypt a message using the private key
def decrypt_with_private_key():
    image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not image_path:
        return

    method = stego_method_var.get()
    img = Image.open(image_path)
    img = img.convert("RGB")
    data = list(img.getdata())
    binary_message = ""

    for pixel in data:
        binary_message += str(pixel[0] & 1)
        if "1111111111111110" in binary_message:
            break

    binary_message = binary_message[:binary_message.find("1111111111111110")]

    encrypted_message = bytes(int(binary_message[i:i+8], 2) for i in range(0, len(binary_message), 8))
    try:
        decrypted_message = private_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ).decode('utf-8')
        messagebox.showinfo("Decrypted Message", decrypted_message)
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {e}")

# UI setup
root = tk.Tk()
root.title("Secure Steganography Tool")

message_label = tk.Label(root, text="Enter message to hide:")
message_label.pack(pady=5)

message_entry = tk.Entry(root, width=50)
message_entry.pack(pady=5)

stego_method_var = StringVar(root)
stego_method_var.set("LSB - Easy")
stego_method_label = tk.Label(root, text="Select steganography method:")
stego_method_label.pack(pady=5)

stego_method_menu = OptionMenu(root, stego_method_var, "LSB - Easy", "LSB - Medium", "LSB - Hard", "Pattern-Based Encoding")
stego_method_menu.pack(pady=5)

decrypt_private_button = tk.Button(root, text="Decrypt with Private Key", command=decrypt_with_private_key)
decrypt_private_button.pack(pady=10)

encrypt_button = tk.Button(root, text="Encrypt with Public Key", command=encrypt_with_public_key)
encrypt_button.pack(pady=10)

set_key_dir_button = tk.Button(root, text="Set Key Directory", command=set_key_directory)
set_key_dir_button.pack(pady=10)

gen_keys_button = tk.Button(root, text="Generate Keys", command=generate_and_save_keys)
gen_keys_button.pack(pady=10)

root.mainloop()
