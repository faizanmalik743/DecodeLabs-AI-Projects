# ============================================================
#  DecodeLabs | AI Industrial Training | Batch 2026
#  Project 1 : Rule-Based AI Chatbot
#  Author    : AI Engineer Intern
# ============================================================

# ── PHASE 2: KNOWLEDGE BASE (Dictionary – O(1) lookup) ──────
RESPONSES = {
    # Greetings
    "hello"        : "Hey there! I'm DecoBot. How can I assist you today?",
    "hi"           : "Hi! Welcome to DecodeLabs. What's on your mind?",
    "hey"          : "Hey! Great to see you. Ask me anything!",

    # Farewells
    "bye"          : "Goodbye! Keep building and keep learning. 🚀",
    "goodbye"      : "See you next time! Stay curious.",
    "see you"      : "See you later! Don't forget to push your code. 😄",

    # Status
    "how are you"  : "I'm running at 100% efficiency — pure logic, zero bugs!",
    "what are you" : "I'm DecoBot, a rule-based AI chatbot built with pure Python logic.",
    "who made you" : "I was built by an AI Engineer intern at DecodeLabs, Batch 2026!",

    # Project-related
    "what is ai"   : "AI is the simulation of human intelligence by machines using logic, learning, and data.",
    "what is a chatbot" : "A chatbot is a program that simulates conversation using rules or machine learning.",
    "what is a rule based chatbot" : "A rule-based chatbot responds using predefined if-else or dictionary logic — no learning involved!",

    # Help
    "help"         : "I can answer: greetings, farewells, AI questions, and chatbot info. Try 'what is ai'!",
    "commands"     : "Try: hello, bye, how are you, what is ai, what is a chatbot, help, exit.",
}

EXIT_COMMANDS = {"exit", "quit", "stop", "close"}

# ── PHASE 1: INPUT & SANITIZATION ───────────────────────────
def sanitize(raw: str) -> str:
    """Normalize input: lowercase + strip whitespace."""
    return raw.lower().strip()

# ── PHASE 3: PROCESS & RESPONSE GENERATION ──────────────────
def get_response(clean_input: str) -> str:
    """
    Dictionary .get() handles lookup + fallback in one atomic operation.
    O(1) time complexity regardless of how many rules exist.
    """
    return RESPONSES.get(clean_input, "I don't understand that yet. Try 'help' to see what I know!")

# ── MAIN LOOP (The Heartbeat) ────────────────────────────────
def run_chatbot():
    print("=" * 55)
    print("  DecoBot | Rule-Based AI Chatbot | DecodeLabs 2026  ")
    print("=" * 55)
    print("  Type 'help' for commands. Type 'exit' to quit.\n")

    while True:                                  # Infinite loop — stays alive
        raw_input   = input("You   : ")          # PHASE 1 — Capture raw input
        clean_input = sanitize(raw_input)        # PHASE 1 — Sanitize

        if clean_input in EXIT_COMMANDS:         # EXIT STRATEGY — kill command
            print("DecoBot: Goodbye! Session terminated. 👋")
            break

        response = get_response(clean_input)     # PHASE 2+3 — Lookup & respond
        print(f"DecoBot: {response}\n")

# ── ENTRY POINT ──────────────────────────────────────────────
if __name__ == "__main__":
    run_chatbot()
