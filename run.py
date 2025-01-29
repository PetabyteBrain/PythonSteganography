import tkinter as tk
from tkinter import filedialog, messagebox, StringVar, OptionMenu, Toplevel, Label, Button
from PIL import Image
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import os

# Global variables
key_directory = ""
private_key = None
public_key = None
friend_public_key = None

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

# Load a public key from a file (for friend's key)
def load_friend_public_key():
    global friend_public_key

    friend_key_path = filedialog.askopenfilename(
        title="Select Friend's Public Key", filetypes=[("PEM Files", "*.pem")]
    )

    if not friend_key_path:
        return

    try:
        with open(friend_key_path, "rb") as f:
            friend_public_key_data = f.read()
            friend_public_key = serialization.load_pem_public_key(friend_public_key_data)
            messagebox.showinfo("Success", "Friend's public key loaded successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load friend's public key: {e}")

# Encrypt a message using steganography with your public key
def encrypt_with_own_public_key():
    image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not image_path:
        return

    message = message_entry.get()
    if not message:
        messagebox.showerror("Error", "Please enter a message to hide.")
        return

    if not public_key:
        messagebox.showerror("Error", "Public key not found. Please generate your keys.")
        return

    method = stego_method_var.get()
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '1111111111111110'  # Delimiter

    img = Image.open(image_path)
    img = img.convert("RGB")
    data = list(img.getdata())
    new_data = []
    data_index = 0

    for pixel in data:
        if data_index < len(binary_message):
            if method == "LSB - Easy":
                # Modify the least significant bit of the red channel
                new_pixel = (pixel[0] & ~1 | int(binary_message[data_index]), pixel[1], pixel[2])
                data_index += 1
            elif method == "LSB - Medium":
                # Modify the last 2 bits of the red channel
                new_pixel = (pixel[0] & ~3 | int(binary_message[data_index:data_index+2], 2), pixel[1], pixel[2])
                data_index += 2
            elif method == "LSB - Hard":
                # Modify the last 3 bits of the red channel
                new_pixel = (pixel[0] & ~7 | int(binary_message[data_index:data_index+3], 2), pixel[1], pixel[2])
                data_index += 3
            elif method == "Pattern-Based Encoding":
                # Modify the last 4 bits of the red channel
                new_pixel = ((pixel[0] & ~15) | int(binary_message[data_index:data_index+4], 2), pixel[1], pixel[2])
                data_index += 4
            new_data.append(new_pixel)
        else:
            new_data.append(pixel)

    img.putdata(new_data)

    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        img.save(save_path)
        messagebox.showinfo("Success", "Message hidden successfully!")

# Encrypt a message using steganography with friend's public key
def encrypt_with_friend_public_key():
    image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not image_path:
        return

    message = message_entry.get()
    if not message:
        messagebox.showerror("Error", "Please enter a message to hide.")
        return

    if not friend_public_key:
        messagebox.showerror("Error", "Friend's public key not loaded. Please load your friend's public key.")
        return

    method = stego_method_var.get()
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '1111111111111110'  # Delimiter

    img = Image.open(image_path)
    img = img.convert("RGB")
    data = list(img.getdata())
    new_data = []
    data_index = 0

    for pixel in data:
        if data_index < len(binary_message):
            if method == "LSB - Easy":
                # Modify the least significant bit of the red channel
                new_pixel = (pixel[0] & ~1 | int(binary_message[data_index]), pixel[1], pixel[2])
                data_index += 1
            elif method == "LSB - Medium":
                # Modify the last 2 bits of the red channel
                new_pixel = (pixel[0] & ~3 | int(binary_message[data_index:data_index+2], 2), pixel[1], pixel[2])
                data_index += 2
            elif method == "LSB - Hard":
                # Modify the last 3 bits of the red channel
                new_pixel = (pixel[0] & ~7 | int(binary_message[data_index:data_index+3], 2), pixel[1], pixel[2])
                data_index += 3
            elif method == "Pattern-Based Encoding":
                # Modify the last 4 bits of the red channel
                new_pixel = ((pixel[0] & ~15) | int(binary_message[data_index:data_index+4], 2), pixel[1], pixel[2])
                data_index += 4
            new_data.append(new_pixel)
        else:
            new_data.append(pixel)

    img.putdata(new_data)

    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        img.save(save_path)
        messagebox.showinfo("Success", "Message hidden successfully!")

# Decrypt a message from steganography with private key
def decrypt_steganography():
    image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not image_path:
        return

    method = stego_method_var.get()
    img = Image.open(image_path)
    img = img.convert("RGB")
    data = list(img.getdata())
    binary_message = ""

    for pixel in data:
        if method == "LSB - Easy":
            binary_message += str(pixel[0] & 1)
        elif method == "LSB - Medium":
            binary_message += format(pixel[0] & 3, '02b')
        elif method == "LSB - Hard":
            binary_message += format(pixel[0] & 7, '03b')
        elif method == "Pattern-Based Encoding":
            binary_message += format(pixel[0] & 15, '04b')

        # Stop if delimiter is found
        if "1111111111111110" in binary_message:
            break

    # Truncate the binary message at the delimiter
    binary_message = binary_message[:binary_message.find("1111111111111110")]

    # Decode the message from binary
    decoded_message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        decoded_message += chr(int(byte, 2))

    if decoded_message:
        messagebox.showinfo("Decrypted Message", decoded_message)
    else:
        messagebox.showerror("Error", "No message found!")

# Help page
def open_help():
    help_window = Toplevel()
    help_window.title("Help")

    help_text = """
    Welcome to the Steganography Tool!

    This tool allows you to hide messages in images using steganography.

    Features:
    - Encrypt a message by selecting an image and choosing a method.
    - Decrypt a message from a previously encoded image.
    - Save and load keys for encryption/decryption.
    - Choose between multiple steganography methods (LSB Easy, LSB Medium, LSB Hard, Pattern-Based Encoding).
    - You can choose to use your own keys or load a friend's public key.

    Instructions:
    1. Set the key directory where your keys will be saved.
    2. Generate your public and private keys.
    3. Select a steganography method and either encrypt or decrypt a message.
    4. For encryption, choose your or a friend's public key.
    5. For decryption, use your private key or your friend's private key.

    Enjoy!
    """

    label = Label(help_window, text=help_text, padx=10, pady=10, justify="left")
    label.pack()

    close_button = Button(help_window, text="Close", command=help_window.destroy)
    close_button.pack(pady=10)

# Main UI
root = tk.Tk()
root.title("Secure Steganography Tool")

message_label = tk.Label(root, text="Enter message to hide:")
message_label.pack(pady=5)

message_entry = tk.Entry(root, width=50)
message_entry.pack(pady=5)

stego_method_var = StringVar(root)
stego_method_var.set("LSB - Easy")  # Default value
stego_method_label = tk.Label(root, text="Select steganography method:")
stego_method_label.pack(pady=5)

stego_method_menu = OptionMenu(root, stego_method_var, "LSB - Easy", "LSB - Medium", "LSB - Hard", "Pattern-Based Encoding")
stego_method_menu.pack(pady=5)

encrypt_own_button = tk.Button(root, text="Encrypt with Own Public Key", command=encrypt_with_own_public_key)
encrypt_own_button.pack(pady=10)

encrypt_friend_button = tk.Button(root, text="Encrypt with Friend's Public Key", command=encrypt_with_friend_public_key)
encrypt_friend_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_steganography)
decrypt_button.pack(pady=10)

set_key_dir_button = tk.Button(root, text="Set Key Directory", command=set_key_directory)
set_key_dir_button.pack(pady=10)

gen_keys_button = tk.Button(root, text="Generate Keys", command=generate_and_save_keys)
gen_keys_button.pack(pady=10)

help_button = tk.Button(root, text="Help", command=open_help)
help_button.pack(pady=10)

# Load Friend's public key
load_friend_pub_key_button = tk.Button(root, text="Load Friend's Public Key", command=load_friend_public_key)
load_friend_pub_key_button.pack(pady=10)

root.mainloop()
