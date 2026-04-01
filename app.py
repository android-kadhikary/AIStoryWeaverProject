import streamlit as st
from core.engine import call_llm_with_retry
from core.prompts import SYSTEM_PROMPT

st.set_page_config(page_title="Story Weaver", layout="wide")

# Initialize State
if "history" not in st.session_state:
    st.session_state.history = []
if "started" not in st.session_state:
    st.session_state.started = False

# Sidebar Controls
st.sidebar.header("Story Settings")
genre = st.sidebar.selectbox("Genre", ["Fantasy", "Sci-Fi", "Mystery", "Romance", "Horror", "Comedy"])
temp = st.sidebar.slider("Creativity (Temperature)", 0.0, 1.0, 0.7)

# 1. Story Setup
if not st.session_state.started:
    st.title("✍️ AI Story Weaver")
    title = st.text_input("Story Title")
    hook = st.text_area("Initial Hook/Setting")
    
    if st.button("Start the Story"):
        full_prompt = f"{SYSTEM_PROMPT.format(genre=genre, character_list='None', current_arc='Intro')} \n\n Starting Hook: {hook}"
        opening = call_llm_with_retry(full_prompt, temp)
        st.session_state.history.append({"role": "ai", "content": opening})
        st.session_state.started = True
        st.rerun()

# 2. Main Storytelling View
else:
    st.title(f"📖 {genre} Tale")
    
    # Display full history
    for turn in st.session_state.history:
        if turn["role"] == "ai":
            st.markdown(f"*{turn['content']}*")
        else:
            st.info(turn['content'])

    # User Input
    user_input = st.text_input("Your contribution...")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Continue with AI"):
            if user_input:
                st.session_state.history.append({"role": "user", "content": user_input})
            
            # Send entire history
            context = "\n".join([t["content"] for t in st.session_state.history])
            ai_next = call_llm_with_retry(context, temp)
            st.session_state.history.append({"role": "ai", "content": ai_next})
            st.rerun()

    with col2:
        if st.button("Give Me Choices"):
            # logic for generating 3 options using a specific prompt...
            pass

    with col3:
        if st.button("Undo Last Turn"):
            if st.session_state.history:
                st.session_state.history.pop()
                st.rerun()