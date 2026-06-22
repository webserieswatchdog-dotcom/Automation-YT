from youtube_content_generator import build_content


def main():
    topic = input("Enter a YouTube topic: ")

    result = build_content(topic)

    print("\nGenerated Content\n")

    for key, value in result.items():
        print(f"{key}:")
        print(value)
        print()


if __name__ == "__main__":
    main()
