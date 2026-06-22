"""
Research helper for Automation-YT.
This module prepares search queries for external research tools.
"""

def create_research_query(topic: str) -> str:
    return f"Latest information and key facts about {topic}"


if __name__ == "__main__":
    topic = "Artificial Intelligence"
    print(create_research_query(topic))
