import time
import os

lyrics = [
    "Welcome to my world...",
    "Music is my emotion...",
    "Every moment has a story...",
    "Let the music speak..."
]

os.system("cls" if os.name == "nt" else "clear")

print("\n🎵 CR LYRICS ANIMATION 🎵\n")
time.sleep(1)

for line in lyrics:
    print("✨ " + line)
    time.sleep(2)

print("\n❤️ Thanks for watching ❤️")
