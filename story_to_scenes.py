from pathlib import Path
import re

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

STORY_TITLE = "The Crown of Eternity"
HERO = "Elian Ashborne"


def split_story(story):
    return [line.strip() for line in story.splitlines() if line.strip()]



def main():
    print("\n=== MAGICAL CITY: STORY TO SCENES ===")
    print("Paste your story below.")
    print("When finished, type END on a new line and press Enter.\n")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    story = "\n".join(lines).strip()

    if not story:
        print("No story entered. Please try again.")
        return

    scenes = split_story(story)

    if not scenes:
        print("No scenes could be created.")
        return

    output_file = OUTPUT_DIR / "scene_plan.md"

    with output_file.open("w", encoding="utf-8") as file:
        file.write("# Magical City - Scene Plan\n\n")
        file.write("**Story:** The Crown of Eternity\n\n")

        for number, scene in enumerate(scenes, start=1):
            file.write(f"## Scene {number}\n\n")
            file.write(f"**Story action:** {scene}\n\n")
            file.write(f"**Visual prompt:** Cinematic realistic Hollywood fantasy scene from {STORY_TITLE}, featuring {HERO}. Action: {scene} Ancient magical kingdom, dramatic storm lighting, detailed environment, epic fantasy film quality.\n\n")
            file.write(f"**Dialogue / narration:** {HERO}: {scene}\n\n")
            file.write("---\n\n")

    print(f"\nSuccess! Created {len(scenes)} scenes.")
    print(f"Scene plan saved to: {output_file}")


if __name__ == "__main__":
    main()
