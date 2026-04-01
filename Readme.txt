story-weaver/
├── .env                # API Keys (Gemini/Groq)
├── requirements.txt    # dependencies (streamlit, google-generativeai, python-dotenv)
├── app.py              # Main Streamlit UI and Logic
├── core/
│   ├── engine.py       # LLM API wrappers & Rate limit handling
│   └── prompts.py      # System prompts and template logic
└── utils/
    ├── state.py        # Session state management
    └── export.py       # Markdown export logic



pip install streamlit google-generativeai python-dotenv