import os
import time
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

def call_llm_with_retry(prompt, temperature, model_name="llama-3.3-70b-versatile"):
    """
    Wraps the Groq API call with keyword arguments and basic retry logic.
    """
    # 1. Initialize the model with KEYWORD arguments
    # model = genai.GenerativeModel(model_name) # best use

    llm = ChatGroq(
        model=model_name,
        temperature=temperature,
        # Max retries is built into some LangChain versions, but we'll 
        # keep our custom loop for finer control over the UI feedback.
    )

    max_retries = 3
    for attempt in range(max_retries):
        try:
            # invoke() is the standard method for LangChain chat models
            response = llm.invoke(prompt)
            return response.content
        
        except Exception as e:
            err_msg = str(e).lower()
            # Handle Rate Limits (HTTP 429)
            if "429" in err_msg or "rate limit" in err_msg:
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt
                    time.sleep(wait_time)
                    continue
            
            # Re-raise the error so the UI can catch it and show a message
            raise e