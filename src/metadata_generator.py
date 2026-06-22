"""
Generate YouTube metadata for videos.
"""

def generate_metadata(topic: str):
    return {
        "title": f"{topic} Explained in 5 Minutes",
        "description": (
            f"This video explores {topic} using AI-powered automation.\n"
            "Created with Automation-YT."
        ),
        "tags": [
            topic,
            "AI",
            "Automation",
            "YouTube",
            "Python"
        ]
    }


if __name__ == "__main__":
    metadata = generate_metadata("Artificial Intelligence")
    print(metadata)
