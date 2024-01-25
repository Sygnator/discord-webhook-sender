import streamlit as st
import requests

def send_discord_webhook(url, data):
    response = requests.post(url, json=data)
    return response

def main():
    st.title("Discord Webhook Customizer")

    # Input fields for user to customize the Discord webhook
    webhook_url = st.text_input("Enter Discord Webhook URL:")
    content = st.text_area("Enter Message Content:")

    # Button to send the message
    if st.button("Send Message"):
        if not webhook_url:
            st.warning("Please enter a Discord Webhook URL.")
        else:
            data = {
                "content": content,
            }

            response = send_discord_webhook(webhook_url, data)

            if response.status_code == 204:
                st.success("Message sent successfully!")
            else:
                st.error(f"Failed to send message. Status Code: {response.status_code}")

if __name__ == "__main__":
    main()