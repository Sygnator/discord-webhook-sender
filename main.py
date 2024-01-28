import streamlit as st
import requests

# count embeds
if 'embed_counter' not in st.session_state:
    st.session_state.embed_counter = 0

def send_discord_webhook(url, data):
    response = requests.post(url, json=data)
    return response

def create_embed_fields():
    text_embeds = []

    if st.button("Add embed"): 
        if st.session_state.embed_counter < 3:
            st.session_state.embed_counter += 1
        else:
            st.warning("You cannot create more than 3 embeds.")

    for i in range(st.session_state.embed_counter):
        with st.expander(f"Embed {i+1}"):
            e_title = st.text_input("Enter Embed Title", key=f"t{i}")
            e_description = st.text_area(f"Enter Embed Content:", max_chars=2000, key=f"d{i}")
            text_embeds.append({'title': e_title, 'description': e_description})
    
    return text_embeds

def main():
    st.title("Discord Webhook Customizer")

    # Input fields for user to customize the Discord webhook
    webhook_url = st.text_input("Enter Discord Webhook URL:", placeholder="https://discord.com/api/webhooks/...")
    content = st.text_area(f"Enter Message Content:", max_chars=2000)

    # Add a new embed field
    embeds = create_embed_fields()

    st.text(embeds)

    # Button to send the message
    if st.button("Send Message"):
        if not webhook_url:
            st.warning("Please enter a Discord Webhook URL.")
        else:
            data = {
                "content": content,
                "embeds": embeds
            }

            response = send_discord_webhook(webhook_url.replace(" ", ""), data)

            if response.status_code == 204:
                st.success("Message sent successfully!")
            else:
                st.error(f"Failed to send message. Status Code: {response.status_code}")

if __name__ == "__main__":
    main()