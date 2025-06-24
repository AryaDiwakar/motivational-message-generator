import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Motivational Message Generator")

st.title("Personalized Motivational Message Generator")

# Input Section
mood = st.selectbox(
    "How are you feeling today?",
    ["Happy", "Sad", "Excited", "Tired", "Stressed"]
)

goal = st.text_input("What's your focus or goal today? (e.g. work, fitness, study)")

if st.button("Generate Message"):
    if not goal.strip():
        st.warning("Please enter your goal to proceed!")
    else:
        # Load the model
        generator = pipeline("text-generation", model="gpt2")

        prompt = f"Write an uplifting motivational message for someone who feels {mood.lower()} and wants to focus on {goal}:"
        outputs = generator(
            prompt,
            max_length=50,
            num_return_sequences=3,
            temperature=0.8,
            top_p=0.95,
        )

        st.success("Here are your personalized motivational messages:")
        for idx, output in enumerate(outputs, 1):
            st.markdown(f"{idx}. {output['generated_text'].replace(prompt, '').strip()}")
