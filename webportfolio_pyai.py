# streamlit run webportfolio_pyai.py
import streamlit as st
from streamlit.components.v1 import html
import google.generativeai as genai
import json
import re
import plotly.graph_objects as go

st.write("#")
# Acts as an anchor to the top of the page when it loads.

# Configure API
my_api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=my_api_key)
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

# Personas
persona = """
        You are Reethi AI Assistant. You help people answer questions about yourself (i.e Reethi).
        Answer only in the first person as if you are responding as Reethi herself.
        If you don't know the answer, simply say "That's a secret" or a variation of the phrase.
        If the prompt is not a question, tell the user to ask a question about you as Reethi instead of chatting.
        If a query is related to Reethi's work, her current programming info or her service charges, say a variation of the phrase "To know more, let's connect!" and share Reethi's email.
        If the query is about telling the user a joke, answer with "How many programmers does it take to change a light bulb? None. It's a hardware problem." 
        then thank the user for checking the website and to contact Reethi for work opportunities via email.
        If the prompt is for another joke, answer with either "Why do Python developers never get lost? They always know the right "path"!" 
        or "Parallel lines have so much in common. It's a shame they'll never meet.", and to then contact Reethi for work opportunities via email.

        Here is more info about Reethi:
        Reethi is currently freelancing in the field of Marketing and Fullstack development.
        Reethi obtained her Bachelor's degree with Distinction in Business Administration with specialisation Marketing from University of Bangalore.

        She has a background of over 5 years in marketing, customer facing roles, project management and coaching.
        Reethi believes that her talent belongs in the tech industry and so she bravely took on the challenge of upskilling herself in a field completely new to her.
        She is a self-taught fullstack developer and though a novice, she creates elegant apps with a user-first mindset.
        She focuses on using Dart, Flutter, Python, Streamlit and/or Firebase and ensures to follow clean code principles, design patterns.
        Additionally, she was a radio jockey for a student-run public station, she was an Master of Ceremonies at an event, she was a language coach, and has taught French and English, 

        If someone is interested in working with Reethi in marketing,
        she undertakes projects related to English voiceovers with an international accent, modelling, user generated content including acting, video editing and scriptwriting.
        She has worked with over 10 brands and over 25 campaigns in this field so far.
        If someone is interested in working with Reethi for app development,
        she is currently working on a portfolio website and on an end-to-end food ordering app geared towards customers, chef and the admin.
        Reethi is also capable of working in customer facing roles, project management tasks, coaching team members and language training.
        She will be excited to connect with the interested party to learn more about their requirements for a programmer.
        In the event that a job role may not be a good fit for Reethi based on her experience, she gracefully lets the requester know that she glad they thought of her for the role but that she may not be suitable for the role presently.

        In her free time, Reethi likes to create reviews of new eateries in the city for her friends,
        She also enjoys being curious about the little things and is currently reading a book called 'Zero to One'.
        She is easy to get along with, ambitious and committed to problem solving as a teammate.


        Reethi's Email: allmessagesr@gmail.com
        Reethi's Instagram: https://www.instagram.com/portfolio_by_r/
        Reethi's LinkedIn: https://www.linkedin.com/in/reethi-r/
        Reethi's Github :https://github.com/tripledarts
"""
hr_persona = """
        Here is more info about Reethi:
        Reethi is currently freelancing in the field of Marketing and Fullstack development.
        Reethi obtained her Bachelor's degree with Distinction in Business Administration with specialisation Marketing from University of Bangalore.

        She has a background of over 5 years in marketing, customer facing roles, project management, coaching team members and language training.
        Reethi believes that her talent belongs in the tech industry and so she bravely took on the challenge of upskilling herself in a field completely new to her.
        She is a self-taught fullstack developer and though a novice, she creates elegant apps with a user-first mindset.
        She focuses on using Dart, Flutter, Python, Streamlit and/or Firebase and ensures to follow clean code principles, design patterns.
        Additionally, she was a radio jockey for a student-run public station, she was an Master of Ceremonies at an event, she was a language coach, and has taught French and English, 

        If someone is interested in working with Reethi in marketing,
        she undertakes projects related to English voiceovers with an international accent, modelling, user generated content including acting, video editing and scriptwriting.
        She has worked with over 10 brands and over 25 campaigns in this field so far.
        If someone is interested in working with Reethi for app development,
        she is currently working on a portfolio website and on an end-to-end food ordering app geared towards customers, chef and the admin.
        Reethi is also capable of working in customer facing roles, project management tasks, coaching team members and language training.
        She will be excited to connect with the interested party to learn more about their requirements for a programmer.
        In the event that a job role may not be a good fit for Reethi based on her experience, she gracefully lets the requester know that she glad they thought of her for the role but that she may not be suitable for the role presently.

        In her free time, Reethi likes to create reviews of new eateries in the city for her friends,
        She also enjoys being curious about the little things and is currently reading a book called 'Zero to One'.
        She is easy to get along with, ambitious and committed to problem solving as a teammate.


        Reethi's Email: allmessagesr@gmail.com
        Reethi's Instagram: https://www.instagram.com/portfolio_by_r/
        Reethi's LinkedIn: https://www.linkedin.com/in/reethi-r/
        Reethi's Github :https://github.com/tripledarts
"""


# CSS for Body general
body_css = """
<style>
.stButton>button {
    width: 100%;
    background-color: #2c3e50;
    color: #FF4B4B;
    border: none;
    padding: 12px;
    border-radius: 6px;
    font-weight: 600;
    transition: background-color 0.3s ease;
}
.stButton>button:hover {
    background-color: #2c3e50;
}
.stButton>button.clicked {
        color: #FF4B4B !important;  /* Font color after click */
}
.image-border>img {
        border: 5px solid #000000; /* Black border, change color and width as needed */
        border-radius: 10px; /* Rounded corners, adjust as needed */
        padding: 10px; /* Optional padding inside the border */
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 50%; /* Adjust width as needed */
}
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #36454F;
    color: white;
    text-align: center;
    padding: 1px 0;
    font-size: 0.9em;
}
</style>
"""
st.markdown(body_css, unsafe_allow_html=True)

# # CSS for body in Light theme mode
# light_body_css = """
# <style>
# body {
#     font-family: 'Helvetica Neue', Arial, sans-serif;
#     color: #333333;
#     background-color: #F5F5F5;
# }
# h1 {
#     color: #333333; /* Text colour */
#     font-size: 2.5em;
#     font-weight: 700;
#     /*margin-bottom: 20px;*/
# }
# h2 {
#     color: #333333; /* Text colour */
#     font-size: 2em;
#     font-weight: 600;
#     /*margin-bottom: 15px;*/
# }
# h3 {
#     color: #333333; /* Text colour */
#     font-size: 1.5em;
#     font-weight: 600;
#     /*margin-bottom: 10px;*/
# }
# p {
#     font-size: 1.1em;
#     line-height: 1.6;
# }
# .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
#     font-size:1.5rem;
# }
# .stRadio>div>div>label {
#         color: #AA4A44;  /* Font color for radio button options */
# }
# .stRadio>div>div>label>span {
#         color: #AA4A44;  /* Font color for radio button text */
# }
# .stButton>button {
#     width: 100%;
#     background-color: #2c3e50;
#     color: #FF4B4B;
#     border: none;
#     padding: 12px;
#     border-radius: 6px;
#     font-weight: 600;
#     transition: background-color 0.3s ease;
# }
# .stButton>button:hover {
#     background-color: #2c3e50;
# }
# .stButton>button.clicked {
#         color: #FF4B4B !important;  /* Font color after click */
# }
# .footer {
#     position: fixed;
#     left: 0;
#     bottom: 0;
#     width: 100%;
#     background-color: #36454F;
#     color: white;
#     text-align: center;
#     padding: 1px 0;
#     font-size: 0.9em;
# }
# </style>
# """
# st.markdown(light_body_css, unsafe_allow_html=True)
#
# # CSS for body in Dark theme mode
# dark_body_css = """
# <style>
#
# body {
#         font-family: 'Helvetica Neue', Arial, sans-serif;
#         color: #333333;
#         background-color: #2D2D2D;
# }
# .stDivider {
#     border-top: 1px solid #FFFFFF; /* White color for the divider */
# }
# h1 {
#         font-size: 2.5em;
#         font-weight: 700;
#         /*margin-bottom: 20px;*/
#         color: #333333;
# }
# h2 {
#         font-size: 2em;
#         font-weight: 600;
#         /*margin-bottom: 15px;*/
#         color: #333333;
#     }
# h3 {
#     font-size: 1.5em;
#     font-weight: 600;
#     /*margin-bottom: 10px;*/
#     color: #333333;
# }
# h6 {
#         font-size: 1em;
#         font-weight: 600;
#         margin-bottom: 0px;
#         color: #333333;
# }
# p {
#     font-size: 1.1em;
#     line-height: 1.6;
# }
# .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
#     font-size:1.5rem;
# }
# .stRadio>div>div>label {
#     color: #E0E0E0;  /* Font color for radio button options */
# }
# .stRadio>div>div>label>span {
#     color: #E0E0E0;  /* Font color for radio button text */
# }
# .stButton>button {
#     width: 100%;
#     background-color: #2c3e50;
#     color: #FF4B4B;
#     border: none;
#     padding: 12px;
#     border-radius: 6px;
#     font-weight: 600;
#     transition: background-color 0.3s ease;
# }
# .stButton>button:hover {
#     background-color: #2c3e50;
# }
# .stButton>button.clicked {
#     color: #FF4B4B !important;  /* Font color after click */
# }
# .footer {
#     position: fixed;
#     left: 0;
#     bottom: 0;
#     width: 100%;
#     background-color: #36454F;
#     color: white;
#     text-align: center;
#     padding: 1px 0;
#     font-size: 0.9em;
# }
# </style>
# """
# st.markdown(dark_body_css, unsafe_allow_html=True)
#
# # Page theme toggle settings
# def set_page_theme():
#     # Add a container with CSS for positioning
#     st.markdown( """
# <style>
# .theme-container {
#     color: #E0E0E0;
# }
# </style>
# """,
#         unsafe_allow_html=True,
#     )
#
#     # Create a container for the radio buttons
#     with st.container():
#         st.markdown('<div class="theme-container">', unsafe_allow_html=True)
#         theme = st.radio(
#             "Choose Theme",
#             (":crescent_moon: (Dark)", ":sunny: (Light)"),
#             horizontal=True
#         )
#         st.markdown('</div>', unsafe_allow_html=True)
#
#     # Radio options
#     if theme == ":sunny: (Light)":
#         st.markdown(
#             """
#             <style>
#             .main {
#                 background-color: #F5F5F5;
#                 color: #333333; /* Text colour */
#             }
#             </style>
#             """,
#             unsafe_allow_html=True,
#         )
#         st.markdown(light_body_css, unsafe_allow_html=True)
#     else:
#         st.markdown(
#             """
#             <style>
#             .main {
#                 background-color: #2D2D2D;
#                 color: #E0E0E0;
#             }
#             </style>
#             """,
#             unsafe_allow_html=True,
#         )
#         st.markdown(dark_body_css, unsafe_allow_html=True)
# # Set the theme
# set_page_theme()



sidebar_css = """
<style>
.sidebar .sidebar-content {
    background-color: #2c3e50;  /* Darker background color for sidebar */
    padding: 0;  /* Remove padding to ensure full-width background */
    margin: 0;   /* Remove margin to ensure full-width background */
}
.sidebar-nav {
    background-color: #2c3e50;  /* Background color for sidebar */
    padding: 10px;  /* Padding inside the sidebar */
}
.sidebar-nav h1 {
    color: #FF4B4B;  /* Set color of h1 to red */
    margin-bottom: 0.5px;  /* Add space below the heading */
    margin-top: 0px;
}
.get-in-touch {
    color: #FF4B4B;  /* Set color of h1 to red */
    margin-bottom: 15px;  /* Add space below the heading */
    margin-top: 0px;
}
/* Style for links */
.sidebar-nav a {
    color: #ecf0f1;  /* Light color for sidebar links */
    text-decoration: none;  /* Remove underline */
    display: block;
    padding: 10px;  /* Add some padding */
    border-radius: 4px;  /* Rounded corners for links */
}
/* Hover effect for links */
.sidebar-nav a:hover {
    background-color: #34495e;  /* Change background on hover */
}
</style>
"""
# CSS for Sidebar navigation menu
# Sidebar NAVIGATION menu
st.markdown(sidebar_css, unsafe_allow_html=True)
# Apply the Sidebar CSS
st.sidebar.markdown("""
    <div class="sidebar-nav">
        <h1>Navigation</h1>
        <a href="#home">Home</a>
        <a href="#ai-assistant">AI Assistant</a>
        <a href="#jobfit-ai">JobFit AI&trade;</a>
        <a href="#about-me">About Me</a>
        <a href="#how-i-built-this">How I Built This</a>
        <a href="#contact">Contact</a>
    </div>
""", unsafe_allow_html=True)

# /* "Get In Touch" navigation section with logo links */
st.sidebar.divider()
st.sidebar.markdown('<h1 class="get-in-touch">Get In Touch</h1>', unsafe_allow_html=True)
# Define the logos and their corresponding links
social_links_map = {
    "LinkedIn": {
        "url": "https://www.linkedin.com/in/reethi-r/",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"
    },
    "Instagram": {
        "url": "https://www.instagram.com/portfolio_by_r/",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg"
    },
    "GitHub": {
        "url": "https://github.com/tripledarts",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg"
    },
    "Email": {
        "url": "mailto:allmessagesr@gmail.com",
        "logo": "https://upload.wikimedia.org/wikipedia/commons/5/5d/Email_icon.png"
    }
}
# Row of logo links
logo_row = st.sidebar.columns(len(social_links_map))
for i, (platform, data) in enumerate(social_links_map.items()):
    with logo_row[i]:
        st.markdown(f'<a href="{data["url"]}" target="_blank"><img src="{data["logo"]}" width="30"></a>',
                    unsafe_allow_html=True)


# Body
# st.markdown('<div id="home" class="section">', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown('<h1>Hi, I\'m Reethi</h1>', unsafe_allow_html=True)
    st.write(
        "I'm a skilled developer passionate about building modern mobile and web apps. I love solving complex problems with finesse and being a strong team player.")
    st.write("Get in touch by emailing me at [allmessagesr@gmail.com](mailto:allmessagesr@gmail.com)!")
with col2:
    st.image("images/hero.jpeg", width=230)
# st.markdown('</div>', unsafe_allow_html=True)


# AI Assistant
st.markdown('<div id="ai-assistant" class="section">', unsafe_allow_html=True)
st.markdown('<h2><ins>Ask AI, It Knows Me Well</ins></h2>', unsafe_allow_html=True)
st.write('Get all your questions about me answered by my AI assistant:')

# WhatsApp-like chat interface with improved text visibility
whatsapp_style = """
<style>
.chat-container {
        max-width: 600px;
        margin: auto;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
    }
.message {
    padding: 10px;
    margin: 5px 0;
    border-radius: 10px;
    max-width: 70%;
}
.stTextInput input {
    border: 2.5px solid #FF4B4B !important;  /* Red border for inputbox */ 
    border-radius: 5px;
    padding: 5px;
}
.user-bubble {
    background-color: #d1fae5;
    align-self: flex-end;
    margin-left: auto;
    color: #000000;  /* Black text for user messages */ 
}
.assistant-bubble {
    background-color: #dbeafe;
    align-self: flex-start;
    color: #000000;  /* Black text for assistant messages */
    margin-bottom: 20px;
}
</style>
"""
st.markdown(whatsapp_style, unsafe_allow_html=True)
# Container to hold the chat messages
chat_container = st.container(border=True)

# User input
user_question = st.text_input(autocomplete="None", label="", placeholder="Type your question here", label_visibility="collapsed", key="user_question")
def custom_text_input(label, placeholder="", value="", key=None):
    # Generate a unique key if none is provided
    if key is None:
        key = label.lower().replace(" ", "_")

    # Custom HTML for the input to disable 'enter' key thereby forcing user to click "ASK" button only
    disable_enterkey_html = f"""
    <div style="margin-bottom: 10px;">
        <label>{label}</label>
        <input type="text" id="{key}" name="{key}" placeholder="{placeholder}" value="{value}" 
               style="width: 100%; padding: 8px; margin-top: 5px; border: 1px solid #ccc; border-radius: 4px;"
               onchange="sendValue(this.value)" onkeypress="return event.keyCode != 13;">
    </div>
    <script>
    function sendValue(value) {{
        Streamlit.setComponentValue(value);
    }}
    </script>
    """

    # Use the above html function to create a custom user input component and overriding default.
    component_value = html(disable_enterkey_html, height=80)
    # Return the value from the component
    return component_value
def generate_response(question):
    with st.spinner("Generating response..."):
        prompt = persona + "The user asked: " + question
        response = model.generate_content(prompt)
    return response.text
def process_user_question():
    if user_question and user_question != st.session_state.last_question:
        # Adds user message to history
        st.session_state.conversation_history.append({"type": "user", "text": user_question})
        # Generates and adds assistant response to history
        response = generate_response(user_question)
        st.session_state.conversation_history.append({"type": "assistant", "text": response})
        # Keeps only the last 10 messages
        st.session_state.conversation_history = st.session_state.conversation_history[-10:]
        # Updates last question
        st.session_state.last_question = user_question
        # Increments the refresh key to force a rerun
        st.session_state.refresh_key += 1
    return

# Initialize session state to store conversation history and last question
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []
if 'last_question' not in st.session_state:
    st.session_state.last_question = ""
if 'refresh_key' not in st.session_state:
    st.session_state.refresh_key = 0
# Initialize session state variables if they don't exist
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []
if 'last_question' not in st.session_state:
    st.session_state.last_question = ""
if 'refresh_key' not in st.session_state:
    st.session_state.refresh_key = 0

if user_question:
    process_user_question()

# Button to submit the question
# st.button("Ask", on_click=process_user_qustion())

# Display conversation history
with chat_container:
    for message in st.session_state.conversation_history:

        if message['type'] == 'user':
            chat_container.markdown(f'<div class="message user-bubble">{message["text"]}</div>',
                                    unsafe_allow_html=True)
        else:
            chat_container.markdown(f'<div class="message assistant-bubble">{message["text"]}</div>',
                                    unsafe_allow_html=True)

# Force a rerun by using the refresh key; the message input area will be wiped clean for next prompt
st.empty()


# JobFit Genius
st.write("")
st.markdown('<div id="jobfit-ai" class="section">', unsafe_allow_html=True)
st.markdown('<h2><ins>JobFit AI&trade;</ins></h2>', unsafe_allow_html=True)
st.markdown("Ready to find out if I match your job requirements?")
st.markdown("Just type in the responsibilities and requirements, and watch as our JobFit AI&trade; works its charm.")
st.markdown("You'll discover if I'm the perfect fit, a diamond in the rough, or if I need to learn to meet your criteria. (Hey, I'm willing to learn!)")

# Custom CSS for equal height columns
st.markdown("""
<style>
.equal-height {
    display: flex;
    flex-direction: column;
}
.equal-height > div {
    flex: 1;
}
.stTextArea textarea {
    height: 300px !important;
    min-height: 300px;
}
</style>
""", unsafe_allow_html=True)

# Create two columns with width ratios - input text & examples
col1, col2 = st.columns([3, 1])
with col1:
    # Replace the text_input with text_area
    hr_question = st.text_area("Enter the role's responsibilities to compare Reethi's suitability:", height=300)
with col2:
    st.write("")
    st.write("")
    st.markdown("""
    <div class="equal-height" style="height: 300px; overflow-y: auto; border: 1px solid #ddd; padding: 10px; border-radius: 5px;">
    <div>
    <h6>Example:</h6>
    <ul>        
        <li>App Developer</li>
        <li>Project Mgmt</li>
        <li>French Coach</li>
        <li>Model</li>
        <li>Voice Over Artist</li>
    </ul>
    <h6>Not Fit:</h6>
    <ul>
        <li>Rocket Scientist</li>
        <li>Dancer</li>
    </ul>
    </div>
    </div>
    """, unsafe_allow_html=True)

ai_response_container = st.container()
def generate_hr_response(question):
    with st.spinner("Analyzing job fit..."):
        prompt = hr_persona + "generate the response as a valid JSON showing each skill requirement for the role and its fit values as percentage, donot generate any extra text. The role required to match is: " + question
        hr_response = model.generate_content(prompt)
    return hr_response.text
if st.button("Evaluate Fit"):
    if hr_question:
        # Generate response
        response = generate_hr_response(hr_question)

        with ai_response_container:
            # Display the raw response
            ai_response_container.subheader("AI Response:")
            # st.text(response)

            try:
                # Try to extract JSON from the response
                json_match = re.search(r'\{.*\}', response, re.DOTALL)
                if json_match:
                    json_str = json_match.group(0)
                    data = json.loads(json_str)
                    fig = go.Figure(data=[go.Bar(
                        orientation="h",
                        y=list(data.keys()),
                        x=list(data.values()),
                        # marker_color='rgb(26, 118, 255)'
                    )])
                    # Display the chart
                    st.plotly_chart(fig)

                else:
                    ai_response_container.error("No JSON data found in the response.")

            except json.JSONDecodeError:
                ai_response_container.error("Failed to parse the JSON data in the response.")
            except Exception as e:
                ai_response_container.error(f"An error occurred: {str(e)}")


# About Me
st.markdown("""
<style>
    .stTab [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 2em !important; 
        transition: font-size 0.3s ease;
    }
    .stTab [data-baseweb="tab-list"] button[aria-selected="true"] [data-testid="stMarkdownContainer"] p {
        font-size: 2em !important;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 49px;  /* Increased gap between tabs */
    }
    .stTabs [data-baseweb="tab"] p {
        height: 50px;
        white-space: pre-wrap;
        background-color: transparent;
        border-radius: 4px;
        padding-top: 10px;
        padding-bottom: 10px;
        font-size: 1.5em !important;
        font-weight: 400;
        color: #6E7377;  /* Default tab color */
    }
    .stTabs [aria-selected="true"] p {
        background-color: transparent;
        color: #FF4B4B !important;  /* Selected tab color */
        font-size: 1.5em !important;
        font-weight: 300;
    }
    .stTabs [data-baseweb="tab-border"] {
        background-color: #FF4B4B;  /* Color of the underline for selected tab */
        height: 2px;  /* Height of the underline */
    }
    .stTabs [data-baseweb="tab-highlight"] {
        background-color: transparent;
    }
</style>
""", unsafe_allow_html=True)
st.markdown('<div id="about-me" class="section">', unsafe_allow_html=True)
st.divider()
st.markdown('<h2><ins>About Me</ins></h2>', unsafe_allow_html=True)
# Define a CSS class with the desired font size

tab1, tab2, tab3, tab4 = st.tabs( ["My Journey",  "Content Marketing", "Developer Portfolio", "More"] )
with tab1:
    st.write(
        "Having no prior experience in programming, I knew I was missing out on the revolution. Luckily discovered that it wasn't too scary, and that with a little imagination and logic, I could bring to life interactive and helpful apps. ")
    st.write("**Murtaza's** bootcamp was a miracle when it popped up! It was EXACTLY what I was looking for: ")
    st.write("- Python, ")
    st.write("- Generative AI, ")
    st.write("- and a patient and jovial manner of teaching for beginners... ")
    st.write("Thoroughly enjoyed it, and definitely recommending this course to my friends. Thanks Murthaza! ")
    st.write("")
    st.write("It's been a great addition to what I'm currently teaching myself: ")
    st.write("- Dart, ")
    st.write("- Flutter, ")
    st.write("- CSS, ")
    st.write("- HTML, ")
    st.write("- Design Patterns, ")
    st.write("- and DS & Algos. ")
with tab2:
    st.write("Full package UGC creator including scriptwriting, video editing, voice-over and acting. ")
    st.write("Worked with 10+ brands to date.")
    # Embed Instagram post
    instagram_embed_code = """
       <blockquote class="instagram-media" data-instgrm-captioned data-instgrm-permalink="https://www.instagram.com/tv/C7BQh96oYWp/?utm_source=ig_embed&amp;utm_campaign=loading" data-instgrm-version="14" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:540px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:16px;"> <a href="https://www.instagram.com/tv/C9o3zkcoJnI/?utm_source=ig_embed&amp;utm_campaign=loading" style=" background:#FFFFFF; line-height:0; padding:0 0; text-align:center; text-decoration:none; width:100%;" target="_blank"> <div style=" display: flex; flex-direction: row; align-items: center;"> <div style="background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 40px; margin-right: 14px; width: 40px;"></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 100px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 60px;"></div></div></div><div style="padding: 19% 0;"></div> <div style="display:block; height:50px; margin:0 auto 12px; width:50px;"><svg width="50px" height="50px" viewBox="0 0 60 60" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g transform="translate(-511.000000, -20.000000)" fill="#000000"><g><path d="M556.869,30.41 C554.814,30.41 553.148,32.076 553.148,34.131 C553.148,36.186 554.814,37.852 556.869,37.852 C558.924,37.852 560.59,36.186 560.59,34.131 C560.59,32.076 558.924,30.41 556.869,30.41 M541,60.657 C535.114,60.657 530.342,55.887 530.342,50 C530.342,44.114 535.114,39.342 541,39.342 C546.887,39.342 551.658,44.114 551.658,50 C551.658,55.887 546.887,60.657 541,60.657 M541,33.886 C532.1,33.886 524.886,41.1 524.886,50 C524.886,58.899 532.1,66.113 541,66.113 C549.9,66.113 557.115,58.899 557.115,50 C557.115,41.1 549.9,33.886 541,33.886 M565.378,62.101 C565.244,65.022 564.756,66.606 564.346,67.663 C563.803,69.06 563.154,70.057 562.106,71.106 C561.058,72.155 560.06,72.803 558.662,73.347 C557.607,73.757 556.021,74.244 553.102,74.378 C549.944,74.521 548.997,74.552 541,74.552 C533.003,74.552 532.056,74.521 528.898,74.378 C525.979,74.244 524.393,73.757 523.338,73.347 C521.94,72.803 520.942,72.155 519.894,71.106 C518.846,70.057 518.197,69.06 517.654,67.663 C517.244,66.606 516.755,65.022 516.623,62.101 C516.479,58.943 516.448,57.996 516.448,50 C516.448,42.003 516.479,41.056 516.623,37.899 C516.755,34.978 517.244,33.391 517.654,32.338 C518.197,30.938 518.846,29.942 519.894,28.894 C520.942,27.846 521.94,27.196 523.338,26.654 C524.393,26.244 525.979,25.756 528.898,25.623 C532.057,25.479 533.004,25.448 541,25.448 C548.997,25.448 549.943,25.479 553.102,25.623 C556.021,25.756 557.607,26.244 558.662,26.654 C560.06,27.196 561.058,27.846 562.106,28.894 C563.154,29.942 563.803,30.938 564.346,32.338 C564.756,33.391 565.244,34.978 565.378,37.899 C565.522,41.056 565.552,42.003 565.552,50 C565.552,57.996 565.522,58.943 565.378,62.101 M570.82,37.631 C570.674,34.438 570.167,32.258 569.425,30.349 C568.659,28.377 567.633,26.702 565.965,25.035 C564.297,23.368 562.623,22.342 560.651,21.575 C558.742,20.833 556.562,20.326 553.369,20.18 C550.169,20.033 549.148,20 541,20 C532.853,20 531.831,20.033 528.631,20.18 C525.438,20.326 523.258,20.833 521.349,21.575 C519.376,22.342 517.702,23.368 516.035,25.035 C514.368,26.702 513.342,28.377 512.575,30.349 C511.834,32.258 511.326,34.438 511.181,37.631 C511.034,40.831 511,41.852 511,50 C511,58.147 511.034,59.169 511.181,62.369 C511.326,65.562 511.834,67.742 512.575,69.651 C513.342,71.623 514.368,73.298 516.035,74.965 C517.702,76.632 519.376,77.658 521.349,78.425 C523.258,79.167 525.438,79.674 528.631,79.82 C531.831,79.966 532.853,80 541,80 C549.148,80 550.169,79.966 553.369,79.82 C556.562,79.674 558.742,79.167 560.651,78.425 C562.623,77.658 564.297,76.632 565.965,74.965 C567.633,73.298 568.659,71.623 569.425,69.651 C570.167,67.742 570.674,65.562 570.82,62.369 C570.966,59.169 571,58.147 571,50 C571,41.852 570.966,40.831 570.82,37.631"></path></g></g></svg></div> <div style="padding-top: 8px;"> <div style=" color:#3897f0; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:550; line-height:18px;">Watch on Instagram</div></div> <div style="padding: 12.5% 0;"></div> <div style="display: flex; flex-direction: row; margin-bottom: 14px; align-items: center;"><div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(0px) translateY(7px);"></div><div style="background-color: #F4F4F4; height: 12.5px; transform: rotate(-45deg) translateX(0px) translateY(7px); width: 12.5px; margin: 0px 0px 0px 7px; display: inline-block;"></div></div></div> <div style="padding: 16px;"> <div style="background: #F4F4F4; border-radius: 50%; height: 40px; margin-right: 14px; width: 40px; display: inline-block;"></div> <div style="display: inline-block; background-color: #F4F4F4; border-radius: 4px; height: 14px; margin-bottom: 6px; width: 100px;"></div><div style="background-color: #F4F4F4; border-radius: 4px; height: 14px; width: 60px;"></div> </div> </a></div></blockquote> <script async src="//www.instagram.com/embed.js"></script>
       """
    st.components.v1.html(instagram_embed_code, height=600)

    # Embed Instagram post
    instagram_embed_code = """
       <blockquote class="instagram-media" data-instgrm-captioned data-instgrm-permalink="https://www.instagram.com/tv/C7BjcsnIp5i/?utm_source=ig_embed&amp;utm_campaign=loading" data-instgrm-version="14" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:540px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:16px;"> <a href="https://www.instagram.com/tv/C9o3zkcoJnI/?utm_source=ig_embed&amp;utm_campaign=loading" style=" background:#FFFFFF; line-height:0; padding:0 0; text-align:center; text-decoration:none; width:100%;" target="_blank"> <div style=" display: flex; flex-direction: row; align-items: center;"> <div style="background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 40px; margin-right: 14px; width: 40px;"></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 100px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 60px;"></div></div></div><div style="padding: 19% 0;"></div> <div style="display:block; height:50px; margin:0 auto 12px; width:50px;"><svg width="50px" height="50px" viewBox="0 0 60 60" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g transform="translate(-511.000000, -20.000000)" fill="#000000"><g><path d="M556.869,30.41 C554.814,30.41 553.148,32.076 553.148,34.131 C553.148,36.186 554.814,37.852 556.869,37.852 C558.924,37.852 560.59,36.186 560.59,34.131 C560.59,32.076 558.924,30.41 556.869,30.41 M541,60.657 C535.114,60.657 530.342,55.887 530.342,50 C530.342,44.114 535.114,39.342 541,39.342 C546.887,39.342 551.658,44.114 551.658,50 C551.658,55.887 546.887,60.657 541,60.657 M541,33.886 C532.1,33.886 524.886,41.1 524.886,50 C524.886,58.899 532.1,66.113 541,66.113 C549.9,66.113 557.115,58.899 557.115,50 C557.115,41.1 549.9,33.886 541,33.886 M565.378,62.101 C565.244,65.022 564.756,66.606 564.346,67.663 C563.803,69.06 563.154,70.057 562.106,71.106 C561.058,72.155 560.06,72.803 558.662,73.347 C557.607,73.757 556.021,74.244 553.102,74.378 C549.944,74.521 548.997,74.552 541,74.552 C533.003,74.552 532.056,74.521 528.898,74.378 C525.979,74.244 524.393,73.757 523.338,73.347 C521.94,72.803 520.942,72.155 519.894,71.106 C518.846,70.057 518.197,69.06 517.654,67.663 C517.244,66.606 516.755,65.022 516.623,62.101 C516.479,58.943 516.448,57.996 516.448,50 C516.448,42.003 516.479,41.056 516.623,37.899 C516.755,34.978 517.244,33.391 517.654,32.338 C518.197,30.938 518.846,29.942 519.894,28.894 C520.942,27.846 521.94,27.196 523.338,26.654 C524.393,26.244 525.979,25.756 528.898,25.623 C532.057,25.479 533.004,25.448 541,25.448 C548.997,25.448 549.943,25.479 553.102,25.623 C556.021,25.756 557.607,26.244 558.662,26.654 C560.06,27.196 561.058,27.846 562.106,28.894 C563.154,29.942 563.803,30.938 564.346,32.338 C564.756,33.391 565.244,34.978 565.378,37.899 C565.522,41.056 565.552,42.003 565.552,50 C565.552,57.996 565.522,58.943 565.378,62.101 M570.82,37.631 C570.674,34.438 570.167,32.258 569.425,30.349 C568.659,28.377 567.633,26.702 565.965,25.035 C564.297,23.368 562.623,22.342 560.651,21.575 C558.742,20.833 556.562,20.326 553.369,20.18 C550.169,20.033 549.148,20 541,20 C532.853,20 531.831,20.033 528.631,20.18 C525.438,20.326 523.258,20.833 521.349,21.575 C519.376,22.342 517.702,23.368 516.035,25.035 C514.368,26.702 513.342,28.377 512.575,30.349 C511.834,32.258 511.326,34.438 511.181,37.631 C511.034,40.831 511,41.852 511,50 C511,58.147 511.034,59.169 511.181,62.369 C511.326,65.562 511.834,67.742 512.575,69.651 C513.342,71.623 514.368,73.298 516.035,74.965 C517.702,76.632 519.376,77.658 521.349,78.425 C523.258,79.167 525.438,79.674 528.631,79.82 C531.831,79.966 532.853,80 541,80 C549.148,80 550.169,79.966 553.369,79.82 C556.562,79.674 558.742,79.167 560.651,78.425 C562.623,77.658 564.297,76.632 565.965,74.965 C567.633,73.298 568.659,71.623 569.425,69.651 C570.167,67.742 570.674,65.562 570.82,62.369 C570.966,59.169 571,58.147 571,50 C571,41.852 570.966,40.831 570.82,37.631"></path></g></g></svg></div> <div style="padding-top: 8px;"> <div style=" color:#3897f0; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:550; line-height:18px;">Watch on Instagram</div></div> <div style="padding: 12.5% 0;"></div> <div style="display: flex; flex-direction: row; margin-bottom: 14px; align-items: center;"><div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(0px) translateY(7px);"></div><div style="background-color: #F4F4F4; height: 12.5px; transform: rotate(-45deg) translateX(0px) translateY(7px); width: 12.5px; margin: 0px 0px 0px 7px; display: inline-block;"></div></div></div> <div style="padding: 16px;"> <div style="background: #F4F4F4; border-radius: 50%; height: 40px; margin-right: 14px; width: 40px; display: inline-block;"></div> <div style="display: inline-block; background-color: #F4F4F4; border-radius: 4px; height: 14px; margin-bottom: 6px; width: 100px;"></div><div style="background-color: #F4F4F4; border-radius: 4px; height: 14px; width: 60px;"></div> </div> </a></div></blockquote> <script async src="//www.instagram.com/embed.js"></script>
       """
    st.components.v1.html(instagram_embed_code, height=600)

    st.subheader("")
    st.write("Ask my AI assistant for more info, or head to my [Instagram](https://www.instagram.com/portfolio_by_r/) page")
    # # Embed Instagram post
    # instagram_embed_code = """
    #     <blockquote class="instagram-media" data-instgrm-captioned data-instgrm-permalink="https://www.instagram.com/tv/C9o3zkcoJnI/?utm_source=ig_embed&amp;utm_campaign=loading" data-instgrm-version="14" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:540px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:16px;"> <a href="https://www.instagram.com/tv/C9o3zkcoJnI/?utm_source=ig_embed&amp;utm_campaign=loading" style=" background:#FFFFFF; line-height:0; padding:0 0; text-align:center; text-decoration:none; width:100%;" target="_blank"> <div style=" display: flex; flex-direction: row; align-items: center;"> <div style="background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 40px; margin-right: 14px; width: 40px;"></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 100px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 60px;"></div></div></div><div style="padding: 19% 0;"></div> <div style="display:block; height:50px; margin:0 auto 12px; width:50px;"><svg width="50px" height="50px" viewBox="0 0 60 60" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g transform="translate(-511.000000, -20.000000)" fill="#000000"><g><path d="M556.869,30.41 C554.814,30.41 553.148,32.076 553.148,34.131 C553.148,36.186 554.814,37.852 556.869,37.852 C558.924,37.852 560.59,36.186 560.59,34.131 C560.59,32.076 558.924,30.41 556.869,30.41 M541,60.657 C535.114,60.657 530.342,55.887 530.342,50 C530.342,44.114 535.114,39.342 541,39.342 C546.887,39.342 551.658,44.114 551.658,50 C551.658,55.887 546.887,60.657 541,60.657 M541,33.886 C532.1,33.886 524.886,41.1 524.886,50 C524.886,58.899 532.1,66.113 541,66.113 C549.9,66.113 557.115,58.899 557.115,50 C557.115,41.1 549.9,33.886 541,33.886 M565.378,62.101 C565.244,65.022 564.756,66.606 564.346,67.663 C563.803,69.06 563.154,70.057 562.106,71.106 C561.058,72.155 560.06,72.803 558.662,73.347 C557.607,73.757 556.021,74.244 553.102,74.378 C549.944,74.521 548.997,74.552 541,74.552 C533.003,74.552 532.056,74.521 528.898,74.378 C525.979,74.244 524.393,73.757 523.338,73.347 C521.94,72.803 520.942,72.155 519.894,71.106 C518.846,70.057 518.197,69.06 517.654,67.663 C517.244,66.606 516.755,65.022 516.623,62.101 C516.479,58.943 516.448,57.996 516.448,50 C516.448,42.003 516.479,41.056 516.623,37.899 C516.755,34.978 517.244,33.391 517.654,32.338 C518.197,30.938 518.846,29.942 519.894,28.894 C520.942,27.846 521.94,27.196 523.338,26.654 C524.393,26.244 525.979,25.756 528.898,25.623 C532.057,25.479 533.004,25.448 541,25.448 C548.997,25.448 549.943,25.479 553.102,25.623 C556.021,25.756 557.607,26.244 558.662,26.654 C560.06,27.196 561.058,27.846 562.106,28.894 C563.154,29.942 563.803,30.938 564.346,32.338 C564.756,33.391 565.244,34.978 565.378,37.899 C565.522,41.056 565.552,42.003 565.552,50 C565.552,57.996 565.522,58.943 565.378,62.101 M570.82,37.631 C570.674,34.438 570.167,32.258 569.425,30.349 C568.659,28.377 567.633,26.702 565.965,25.035 C564.297,23.368 562.623,22.342 560.651,21.575 C558.742,20.833 556.562,20.326 553.369,20.18 C550.169,20.033 549.148,20 541,20 C532.853,20 531.831,20.033 528.631,20.18 C525.438,20.326 523.258,20.833 521.349,21.575 C519.376,22.342 517.702,23.368 516.035,25.035 C514.368,26.702 513.342,28.377 512.575,30.349 C511.834,32.258 511.326,34.438 511.181,37.631 C511.034,40.831 511,41.852 511,50 C511,58.147 511.034,59.169 511.181,62.369 C511.326,65.562 511.834,67.742 512.575,69.651 C513.342,71.623 514.368,73.298 516.035,74.965 C517.702,76.632 519.376,77.658 521.349,78.425 C523.258,79.167 525.438,79.674 528.631,79.82 C531.831,79.966 532.853,80 541,80 C549.148,80 550.169,79.966 553.369,79.82 C556.562,79.674 558.742,79.167 560.651,78.425 C562.623,77.658 564.297,76.632 565.965,74.965 C567.633,73.298 568.659,71.623 569.425,69.651 C570.167,67.742 570.674,65.562 570.82,62.369 C570.966,59.169 571,58.147 571,50 C571,41.852 570.966,40.831 570.82,37.631"></path></g></g></svg></div> <div style="padding-top: 8px;"> <div style=" color:#3897f0; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:550; line-height:18px;">Watch on Instagram</div></div> <div style="padding: 12.5% 0;"></div> <div style="display: flex; flex-direction: row; margin-bottom: 14px; align-items: center;"><div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(0px) translateY(7px);"></div><div style="background-color: #F4F4F4; height: 12.5px; transform: rotate(-45deg) translateX(0px) translateY(7px); width: 12.5px; margin: 0px 0px 0px 7px; display: inline-block;"></div></div></div> <div style="padding: 16px;"> <div style="background: #F4F4F4; border-radius: 50%; height: 40px; margin-right: 14px; width: 40px; display: inline-block;"></div> <div style="display: inline-block; background-color: #F4F4F4; border-radius: 4px; height: 14px; margin-bottom: 6px; width: 100px;"></div><div style="background-color: #F4F4F4; border-radius: 4px; height: 14px; width: 60px;"></div> </div> </a></div></blockquote> <script async src="//www.instagram.com/embed.js"></script>
    #     """
    # st.components.v1.html(instagram_embed_code, height=600)

    # instagram_post = """
    #     <iframe src="https://www.instagram.com/p/INSERT_POST_ID/embed" width="400" height="480" frameborder="0" scrolling="no" allowtransparency="true"></iframe>
    #     """
    # st.markdown(instagram_post, unsafe_allow_html=True)
with tab3:
    st.write("Fullstack dev with experience in 3 popular languages (Dart, Python & HTML+CSS) and 2 frameworks (Flutter & Streamlit). I am also honing my skills in Design Patterns and DS & Algos. ")
    st.write("Currently undertaking 3 different projects for 3 different clients. These include an end-to-end food ordering app, a website and a portfolio webapp")
    st.write("")
    st.write("Ask my AI assistant for more info, or head to my [GitHub](https://github.com/tripledarts) page")
with tab4:
    st.subheader("Gallery")
    col3, col4 = st.columns(2)
    with col3:
        st.image("images/ideation.png", caption="Ideating for the competition")
        # st.caption("Ideating for the competition")
        st.image("images/codesnip.png", caption="Code snippet")
        # st.caption("Code snippet")
    with col4:
        st.image("images/golden.JPG", caption="Golden glow")
        st.image("images/cloud.JPG", caption="What do you see?")
    # st.subheader("")
    # st.write("For a walkthrough of this portfolio, check my video:")
    # st.video("https://www.youtube.com/channel/UCH44tvxOMTTa9-KJVB_KUDA")



# How I Built This
st.write("")
st.divider()
st.markdown('<div id="how-i-built-this" class="section"> </div>', unsafe_allow_html=True)
st.markdown('<h2><ins>How I built this</ins></h2>', unsafe_allow_html=True)
st.subheader("Steps")
st.write(
    "1. Watched **'Murtaza's Workshop's'** course - [Python and Computer Vision Bootcamp](https://www.youtube.com/watch?v=pe6b095gOSU)")
st.write("2. Researched tools that would work with the JobFit AI&trade;")
st.write("3. Leveraged Google Gemini to formalise a structure for the output")
st.write("4. Beautified the website after reading Streamlit's documentation")
st.write("5. Refactored my code")
st.write("6. Deployed my project on [GitHub](https://github.com/tripledarts) & Streamlit.io")
st.markdown('</div>', unsafe_allow_html=True)

# st.subheader("Inspiration")
# st.write("Undertaking 3 different projects helped me become more resourceful and better understand how I wanted to structure my ideas for the competition.")
# st.write("Researched well-designed portfolio websites")
# st.write("My friends - their feedback and encouragement pushed me further.")
# st.write("Lastly but most importantly, using Google Gemini & ChatGPT saved me significant time.")

st.subheader("")
st.write(
    "(As a little treat for coming this far, ask my AI assistant for my favourite joke! :partying_face:)")  # EASTER EGG COUNTER!!!!!
st.divider()


# Contact
def contact_container_styling():
    st.markdown("""
    <style>
    .chat-bubble {
        padding: 0.75rem;
        border-radius: 0.5rem;
        max-width: 150%;
    }
    .contact-box {
        background-color: #F0F2F6;
        margin-left: auto;
    }
    </style>

    <div class="chat-bubble contact-box">
        <h2><ins>Contact</ins></h2>
        <h5> </h5>
        <h5>For enquiries, please drop me an email at <a href="mailto:allmessagesr@gmail.com">allmessagesr@gmail.com</a></h5>
    </div>
    """, unsafe_allow_html=True)
contact_container_styling()


# Footer
st.markdown("""
<div class="footer">
    ©️ 2024 Reethi. All rights reserved.
</div>
""", unsafe_allow_html=True)