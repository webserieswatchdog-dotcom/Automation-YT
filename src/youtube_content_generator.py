"""
AI YouTube Content Generator
"""

from metadata_generator import generate_metadata


def generate_video_outline(topic):
    return [
        f"Introduction to {topic}",
        f"Why {topic} matters",
        f"Key facts about {topic}",
        f"Future possibilities of {topic}",
        "Summary and conclusion"
    ]


def generate_thumbnail_prompt(topic):
    return (
        f"Create a cinematic futuristic YouTube thumbnail "
        f"for '{topic}' with vibrant colors and dramatic lighting."
    )


def build_content(topic):
    metadata = generate_metadata(topic)

    return {
        "title": metadata["title"],
        "description": metadata["description"],
        "tags": metadata["tags"],
        "thumbnail_prompt": generate_thumbnail_prompt(topic),
        "outline": generate_video_outline(topic)
    }


if __name__ == "__main__":
    result = build_content("Artificial Intelligence")

    for key, value in result.items():
        print(key)
        print(value)
        print("-" * 40)
