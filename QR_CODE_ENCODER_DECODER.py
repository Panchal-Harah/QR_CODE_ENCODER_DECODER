import qrcode
import cv2

def generate_qr(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code generated and saved as {filename}")

def decode_qr(image_path):
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, vertices_array, _ = detector.detectAndDecode(img)

    if vertices_array is not None:
        return data
    else:
        return "No QR code detected"

# Example Usage
if __name__ == "__main__":
    data_to_encode = "https://www.example.com"
    qr_filename = "example_qr.png"
    
    generate_qr(data_to_encode, qr_filename)
    
    decoded_data = decode_qr(qr_filename)
    print("Decoded data:", decoded_data)
