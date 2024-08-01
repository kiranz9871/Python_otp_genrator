import random
import smtplib
from email.message import EmailMessage
import getpass

# Function to generate a 6-digit OTP
def generate_otp():
    return random.randint(100000, 999999)

# Function to send OTP via email
def send_otp(email, otp):
    sender_email = "kiranzirpe9871@gmail.com"  
    sender_password = getpass.getpass("Enter your app password: ")  

    msg = EmailMessage()
    msg.set_content(f"Your OTP is {otp}")
    msg["Subject"] = "Your OTP Code" 
    msg["From"] = sender_email
    msg["To"] = email

    # Sending email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print(f"OTP sent to {email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to validate the OTP entered by the user
def validate_otp(generated_otp):
    user_otp = input("Enter the OTP sent to your email: ")
    if user_otp.isdigit() and int(user_otp) == generated_otp:
        return True
    return False

def main():
    email = input("Enter your email address: ")
    otp = generate_otp()
    send_otp(email, otp)
    
    if validate_otp(otp):
        print("Access Granted")
    else:
        print("Access Denied")

if __name__ == "__main__":
    main()
