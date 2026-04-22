from crewai import LLM

def get_llm(model="llama-3.3-70b-versatile"):
    return LLM(
        model=f"groq/{model}",
        temperature=0.2
    )
