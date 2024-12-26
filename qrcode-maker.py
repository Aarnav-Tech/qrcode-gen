import qrcode
from PIL import Image

def generate_qr_code(data, version, error_correction, box_size, border):
    # Create a QR Code instance with user-defined parameters
    qr = qrcode.QRCode(
        version=version,  # controls the size of the QR Code
        error_correction=error_correction,  # controls the error correction used for the QR Code
        box_size=box_size,  # controls how many pixels each “box” of the QR code is
        border=border,  # controls how many boxes thick the border should be
    )
    
    # Add data to the QR Code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Show the image in a separate window
    img.show()

def get_wifi_data():
    ssid = input("Enter the Wi-Fi SSID: ")
    password = input("Enter the Wi-Fi password: ")
    encryption = input("Enter the encryption type (WPA/WPA2/WEP/none): ")
    return f"WIFI:S:{ssid};T:{encryption};P:{password};;"

def get_email_data():
    email = input("Enter the recipient's email address: ")
    subject = input("Enter the email subject: ")
    body = input("Enter the email body: ")
    return f"mailto:{email}?subject={subject}&body={body}"

def get_sms_data():
    phone_number = input("Enter the phone number: ")
    message = input("Enter the message: ")
    return f"smsto:{phone_number}:{message}"

def get_contact_data():
    name = input("Enter the contact name: ")
    email = input("Enter the contact email: ")
    phone = input("Enter the contact phone number: ")
    return f"BEGIN:VCARD\nVERSION:3.0\nFN:{name}\nEMAIL:{email}\nTEL:{phone}\nEND:VCARD"

def get_location_data():
    latitude = input("Enter the latitude: ")
    longitude = input("Enter the longitude: ")
    return f"https://www.google.com/maps?q={latitude},{longitude}"

if __name__ == "__main__":
    print("Select the type of QR code to generate:")
    print("1: URL")
    print("2: Plain Text")
    print("3: Wi-Fi Credentials")
    print("4: Email")
    print("5: SMS")
    print("6: Contact (vCard)")
    print("7: Location")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        data = input("Enter the URL: ")
    elif choice == '2':
        data = input("Enter the plain text: ")
    elif choice == '3':
        data = get_wifi_data()
    elif choice == '4':
        data = get_email_data()
    elif choice == '5':
        data = get_sms_data()
    elif choice == '6':
        data = get_contact_data()
    elif choice == '7':
        data = get_location_data()
    else:
        print("Invalid choice. Exiting.")
        exit()

    # Input QR code parameters
    version = int(input("Enter the version {This indicates the size.} (1-40, default is 1): ") or 1)
    
    # Error correction levels
    print("Error correction levels:")
    print("1: ERROR_CORRECT_L (7% of codewords can be restored)")
    print("2: ERROR_CORRECT_M (15% of codewords can be restored)")
    print("3: ERROR_CORRECT_Q (25% of codewords can be restored)")
    print("4: ERROR_CORRECT_H (30% of codewords can be restored)")
    error_correction_input = int(input("Enter the error correction level (1-4, default is 1): ") or 1)
    error_correction = {
        1: qrcode.constants.ERROR_CORRECT_L,
        2: qrcode.constants.ERROR_CORRECT_M,
        3: qrcode.constants.ERROR_CORRECT_Q,
        4: qrcode.constants.ERROR_CORRECT_H
    }.get(error_correction_input, qrcode.constants.ERROR_CORRECT_L)

    box_size = int(input("Enter the box size (default is 10): ") or 10)
    border = int(input("Enter the border size (default is 4): ") or 4)

    generate_qr_code(data, version, error_correction, box_size, border)