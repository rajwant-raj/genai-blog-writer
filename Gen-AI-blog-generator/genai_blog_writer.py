import streamlit as st
from transformers import pipeline, set_seed


st.title("📝 AI Blog Writer (GPT-Neo 1.3B)")
st.markdown("Generate detailed blog posts (8–10+ paragraphs) with an open-source LLM.")

@st.cache_resource
def load_model():
    return pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")

generator = load_model()
set_seed(42)

# 🧠 User Input
topic = st.text_input("Enter a blog topic", placeholder="e.g., Impact of AI on Modern Education")

# 🚀 Generate Blog
if st.button("Generate Blog"):
    if not topic.strip():
        st.warning("Please enter a topic to proceed.")
    else:
        with st.spinner("Generating  blog... Please wait (can take 15–20 sec)..."):
            prompt = f"Write a blog post on: {topic}\n\n"
            try:
                output = generator(
                    prompt,
                    max_length=1200,
                    do_sample=True,
                    temperature=0.7,
                    top_p=0.95,
                    repetition_penalty=1.2,
                    num_return_sequences=1
                )[0]['generated_text']
                st.success("✅ Blog Generated Successfully!")
                st.markdown("---")
                st.markdown(output)
            except Exception as e:
                st.error(f"Error: {e}")
