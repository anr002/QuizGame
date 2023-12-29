import os
import json

def generate_ability_paths(god_name, num_abilities):
    paths = []
    for i in range(num_abilities):
        ability_name = "passive" if i == 0 else f"ability_{i}"
        paths.append(f"God Abilities/{god_name}/{ability_name}.png")
    return paths

gods_dir = "God Abilities"
gods = []

for god_name in os.listdir(gods_dir):
    num_abilities = len(os.listdir(os.path.join(gods_dir, god_name)))
    abilities = generate_ability_paths(god_name, num_abilities)
    god = {
        "name": god_name,
        "icon": f"Icons/{god_name}.png",
        "abilities": abilities
    }
    gods.append(god)

with open('gods.json', 'w') as f:
    json.dump(gods, f, indent=2)