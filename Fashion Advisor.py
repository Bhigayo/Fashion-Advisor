import streamlit as st
from PIL import Image
import random

# Placeholder data (replace with actual AI/database integration)
wardrobe = {
    "tops": ["Red T-shirt", "Blue Blouse", "Striped Sweater"],
    "bottoms": ["Jeans", "Black Skirt", "Khaki Pants"],
    "shoes": ["Sneakers", "Boots", "Sandals"],
    "accessories": ["Scarf", "Necklace", "Hat"]
}

trends = ["Oversized Clothing", "Pastel Colors", "Athleisure"]

body_types = ["Rectangle", "Triangle", "Inverted Triangle", "Hourglass", "Round"]

def get_random_outfit(top, bottom, shoes, accessory):
    return f"{top}, {bottom}, {shoes}, and a {accessory}."

def suggest_outfit(user_tops, user_bottoms, user_shoes, user_accessories, user_trend, user_body_type):
    """Generates an outfit suggestion based on user input."""

    if not user_tops or not user_bottoms or not user_shoes or not user_accessories:
        return "Please select items from your wardrobe."

    random_top = random.choice(user_tops)
    random_bottom = random.choice(user_bottoms)
    random_shoes = random.choice(user_shoes)
    random_accessory = random.choice(user_accessories)

    outfit = get_random_outfit(random_top, random_bottom, random_shoes, random_accessory)

    if user_trend:
        outfit += f" Keeping in line with the '{user_trend}' trend."

    if user_body_type:
        outfit += f" Designed to flatter a '{user_body_type}' body type."

    return outfit

st.title("AI Fashion Advisor")

st.write("Let's create a stylish outfit for you!")

# User input for wardrobe
st.subheader("Your Wardrobe")

user_tops = st.multiselect("Select your tops:", wardrobe["tops"])
user_bottoms = st.multiselect("Select your bottoms:", wardrobe["bottoms"])
user_shoes = st.multiselect("Select your shoes:", wardrobe["shoes"])
user_accessories = st.multiselect("Select your accessories:", wardrobe["accessories"])
import openai #import the library
import streamlit as st

# Replace "YOUR_API_KEY" with your actual API key
openai.api_key = ""

def get_fashion_advice(prompt):
    """Uses OpenAI to get fashion advice."""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Or another suitable engine
            prompt=prompt,
            max_tokens=150,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Sorry, I couldn't get fashion advice right now. Error: {e}"

st.title("AI Fashion Advisor")

user_question = st.text_input("Ask me a fashion question:")

if st.button("Get Advice"):
    if user_question:
        advice = get_fashion_advice(user_question)
        st.write(advice)
    else:
        st.write("Please ask a question.")
# User input for trends and body type
st.subheader("Preferences")

user_trend = st.selectbox("Select a trend (optional):", ["None"] + trends)
user_trend = user_trend if user_trend != "None" else None

user_body_type = st.selectbox("Select your body type (optional):", ["None"] + body_types)
user_body_type = user_body_type if user_body_type != "None" else None

# Generate outfit suggestion
if st.button("Generate Outfit"):
    outfit_suggestion = suggest_outfit(user_tops, user_bottoms, user_shoes, user_accessories, user_trend, user_body_type)
    st.subheader("Outfit Suggestion:")
    st.write(outfit_suggestion)

# Example images (replace with actual image generation/display)
st.subheader("Example Visuals (Placeholder)")
col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://placehold.co/150x200?text=Top", caption="Top", use_column_width=True)
with col2:
    st.image("https://placehold.co/150x200?text=Bottom", caption="Bottom", use_column_width=True)
with col3:
    st.image("https://placehold.co/150x200?text=Shoes", caption="Shoes", use_column_width=True)

st.write("Please remember that this is a simplified example. For a real-world application, you would need to integrate with a database to store user wardrobes, use a machine learning model for trend analysis and body type recommendations, and implement image generation or display.")