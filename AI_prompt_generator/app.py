import os
import streamlit as st
from openai import OpenAI
from prompt import PROMPT_CATEGORIES, build_generator_prompt


st.set_page_config(
    page_title="AI Prompt Generator",
    page_icon="🤖",
    layout="wide"
)


client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=st.secrets["HF_TOKEN"]
)



# -----------------------------
# UI
# -----------------------------

st.title("🤖 AI Prompt Generator")
st.write(
    "Create high-quality prompts using different prompt-engineering "
    "techniques."
)

st.divider()


# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:
    st.header("⚙️ Settings")

    category = st.selectbox(
        "Prompt Technique",
        list(PROMPT_CATEGORIES.keys())
    )

    model = st.text_input(
        "Model",
        value="moonshotai/Kimi-K2-Instruct-0905"
    )

    temperature = st.slider(
        "Creativity",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1
    )


# -----------------------------
# Main Form
# -----------------------------

st.subheader("1. Describe what you want")

task = st.text_area(
    "What should the AI do?",
    placeholder=(
        "Example: Build a modern e-commerce website "
        "using React and Tailwind CSS."
    ),
    height=120
)

context = st.text_area(
    "Context",
    placeholder=(
        "Example: The website is for a clothing brand "
        "targeting young customers."
    ),
    height=100
)

requirements = st.text_area(
    "Additional requirements",
    placeholder=(
        "Example: Use a dark theme, responsive design, "
        "and include authentication."
    ),
    height=100
)


st.subheader("2. Selected technique")

st.info(
    f"**{category}**\n\n"
    f"{PROMPT_CATEGORIES[category].strip()}"
)


# -----------------------------
# Generate
# -----------------------------

if st.button(
    "✨ Generate Prompt",
    type="primary",
    use_container_width=True
):

    if not task.strip():
        st.warning("Please describe what you want the AI to do.")
        st.stop()

    generator_prompt = build_generator_prompt(
        category=category,
        task=task,
        context=context,
        requirements=requirements
    )

    with st.spinner("Generating your prompt..."):

        try:
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": generator_prompt
                    }
                ],
                temperature=temperature
            )

            generated_prompt = (
                completion.choices[0]
                .message.content
            )

            st.session_state["generated_prompt"] = generated_prompt

        except Exception as e:
            st.error(f"Error generating prompt: {e}")


# -----------------------------
# Result
# -----------------------------

if "generated_prompt" in st.session_state:

    st.divider()

    st.subheader("3. Generated Prompt")

    generated_prompt = st.session_state["generated_prompt"]

    st.text_area(
        "Your prompt",
        value=generated_prompt,
        height=400
    )

    st.download_button(
        label="⬇️ Download Prompt",
        data=generated_prompt,
        file_name="generated_prompt.txt",
        mime="text/plain",
        use_container_width=True
    )