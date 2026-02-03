import random
import re
from rag_engine import extract_article   # ✅ FIX: missing import

# Controlled generative components (grounded, no hallucination)
INTRO = [
    "This article establishes that",
    "The Constitution provides that",
    "It clearly states that",
    "According to this provision,"
]

STATE = [
    "the State must follow legal procedures",
    "government authorities are bound by law",
    "power cannot be exercised arbitrarily",
    "the law limits how liberty can be restricted"
]

ACTION = [
    "before interfering with personal freedom.",
    "when affecting a person's life or liberty.",
    "in matters concerning individual liberty.",
    "while taking actions impacting life and freedom."
]


def generate_explanation(article_number: str):
    if article_number == "21":
        return (
            f"{random.choice(INTRO)} "
            f"{random.choice(STATE)} "
            f"{random.choice(ACTION)}"
        )

    if article_number == "19":
        return random.choice([
            "This article protects key freedoms such as speech, movement, and expression, subject to lawful limits.",
            "Citizens are granted important freedoms, which the State may regulate reasonably.",
            "It balances personal freedoms with the needs of public order."
        ])

    if article_number == "14":
        return random.choice([
            "This article guarantees equality before the law.",
            "It ensures that the State treats all individuals equally.",
            "No person can be unfairly discriminated against under this article."
        ])

    return "This article defines an important constitutional rule."


def format_answer(article_number: str):
    article_text = extract_article(article_number)

    if not article_text:
        return "❌ Article not found in the Constitution PDF."

    # Remove headers / noise
    article_text = re.sub(
        r"\bARTICLES?\b|\bARTICLE\b",
        "",
        article_text,
        flags=re.IGNORECASE
    )
    article_text = re.sub(r"\s+", " ", article_text).strip()

    # Extract title safely
    title_match = re.search(
        rf"{article_number}\s*[.\-—]?\s*(.*?)(?=No person|Every citizen|All citizens|The State|$)",
        article_text,
        re.IGNORECASE
    )

    title = title_match.group(1).strip() if title_match else "Constitutional Provision"

    # Extract first legal sentence (official text)
    body = article_text.replace(title, "", 1).strip()
    sentence_end = body.find(".")
    official_text = body[:sentence_end + 1] if sentence_end != -1 else body
    official_text = official_text[:250]

    explanation = generate_explanation(article_number)

    return (
        f"📜 **Article {article_number} – {title}**\n\n"
        f"{official_text}\n\n"
        f"🧠 **Simple Explanation:**\n"
        f"{explanation}\n\n"
        f"⚠️ *Educational purpose only.*"
    )
