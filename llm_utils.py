import ollama
from textwrap import dedent
from pdf_utils import clean_text

def rewrite_resume(resume_text: str, sample_resume_text: str) -> str:
    """Call LLM to rewrite resume in federal 2-page format."""
    prompt = dedent(f"""
    You are a professional federal resume writer. Rewrite the following resume so that it is 
    no more than 2 pages and follows the structure, tone, and style demonstrated in the 
    sample resumes below.

    Instructions:
    - Keep the resume concise, federal-compliant, and list all content in chronological order, newest to oldest.
    - Write plain text only. Do not use Markdown, bullets, special symbols, or '#' for section headers. Section headers must end with a colon (e.g., Profile:).
    - Use consistent headings: Profile, Employment History, Education, Skills, Awards (only if applicable), Certifications (only if applicable and not already listed).
    - If metrics are available then quantify achievements by including numbers, metrics, or data points to illustrate success otherwise leave content as is and do not make up metrics.
    - Use strong active verbs to describe work performed. Be specific and use your own words. Avoid vague phrases.
    - Be concise. Remove redundancies and fluff. Make every word count. Review the draft after a few days to refine.
    - Proofread for spelling, grammar, and typographical errors.
    - Ensure accuracy. Do not make up accomplishments, inflate responsibilities, or exaggerate skills.
    - Do not use personal pronouns (I, my, me).
    - Avoid acronyms unless widely understood.
    - Exclude personal information (hobbies, height, weight, age, date of birth, marital status, ethnicity, health, reasons for leaving previous jobs).
    - Remove any LinkedIn URLs or personal social media links.
    - Replace references with "References available upon request."
    - Do not exceed 2 pages."

    --- Sample Resume(s) ---
    {sample_resume_text}

    --- Resume to Rewrite ---
    {resume_text}
    """)
    try:
        options = {"temperature": 0.3, "max_tokens": 3000}
        response = ollama.chat(
            model="gpt-oss:20b",
            messages=[{"role": "user", "content": prompt}],
            options=options
        )
        
        if "message" in response and "content" in response["message"]:
            return clean_text(response["message"]["content"].strip())
        elif "messages" in response and response["messages"]:
            return clean_text(response["messages"][-1]["content"].strip())
        return ""
    except Exception as e:
        print(f"[ERROR] LLM call failed: {e}")
        return ""
