from generators.script_generator import generate_script
from services.research_service import get_research_notes
from models.video_content import VideoContent


def build_content(topic):
    research = get_research_notes(topic)

    script = generate_script(topic)

    title = f"{topic} Explained"
    description = (
    f"Learn about {topic}. "
    f"Research Summary: {research}"
)
    tags = [topic, "AI", "Automation", "YouTube"]

    thumbnail_prompt = (
        f"Create a futuristic YouTube thumbnail about {topic}"
    )

    outline = [
        "Introduction",
        "Main Concepts",
        "Examples",
        "Future Impact",
        "Conclusion",
    ]

    return VideoContent(
        title=title,
        description=description,
        tags=tags,
        thumbnail_prompt=thumbnail_prompt,
        outline=outline,
        script=script,
    )
