# --------------------------------------------------------------------------- #
# Module: send_email.py
# Purpose: Sends emails using credentials stored in a file.
#
# Author: Matheus Ferreira Silva
# GitHub: https://github.com/MatheusFS-dev
# Created: 2024-11-25
# Last Modified: 2024-11-25
# Dependencies: smtplib, email.mime
#
# --------------------------------------------------------------------------- #

import json
import smtplib
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def get_credentials(file_path: str) -> tuple[str, str]:
    """
    Reads the sender's email and password from a JSON file.

    Parameters:
    - file_path (str): Path to the credentials JSON file.

    Returns:
    - tuple: A tuple containing the sender email and password.
    """
    try:
        with open(file_path, "r") as file:
            credentials = json.load(file)
            return credentials["email"], credentials["password"]
    except Exception as e:
        raise ValueError(f"Failed to read credentials: {e}")


def get_recipient_emails(file_path: str) -> list[str]:
    """
    Reads a list of recipient email addresses from a JSON file.

    Parameters:
    - file_path (str): Path to the recipient JSON file.

    Returns:
    - list: A list of recipient email addresses.
    """
    try:
        with open(file_path, "r") as file:
            recipient_data = json.load(file)
            return recipient_data["emails"]
    except Exception as e:
        raise ValueError(f"Failed to read recipient emails: {e}")


def send_email(
    subject: str, body: str, recipients_file: str, credentials_file: str, text_type: str = "plain"
) -> None:
    """
    Sends an email notification with the specified subject and body content to multiple recipients.

    Parameters:
    - subject (str): The subject of the email.
    - body (str): The main content of the email.
    - recipients_file (str): Path to the recipients JSON file.
    - credentials_file (str): Path to the credentials JSON file.
    - text_type (str): The type of text content (default is "plain").
    """
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Retrieve sender email and password
    try:
        sender_email, sender_password = get_credentials(credentials_file)
    except ValueError as e:
        print(f"[ERROR] {e}")
        return

    # Retrieve recipient email addresses
    try:
        recipient_emails = get_recipient_emails(recipients_file)
    except ValueError as e:
        print(f"[ERROR] {e}")
        return

    # Compose the email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = ", ".join(recipient_emails)
    message["Subject"] = subject
    message.attach(MIMEText(body, text_type))

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_emails, message.as_string())
        print("[INFO] Email sent successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")


def run_with_notification(
    func,
    func_args: tuple,
    func_kwargs: dict,
    recipients_file: str,
    credentials_file: str,
    subject_success: str = "🎉 Task Completed Successfully",
    body_success: str = """
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <h2 style="color: #28a745;">✔️ Task Completed</h2>
                <p>The task you ran has completed successfully without any errors.</p>
                <p>Thank you for using our system.</p>
                <footer style="margin-top: 20px; text-align: center; font-size: 14px; color: #888;">
                    <p>Best regards,</p>
                    <p><strong>The Bot Mailman</strong></p>
                </footer>
            </body>
        </html>
        """,
    text_type: str = "plain",
):
    """
    Runs a given function and sends an email notification upon completion or error.

    Parameters:
    - func (function): The function to execute.
    - func_args (tuple): Positional arguments to pass to the function.
    - func_kwargs (dict): Keyword arguments to pass to the function.
    - recipients_file (str): Path to the recipients JSON file.
    - credentials_file (str): Path to the credentials JSON file.
    - subject_success (str): Subject for the success email.
    - body_success (str): Body content for the success email.
    - text_type (str): The type of text content (default is "plain").
    """
    try:
        # Execute the provided function
        func(*func_args, **func_kwargs)

        # If successful, send a success email
        subject = subject_success
        body = body_success
        send_email(subject, body, recipients_file, credentials_file, text_type)
        print("[INFO] Success email sent.")
    except Exception as e:
        # Capture the error and send an error email
        error_message = traceback.format_exc()
        subject = "❌ Task Failed with an Error"
        body = f"""
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <h2 style="color: #dc3545;">❌ Task Failed</h2>
                <p>The task you ran encountered an error:</p>
                <pre style="background-color: #f8d7da; color: #721c24; padding: 10px; border-radius: 5px; font-size: 14px;">
                {error_message}
                </pre>
                <p>Please review the error above and try again.</p>
                <footer style="margin-top: 20px; text-align: center; font-size: 14px; color: #888;">
                    <p>Best regards,</p>
                    <p><strong>The Bot Mailman</strong></p>
                </footer>
            </body>
        </html>
        """
        send_email(subject, body, recipients_file, credentials_file, text_type)
        print("[INFO] Error email sent.")


# Example usage
if __name__ == "__main__":
    credentials_file_path = "credentials.json"
    recipient_file_path = "recipients.json"

    # ---------------------------------- Example --------------------------------- #
    email_subject = "Model Training Complete"
    email_body = f"""
    <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; background-color: #f9f9f9; padding: 20px;">
            <div style="max-width: 600px; margin: auto; background: #fff; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
                <h2 style="color: #0056b3; text-align: center;">🎉 Training Complete</h2>
                <p style="font-size: 16px; color: #444;">
                    <strong>Dear User,</strong>
                </p>
                <p style="font-size: 18px; color: #333;">
                    Your model, <strong style="color: #0056b3;">LSTM_DNN</strong>, has successfully completed training!
                </p>
                <p style="font-size: 16px; color: #555;">
                    I'm excited to see how you'll utilize your new model!
                </p>
                <p style="text-align: center; font-size: 16px;">
                    <strong style="color: #28a745;">✔️ Training Status:</strong> <span style="color: #0056b3;">Completed</span>
                </p>
                <footer style="margin-top: 20px; text-align: center; font-size: 14px; color: #888;">
                    <p>Best regards,</p>
                    <p><strong>The Bot Mailman</strong></p>
                </footer>
            </div>
        </body>
    </html>
    """
    # ------------------------------------- - ------------------------------------ #

    send_email(
        subject=email_subject,
        body=email_body,
        recipients_file=recipient_file_path,
        credentials_file=credentials_file_path,
        text_type="html",
    )

    def example_task(x, y):
        """
        A sample function that adds two numbers and raises an exception if x or y is negative.
        """
        if x < 0 or y < 0:
            raise ValueError("Inputs must be non-negative.")
        return x + y

    # Test 1: Successful Task
    run_with_notification(
        func=example_task,
        func_args=(10, 20),
        func_kwargs={},
        recipients_file=recipient_file_path,
        credentials_file=credentials_file_path,
        text_type="html",
    )

    # Test 2: Task with an Error
    run_with_notification(
        func=example_task,
        func_args=(-10, 20),
        func_kwargs={},
        recipients_file=recipient_file_path,
        credentials_file=credentials_file_path,
        text_type="html",
    )
