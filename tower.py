import random

def generate_ancient_library_description(room):
    descriptions = [
        f"You are in room {room} of the Ancient Library. Dusty tomes line the walls from floor to ceiling, and the air is heavy with the scent of old parchment. A large, ornate book lies open on a pedestal, its pages filled with strange runes.",
        f"Room {room} of the Ancient Library is dimly lit by flickering candles. Shelves creak under the weight of countless scrolls and leather-bound volumes. A small, round table in the center is stacked with maps of forgotten worlds.",
        f"The Ancient Library's room {room} has a high, vaulted ceiling. The echoes of your footsteps mingle with the soft whispers of turning pages. Ancient tapestries adorn the walls, depicting scenes of legendary heroes and mythical beasts.",
        f"In room {room}, the Ancient Library reveals a cozy alcove, with comfortable chairs and a fireplace casting a warm glow. Shelves are filled with rare first editions and ancient manuscripts.",
        f"Room {room} appears to be a study area in the Ancient Library, with desks laden with quills, ink pots, and parchments. The walls are lined with bookcases containing old texts and forgotten lore.",
        f"As you enter room {room}, you notice a series of intricate murals on the walls of the Ancient Library, depicting the history of magic and alchemy. The room is filled with the aroma of ancient leather and wood.",
        f"Room {room} in the Ancient Library is a quiet reading area. Soft light filters through stained glass windows, illuminating the richly colored carpets and tapestries.",
        f"In this part of the Ancient Library, room {room} holds a collection of astronomical charts and celestial maps. A large brass telescope points towards a domed skylight.",
        f"Room {room} contains a gallery of historical artifacts and relics, each with a placard explaining its significance. The items are carefully displayed in glass cases, surrounded by relevant literature.",
        f"You discover that room {room} is dedicated to ancient musical scores and instruments. The air resonates with a silent melody, a testament to the musical heritage stored within."
    ]
    return random.choice(descriptions)


def generate_forgotten_catacombs_description(room):
    descriptions = [
        f"Room {room} in the Forgotten Catacombs is shrouded in darkness, with only the faint glow of ghostly lanterns lighting the way. The air is thick with the scent of earth and decay.",
        f"In room {room} of the Forgotten Catacombs, skeletal remains are scattered across the ground, and the walls are lined with ancient inscriptions that hint at long-lost secrets.",
        f"As you enter room {room}, you notice a chilling breeze. The walls are adorned with eerie carvings, and you can hear the distant sound of chains clinking.",
        f"Room {room} is eerily silent, save for the occasional drip of water. The floor is uneven, and the walls feel close, as if they are slowly closing in.",
        f"The air in room {room} is musty and stagnant. Old, tattered banners hang from the ceiling, and rusted weapons are strewn about, relics of forgotten battles.",
        f"In this section of the catacombs, room {room} holds a series of coffins. Some are ajar, revealing nothing but dust and cobwebs inside.",
        f"Room {room} is dominated by a large statue of an unknown deity, its eyes seeming to follow your every move. Offerings and candles lie at its base, left by past visitors.",
        f"As you step into room {room}, the sound of your footsteps echoes off the walls. Several alcoves contain stone sarcophagi, etched with names and dates.",
        f"Room {room} has a small, barred window high up on the wall, letting in a sliver of light. The remains of old tapestries and broken pottery are scattered around.",
        f"You find room {room} partially collapsed, with rubble blocking parts of it. Through the gaps in the stone, you can see remnants of what might have been secret chambers."
    ]
    return random.choice(descriptions)

def generate_enchanted_garden_description(room):
    descriptions = [
        f"Room {room} in the Enchanted Garden is a lush oasis, with vibrant flowers and a tranquil pond. The air is perfumed with the scent of blooming jasmine.",
        f"In room {room}, the Enchanted Garden reveals a hidden grove with a sparkling fountain at its center. Butterflies flit about, and the leaves seem to whisper secrets.",
        # ... Add more descriptions
    ]
    return random.choice(descriptions)

def generate_mystical_observatory_description(room):
    descriptions = [
        f"Room {room} of the Mystical Observatory houses ancient telescopes and star charts. The dome above opens to a starry sky, revealing distant galaxies and nebulas.",
        f"In room {room}, you find yourself surrounded by orreries and celestial models. The walls are lined with books on astrology and astronomy, their pages filled with cosmic mysteries.",
        # ... Add more descriptions
    ]
    return random.choice(descriptions)

def generate_abandoned_armory_description(room):
    descriptions = [
        f"Room {room} in the Abandoned Armory is filled with rusted weapons and cracked shields. The remnants of banners hang from the walls, telling tales of forgotten wars.",
        f"The Abandoned Armory's room {room} contains rows of empty armor stands and scattered weaponry. A ghostly chill fills the air, and a sense of long-lost battles lingers.",
        # ... Add more descriptions
    ]
    return random.choice(descriptions)

def generate_echoing_caverns_description(room):
    descriptions = [
        f"Room {room} in the Echoing Caverns amplifies every sound. Stalactites and stalagmites create a natural labyrinth, and the sound of dripping water echoes in the darkness.",
        f"As you enter room {room}, the Echoing Caverns reveal a vast underground lake. The echo of water lapping against the cave walls creates a haunting melody.",
        # ... Add more descriptions
    ]
    return random.choice(descriptions)

def generate_crystal_mines_description(room):
    descriptions = [
        f"Room {room} in the Crystal Mines glitters with countless crystals embedded in the walls. The light refracts in rainbow patterns, casting a kaleidoscope of colors.",
        f"In room {room}, the Crystal Mines are a maze of tunnels, each lined with luminous gems and crystals. The air sparkles with the energy of the stones.",
        # ... Add more descriptions
    ]
    return random.choice(descriptions)

def generate_hall_of_mirrors_description(room):
    descriptions = [
        f"Room {room} in the Hall of Mirrors is a dizzying array of reflective surfaces. Your reflection appears and disappears, creating a disorienting but mesmerizing experience.",
        f"The Hall of Mirrors' room {room} plays tricks on your eyes. Mirrors of all shapes and sizes create an endless maze, reflecting the world in strange and surreal ways.",
        # ... Add more descriptions
    ]
    return random.choice(descriptions)

def generate_frozen_wasteland_description(room):
    descriptions = [
        f"Room {room} of the Frozen Wasteland is a vast expanse of ice and snow. The cold bites at your skin, and the howling wind is the only sound in this desolate landscape.",
        f"In room {room}, the Frozen Wasteland is a field of ice sculptures, frozen in time. The eerie stillness is broken only by the crunch of snow underfoot.",
        # ... Add more descriptions
    ]
    return random.choice(descriptions)

def generate_volcanic_forge_description(room):
    descriptions = [
        f"Room {room} in the Volcanic Forge is filled with the heat of molten lava. The air shimmers with heat, and the walls glow red from the furnaces.",
        f"The Volcanic Forge's room {room} is a cacophony of hammering and the roar of fire. Blacksmiths' anvils are scattered around, surrounded by half-finished weapons and armor.",
        # ... Add more descriptions
    ]
    return random.choice(descriptions)

def generate_whispering_woods_description(room):
    descriptions = [
        f"Room {room} in the Whispering Woods is filled with ancient trees whose leaves rustle with hushed tones. A mystical fog blankets the ground, and mysterious eyes peer from the shadows.",
        f"The air in room {room} of the Whispering Woods is fragrant with wildflowers. Soft whispers seem to float on the breeze, carrying secrets of the forest.",
        # ... Add more descriptions as needed
    ]
    return random.choice(descriptions)

def generate_deserted_marketplace_description(room):
    descriptions = [
        f"Room {room} resembles a Deserted Marketplace, with abandoned stalls and faded goods. The echoes of a once bustling trade hub linger in the silence.",
        f"In room {room}, the remnants of the marketplace tell a story of forgotten commerce. Deserted stalls and scattered wares create a scene of desolation.",
        # ... Add more descriptions as needed
    ]
    return random.choice(descriptions)

def generate_sunken_shipwreck_description(room):
    descriptions = [
        f"Room {room} is an eerie Sunken Shipwreck. Barnacled timbers and tattered sails hint at long-lost sea voyages, while shadowy figures seem to drift in the murky water.",
        f"The water in room {room} is clear but deep, revealing the ghostly outline of a Sunken Shipwreck. Treasures and trinkets glint amongst the wreckage.",
        # ... Add more descriptions as needed
    ]
    return random.choice(descriptions)

def generate_rooftop_gardens_description(room):
    descriptions = [
        f"Room {room} opens up to a lush Rooftop Garden. Vibrant flowers and greenery contrast with the skyline, providing a serene escape amidst the clouds.",
        f"In room {room}, the Rooftop Gardens bloom under the open sky. The scent of blossoms fills the air, and the sound of a trickling fountain soothes the soul.",
        # ... Add more descriptions as needed
    ]
    return random.choice(descriptions)

def generate_clockwork_workshop_description(room):
    descriptions = [
        f"Room {room} is a hive of activity with gears and cogs. The Clockwork Workshop buzzes with mechanical life, with intricate devices lining the walls.",
        f"Within room {room}, the Clockwork Workshop clinks and whirrs. Automatons and intricate clockwork creations stand in various states of completion.",
        # ... Add more descriptions as needed
    ]
    return random.choice(descriptions)

def generate_petrified_forest_description(room):
    descriptions = [
        f"Room {room} is a Petrified Forest, where stone trees stand silent and still. The air is cool and still, and the ground crunches underfoot.",
        f"The Petrified Forest in room {room} creates a scene of eerie beauty. The fossilized trees are frozen in time, their branches reaching towards the sky.",
        # ... Add more descriptions as needed
    ]
    return random.choice(descriptions)

def generate_royal_crypt_description(room):
    descriptions = [
        f"Room {room} holds the solemn grandeur of the Royal Crypt. Tombs of ancient monarchs line the walls, their stories etched in stone.",
        f"The air in room {room} is heavy with history. The Royal Crypt is a resting place of kings and queens, their legacy preserved in the silence.",
        # ... Add more descriptions as needed
    ]
    return random.choice(descriptions)

# ... Define functions for other themes

def generate_room_description(floor, room):
    theme = get_floor_theme(floor)
    if theme == "Ancient Library":
        return generate_ancient_library_description(room)
    elif theme == "Forgotten Catacombs":
        return generate_forgotten_catacombs_description(room)
    elif theme == "Enchanted Garden":
        return generate_enchanted_garden_description(room)
    elif theme == "Mystical Observatory":
        return generate_mystical_observatory_description(room)
    elif theme == "Abandoned Armory":
        return generate_abandoned_armory_description(room)
    elif theme == "Echoing Caverns":
        return generate_echoing_caverns_description(room)
    elif theme == "Crystal Mines":
        return generate_crystal_mines_description(room)
    elif theme == "Hall of Mirrors":
        return generate_hall_of_mirrors_description(room)
    elif theme == "Frozen Wasteland":
        return generate_frozen_wasteland_description(room)
    elif theme == "Volcanic Forge":
        return generate_volcanic_forge_description(room)
    elif theme == "Whispering Woods":
        return generate_whispering_woods_description(room)
    elif theme == "Deserted Marketplace":
        return generate_deserted_marketplace_description(room)
    elif theme == "Sunken Shipwreck":
        return generate_sunken_shipwreck_description(room)
    elif theme == "Rooftop Gardens":
        return generate_rooftop_gardens_description(room)
    elif theme == "Clockwork Workshop":
        return generate_clockwork_workshop_description(room)
    elif theme == "Petrified Forest":
        return generate_petrified_forest_description(room)
    elif theme == "Royal Crypt":
        return generate_royal_crypt_description(room)
    # Add elif branches for the remaining themes
    # ...

    # Fallback generic description
    return f"You are in room {room} on floor {floor}, known as the {theme}. Each corner of the room holds secrets and challenges related to its theme."


class Room:
    def __init__(self, description, exits=None, items=None, challenges=None):
        self.description = description
        self.exits = exits if exits is not None else {}
        self.items = items if items is not None else []
        self.challenges = challenges if challenges is not None else []

def get_floor_theme(floor_number):
    themes = {
        1: "Ancient Library",
        2: "Forgotten Catacombs",
        3: "Enchanted Garden",
        4: "Mystical Observatory",
        5: "Abandoned Armory",
        6: "Echoing Caverns",
        7: "Crystal Mines",
        8: "Hall of Mirrors",
        9: "Frozen Wasteland",
        10: "Volcanic Forge",
        11: "Whispering Woods",
        12: "Deserted Marketplace",
        13: "Sunken Shipwreck",
        14: "Rooftop Gardens",
        15: "Clockwork Workshop",
        16: "Petrified Forest",
        17: "Royal Crypt",
        18: "Wizard's Study",
        19: "Moonlit Graveyard",
        20: "Sun Temple",
        21: "Rainbow Reef",
        22: "Shadowed Alleyways",
        23: "Cloud Castle",
        24: "Wind-swept Plains",
        25: "Overgrown Ruins",
        26: "Haunted Mansion",
        27: "Cursed Mausoleum",
        28: "Sacred Springs",
        29: "Infernal Depths",
        30: "Ancient Battlefield",
        31: "Starlit Sanctuary",
        32: "Frozen Tundra",
        33: "Decaying Dungeon",
        34: "Emerald Vineyards",
        35: "Labyrinthine Library",
        36: "Subterranean Lake",
        37: "Cavern of Wonders",
        38: "Haunted Opera House",
        39: "Underground Bazaar",
        40: "Chamber of Reflection",
        41: "Jeweled Palace",
        42: "Misty Moorlands",
        43: "Eternal Autumn Forest",
        44: "Festival of Lanterns",
        45: "Ship in the Sky",
        46: "City of Clocks",
        47: "Steampunk Metropolis",
        48: "Ivory Tower",
        49: "Coral Kingdom",
        50: "Temple of Time",
        51: "Viking Stronghold",
        52: "Dimensional Rift",
        53: "Nebula Nexus",
        54: "Sky Pirate's Haven",
        55: "Arctic Observatory",
        56: "Elemental Conflux",
        57: "Midnight Carnival",
        58: "Rose Garden Maze",
        59: "Pharaoh's Tomb",
        60: "Dragon's Roost",
        61: "Sphinx's Riddle Chamber",
        62: "Goblin Market",
        63: "Planetary Observatory",
        64: "Time Traveler's Lab",
        65: "Celestial Ballroom",
        66: "Mirror Dimension",
        67: "Garden of Eden",
        68: "Atlantean Ruins",
        69: "Dwarven Mines",
        70: "Elfwood Glade",
        71: "Ninja Dojo",
        72: "Samurai Fortress",
        73: "Mechanical City",
        74: "Wild West Ghost Town",
        75: "Cybernetic Utopia",
        76: "Space Station",
        77: "Interstellar Dock",
        78: "Galactic Council",
        79: "Asteroid Field",
        80: "Alien Hive",
        81: "Cosmic Cathedral",
        82: "Solar Flare Furnace",
        83: "Black Hole Prison",
        84: "Quantum Realm",
        85: "Void of Oblivion",
        86: "Eldritch Abyss",
        87: "Hall of Heroes",
        88: "Chamber of Legends",
        89: "King's Banquet Hall",
        90: "Sorcerer's Sanctum",
        91: "Timekeeper's Vault",
        92: "Celestial Observatory",
        93: "Necromancer's Nook",
        94: "Paladin's Pinnacle",
        95: "Assassin's Alley",
        96: "Bard's Balcony",
        97: "Alchemist's Atelier",
        98: "Rogue's Retreat",
        99: "Monk's Meditation Chamber",
        100: "Dragon's Lair"
    }
    return themes.get(floor_number, "Mystical Unknown")

def determine_layout_pattern(floor_number):
    # A few example layout patterns
    patterns = {
    "pattern1": {0: {"east": (1, 1)}, 1: {"west": (1, 0), "up": (2, 0)}},
    "pattern2": {0: {"north": (2, 1)}, 1: {"south": (2, 0), "up": (3, 0)}},
    "pattern3": {0: {"south": (3, 1)}, 1: {"north": (3, 0), "east": (3, 2)}, 2: {"west": (3, 1), "up": (4, 0)}},
    "pattern4": {0: {"west": (4, 1)}, 1: {"east": (4, 0), "up": (5, 0)}},
    "pattern5": {0: {"east": (5, 1)}, 1: {"west": (5, 0), "north": (5, 2)}, 2: {"south": (5, 1), "up": (6, 0)}},
    "pattern6": {0: {"south": (6, 1)}, 1: {"north": (6, 0), "up": (7, 0)}},
    "pattern7": {0: {"north": (7, 1)}, 1: {"south": (7, 0), "east": (7, 2)}, 2: {"west": (7, 1), "up": (8, 0)}},
    "pattern8": {0: {"west": (8, 1)}, 1: {"east": (8, 0), "south": (8, 2)}, 2: {"north": (8, 1), "up": (9, 0)}},
    "pattern9": {0: {"east": (9, 1)}, 1: {"west": (9, 0), "up": (10, 0)}},
    "pattern10": {0: {"south": (10, 1)}, 1: {"north": (10, 0), "west": (10, 2)}, 2: {"east": (10, 1), "up": (11, 0)}}
}
    # Select a pattern based on the floor number
    # For simplicity, we'll just rotate through the patterns
    pattern_keys = list(patterns.keys())
    selected_pattern = pattern_keys[(floor_number - 1) % len(pattern_keys)]
    
    return patterns[selected_pattern]

def generate_floor(floor_number, rooms_per_floor):
    floor_rooms = {}
    layout_pattern = determine_layout_pattern(floor_number)
    
    for room_number in range(rooms_per_floor):
        exits = layout_pattern.get(room_number, {})
        description = generate_room_description(floor_number, room_number)
        
        floor_rooms[(floor_number, room_number)] = Room(description, exits)

    return floor_rooms

def generate_tower(total_floors, rooms_per_floor):
    tower = {}
    for floor in range(1, total_floors + 1):
        tower.update(generate_floor(floor, rooms_per_floor))
    return tower

# Generate the tower
rooms_per_floor = 5
tower_of_dread = generate_tower(100, rooms_per_floor)

# Initialize player location
player_location = (1, 0)  # Start at the first room of the first floor

# Function to handle player movement
def move(direction):
    global player_location
    current_room = tower_of_dread[player_location]
    if direction in current_room.exits:
        player_location = current_room.exits[direction]
    else:
        print("You can't go that way.")

def get_exit_description(direction, next_room):
    floor_change = next_room[0] != player_location[0]
    
    if floor_change:
        if direction == "up":
            return "A mystical portal glowing with ethereal light, promising passage to a higher level of the tower."
        elif direction == "down":
            return "An ancient stone staircase spiraling downwards into the shadowy depths below."

    else:
        if direction == "east":
            return "A creaking wooden door bound in iron, leading eastward to mysteries unknown."
        elif direction == "west":
            return "A corridor veiled in darkness, winding its way westward through the tower."
        elif direction == "north":
            return "An ornately carved gateway opening to the north, adorned with enigmatic runes."
        elif direction == "south":
            return "A passage to the south, where faint echoes and a cool breeze emanate from the shadows."

    return "A narrow, arched doorway leading to another part of this floor."

def describe_room():
    global player_location
    room = tower_of_dread[player_location]
    print(room.description)

    # Describe the exits
    print("You see the following exits:")
    for exit_dir in room.exits:
        next_room = room.exits[exit_dir]
        exit_description = get_exit_description(exit_dir, next_room)
        print(f"{exit_dir.capitalize()}: {exit_description}")


# Initialize player vars
player_name = ""
player_class = ""
player_stats = {
    "gold": 0,
    "hp": 0,
    "atk": 0,
    "ac": 0,
    "dmg": 0
}
player_inventory = {
    "healing_potion": 0,
    "stale_bread": 0,
    "water_pouch": 0
}

# Function to choose the player's class
def choose_class():
    global player_class
    print(f"Welcome, {player_name}! Choose your starting class:")
    print("1. Rogue")
    print("2. Mage")
    print("3. Warrior")
    
    while True:
        class_choice = input("Enter the number of your chosen class: ")
        
        if class_choice == "1":
            player_class = "Rogue"
            break
        elif class_choice == "2":
            player_class = "Mage"
            break
        elif class_choice == "3":
            player_class = "Warrior"
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Function to initialize player stats based on class
def initialize_player_stats():
    global player_stats
    if player_class == "Rogue":
        player_stats = {
            "gold": 100,
            "hp": 30,
            "atk": 2,
            "ac": 10,
            "dmg": 2
        }
    elif player_class == "Mage":
        player_stats = {
            "gold": 50,
            "hp": 20,
            "atk": 3,
            "ac": 5,
            "dmg": 5
        }
    elif player_class == "Warrior":
        player_stats = {
            "gold": 30,
            "hp": 50,
            "atk": 3,
            "ac": 15,
            "dmg": 2
        }

# Function to display player stats
def display_player_stats():
    global player_stats
    print("Player Stats:")
    for stat, value in player_stats.items():
        print(f"{stat}: {value}")
    display_inventory()    
        
# Function to update player inventory
def update_inventory(item, change):
    global player_inventory
    current_quantity = player_inventory[item]
    new_quantity = current_quantity + change
    player_inventory[item] = new_quantity
        
# Function to display player inventory
def display_inventory():
    global player_inventory
    print("Player Inventory:")
    for item, quantity in player_inventory.items():
        print(f"{item}: {quantity}")

# Function to update player gold
def update_gold(change):
    global player_stats
    current_gold = player_stats["gold"]
    new_gold = current_gold + change
    player_stats["gold"] = new_gold
    
# Function to handle interactions in the town
def visit_town():
    print(f"Welcome, {player_name} to the town of Haven. Here you can find supplies and information on how to clear the dread tower.")
    
    # Add your game logic for interactions in the town here.
    # For example, options to buy items, get information, etc.
    choice = input("What would you like to do?\n0.View stats\n1.Visit shop\n2.Enter the tower")
    
    if choice == "0":
        # Call the function to display player stats
        display_player_stats()
        visit_town()
    elif choice == "1":
        print("You head for the shop.")
        goto_shop()
    elif choice == "2":
        print("You head for the tower.")
        goto_dread_tower()
    else:
        # Player didn't choose a valid option
        print("You ponder what to do next...")

# Function to handle interactions in the shop
def goto_shop():
    print(f"Welcome, {player_class}. Have a look at my wares.")
    
    # Add your game logic for interactions in the shop here.
    # For example, options to buy items, get information, etc.
    shop_inventory = input("1.Healing Potion 10g\n2.Stale Bread 1g\n3.Small water pouch 1g")
    
    if shop_inventory == "1":
        # Deduct the cost of the potion and update player gold
        update_gold(-10)
        # Add the potion to the player's inventory
        update_inventory("healing_potion", 1)
        print("You bought 1 healing potion.")
    elif shop_inventory == "2":
        update_gold(-1)
        # Add the bread to the player's inventory
        update_inventory("stale_bread", 1)
        print("You bought 1 stale bread.")
    elif shop_inventory == "3":
        update_gold(-1)
        # Add the water pouch to the player's inventory
        update_inventory("small_water_pouch", 1)
        print("You bought 1 small water pouch.")    
    else:
        # Player chose not to visit the shop
        print("You decide not to visit the shop for now.")

# Define the Room class
class Room:
    def __init__(self, description, exits=None, items=None):
        self.description = description
        self.exits = exits if exits is not None else {}
        self.items = items if items is not None else []

    def add_exit(self, direction, coordinates):
        self.exits[direction] = coordinates

# Function for the player to explore the Dread Tower
def explore_dread_tower():
    global player_location
    while True:
        describe_room()
        choice = input("What would you like to do? (Type 'help' for options) ").lower()

        if choice == "help":
            print("Available commands: 'north', 'east', 'south', 'west', 'up', 'down', 'quit'")
        elif choice in ("north", "east", "south", "west", "up", "down"):
            move(choice)
        elif choice == "quit":
            print("Thank you for playing. Goodbye!")
            break
        else:
            print("Invalid command. Type 'help' for options.")

# Function to handle Dread Tower exploration
def goto_dread_tower():
    print("Entering the Dread Tower...")
    explore_dread_tower()

# Game loop
while True:
    # Check if the player's name is not set (first run)
    if not player_name:
        player_name = input("Welcome to DREAD TOWER! \nIn this game you will make choices by selecting 1, 2, or 3, etc... \nWhat is your name? ")
        choose_class()
        initialize_player_stats()
    
    # Call the function to visit the town
    visit_town()
    
    # Prompt the player if they want to enter the Dread Tower or leave the game
    tower_choice = input("Do you want to enter the Dread Tower? \n1.Yes\n2.No")
    
    if tower_choice == "1":
        # Call the function to enter the Dread Tower
        goto_dread_tower()
    elif tower_choice == "2":
        # Player chose to leave the game
        print("Thank you for playing. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1 to enter the tower or 2 to leave the game.")
