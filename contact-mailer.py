#!/usr/bin/env python3
"""Lightweight SMTP contact form handler for iremedy.com"""
import os
import json
import smtplib
import html
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.sendgrid.net")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
SMTP_USER = os.environ.get("SMTP_USER", "apikey")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD", "")
SMTP_FROM = os.environ.get("SMTP_FROM", "noreply@iremedy.com")
RECIPIENT = os.environ.get("RECIPIENT", "sales@iremedy.com")
REDIRECT_URL = os.environ.get("REDIRECT_URL", "https://iremedy.com")

class ContactHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/send":
            self.send_response(404)
            self.end_headers()
            return

        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length).decode("utf-8")

        # Parse form data
        content_type = self.headers.get("Content-Type", "")
        if "application/x-www-form-urlencoded" in content_type:
            fields = {k: v[0] for k, v in parse_qs(body).items()}
        elif "application/json" in content_type:
            fields = json.loads(body)
        else:
            fields = {k: v[0] for k, v in parse_qs(body).items()}

        # Honeypot check
        if fields.get("_honey"):
            self.send_response(302)
            self.send_header("Location", REDIRECT_URL)
            self.end_headers()
            return

        # Build email
        name = html.escape(fields.get("name", "Unknown"))
        email = html.escape(fields.get("email", "not provided"))
        phone = html.escape(fields.get("phone", ""))
        org = html.escape(fields.get("organization", ""))
        title = html.escape(fields.get("title", ""))
        user_type = html.escape(fields.get("type", ""))
        topic = html.escape(fields.get("topic", ""))
        message = html.escape(fields.get("message", ""))

        subject = f"iRemedy.com Contact: {name} ({org})" if org else f"iRemedy.com Contact: {name}"

        html_body = f"""
        <h2>New Contact Form Submission</h2>
        <table style="border-collapse:collapse;width:100%;max-width:600px;">
            <tr><td style="padding:8px;border:1px solid #ddd;font-weight:bold;">Name</td><td style="padding:8px;border:1px solid #ddd;">{name}</td></tr>
            <tr><td style="padding:8px;border:1px solid #ddd;font-weight:bold;">Email</td><td style="padding:8px;border:1px solid #ddd;"><a href="mailto:{email}">{email}</a></td></tr>
            <tr><td style="padding:8px;border:1px solid #ddd;font-weight:bold;">Phone</td><td style="padding:8px;border:1px solid #ddd;">{phone}</td></tr>
            <tr><td style="padding:8px;border:1px solid #ddd;font-weight:bold;">Organization</td><td style="padding:8px;border:1px solid #ddd;">{org}</td></tr>
            <tr><td style="padding:8px;border:1px solid #ddd;font-weight:bold;">Title / Role</td><td style="padding:8px;border:1px solid #ddd;">{title}</td></tr>
            <tr><td style="padding:8px;border:1px solid #ddd;font-weight:bold;">Type</td><td style="padding:8px;border:1px solid #ddd;">{user_type}</td></tr>
            <tr><td style="padding:8px;border:1px solid #ddd;font-weight:bold;">Topic</td><td style="padding:8px;border:1px solid #ddd;">{topic}</td></tr>
            <tr><td style="padding:8px;border:1px solid #ddd;font-weight:bold;">Message</td><td style="padding:8px;border:1px solid #ddd;">{message}</td></tr>
        </table>
        """

        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = SMTP_FROM
        msg["To"] = RECIPIENT
        msg["Reply-To"] = email
        msg.attach(MIMEText(html_body, "html"))

        try:
            with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_USER, SMTP_PASSWORD)
                server.sendmail(SMTP_FROM, [RECIPIENT], msg.as_string())
            print(f"[OK] Email sent for {name} <{email}>")
        except Exception as e:
            print(f"[ERROR] Failed to send email: {e}")
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Failed to send email"}).encode())
            return

        # Redirect back to site
        self.send_response(302)
        self.send_header("Location", REDIRECT_URL + "?submitted=1")
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "https://iremedy.com")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def log_message(self, format, *args):
        print(f"[contact-mailer] {args[0]}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8901"))
    server = HTTPServer(("127.0.0.1", port), ContactHandler)
    print(f"Contact mailer listening on 127.0.0.1:{port}")
    server.serve_forever()
