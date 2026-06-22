# Architecture

Automation-YT follows a modular architecture.

## Pipeline

Topic
→ Research
→ Script Generation
→ Metadata Generation
→ Thumbnail Prompt
→ Voice Generation
→ Subtitle Generation
→ Video Assembly
→ YouTube Upload

## Components

- generators/
- services/
- models/
- content_builder.py
- video_pipeline.py

Future versions will integrate LLM providers, TTS engines and automated publishing workflows.
