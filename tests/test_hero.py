from pathlib import Path
from xml.etree import ElementTree


hero_path = Path(__file__).parents[1] / "assets" / "hero.svg"
hero = hero_path.read_text()
root = ElementTree.parse(hero_path).getroot()
namespace = {"svg": "http://www.w3.org/2000/svg"}
greeting = next(
    element
    for element in root.findall(".//svg:text", namespace)
    if element.get("class") == "greeting"
)
characters = greeting.findall("svg:tspan", namespace)

assert len(characters) == len("Hi, I'm Akib.")
assert "".join(character.text for character in characters) == "Hi, I'm Akib."
assert all(character.get("class") == "greeting-char" for character in characters)
assert [character.get("style") for character in characters] == [
    f"--i:{index}" for index in range(len(characters))
]
assert "@keyframes letter-in" in hero
assert ".greeting-char { animation: letter-in 4s steps(1, end) infinite;" in hero
assert "animation-delay: calc(var(--i) * 90ms);" in hero
assert ".greeting-char { animation: none; opacity: 1; }" in hero

print("Hero greeting animation: PASS")
