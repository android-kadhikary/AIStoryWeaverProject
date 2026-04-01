story-weaver/
├── .env                # API Keys (Gemini/Groq)
├── requirements.txt    # dependencies (streamlit, google-generativeai, python-dotenv)
├── app.py              # Main Streamlit UI and Logic
├── core/
│   ├── engine.py       # LLM API wrappers & Rate limit handling
│   └── prompts.py      # System prompts and template logic




1) pip install -r requirements.txt
    It will install 
    python-dotenv
    streamlit
    openai # best to use this or gemini model
    langchain-groq
2) create the .env fule with Groq api key and save