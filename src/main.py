from content_builder import build_content


def main():
    topic = input("Enter topic: ")

    content = build_content(topic)

    print("\nTITLE")
    print(content.title)

    print("\nDESCRIPTION")
    print(content.description)

    print("\nTAGS")
    print(content.tags)

    print("\nTHUMBNAIL")
    print(content.thumbnail_prompt)

    print("\nSCRIPT")
    print(content.script)


if __name__ == "__main__":
    main()
