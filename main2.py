import queue
import threading
import streamlit as st

from embedchain import App
from dotenv import load_dotenv
load_dotenv()

import os

# Initialize the app and set it online
@st.cache(allow_output_mutation=True)
def initialize_app():
    app = App()
    app.online = True
    return app

os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
app = initialize_app()

def scrape_professor_rating(professor_name):
    # Implement your scraping logic here
    # Placeholder for actual scraping logic
    rating = "Rating not found"
    return rating

# Function to handle general queries
def handle_general_query(prompt):
    try:
        return app.query(prompt+"at ASU")
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit UI setup
st.title("🙏 ASU AI")
styled_caption = '<p style="font-size: 17px; color: #aaa;">🚀 An <a href="https://github.com/embedchain/embedchain">Embedchain</a> app powered with ASU\'s wisdom!</p>'
st.markdown(styled_caption, unsafe_allow_html=True)

# Initialize `messages` in session state if not already initialized
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": "Hi, I'm ASU AI! I'm here to answer your questions."
    }]

# Display all previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar="https://newsroom.asu.edu/sites/default/files/styles/panopoly_image_original/public/asu_logo.png?itok=y1sQJVl7" if message["role"] == "assistant" else None):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything!"):
    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

    def app_response(result):
        try:
            if "rating of" in prompt.lower():
                # Extract professor name
                professor_name = prompt.lower().replace("rating of", "").strip()
                result["answer"] = scrape_professor_rating(professor_name)
            else:
                # Handle general query
                result["answer"] = handle_general_query(prompt)
        except Exception as e:
            result["error"] = str(e)

    results = {}
    thread = threading.Thread(target=app_response, args=(results,))
    thread.start()
    thread.join()

    with st.chat_message("assistant", avatar="https://newsroom.asu.edu/sites/default/files/styles/panopoly_image_original/public/asu_logo.png?itok=y1sQJVl7"):
        if "error" in results:
            st.error(f"An error occurred: {results['error']}")
        elif "answer" in results:
            answer = results["answer"]
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
        else:
            st.error("No response received.")
