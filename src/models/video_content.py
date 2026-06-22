"""
Video content model used throughout the project.
"""

class VideoContent:
    def __init__(
        self,
        title,
        description,
        tags,
        thumbnail_prompt,
        outline,
        script,
    ):
        self.title = title
        self.description = description
        self.tags = tags
        self.thumbnail_prompt = thumbnail_prompt
        self.outline = outline
        self.script = script

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "tags": self.tags,
            "thumbnail_prompt": self.thumbnail_prompt,
            "outline": self.outline,
            "script": self.script,
        }
