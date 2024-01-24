import random

def generate_ancient_library_description(room):
    descriptions = [
        f"You are in room {room} of the Ancient Library. Dusty tomes line the walls from floor to ceiling, and the air is heavy with the scent of old parchment. A large, ornate book lies open on a pedestal, its pages filled with strange runes.",
        f"Room {room} of the Ancient Library is dimly lit by flickering candles. Shelves creak under the weight of countless scrolls and leather-bound volumes. A small, round table in the center is stacked with maps of forgotten worlds.",
        f"The Ancient Library's room {room} has a high, vaulted ceiling. The echoes of your footsteps mingle with the soft whispers of turning pages. Ancient tapestries adorn the walls, depicting scenes of legendary heroes and mythical beasts."
        # ... Add more descriptions as needed
    ]
    return random.choice(descriptions)

def generate_forgotten_catacombs_description(room):
    descriptions = [
        f"Room {room} in the Forgotten Catacombs is shrouded in darkness, with only the faint glow of ghostly lanterns lighting the way. The air is thick with the scent of earth and decay.",
        f"In room {room} of the Forgotten Catacombs, skeletal remains are scattered across the ground, and the walls are lined with ancient inscriptions that hint at long-lost secrets.",
        # ... Add more descriptions
    ]
    return random.choice(descriptions)

# ... Define functions for other themes

def generate_room_description(floor, room):
    theme = get_floor_theme(floor)
    if theme == "Ancient Library":
        return generate_ancient_library_description(room)
    elif theme == "Forgotten Catacombs":
        return generate_forgotten_catacombs_description(room)
    # Add elif branches for other themes
    # ...
    return f"You are in room {room} on floor {floor}, known as the {theme}. Each corner of the room holds secrets and challenges related to its theme."

# ... Rest of your code


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

def generate_floor(floor_number, rooms_per_floor):
    floor_rooms = {}
    for room_number in range(rooms_per_floor):
        exits = {"up": (floor_number + 1, 0)} if room_number == rooms_per_floor - 1 else {}
        if room_number > 0:
            exits["west"] = (floor_number, room_number - 1)
        if room_number < rooms_per_floor - 1:
            exits["east"] = (floor_number, room_number + 1)

        floor_rooms[(floor_number, room_number)] = Room(
            generate_room_description(floor_number, room_number), exits
        )

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
        #describe_room()
    else:
        print("You can't go that way.")

def describe_room():
    room = tower_of_dread[player_location]
    print(room.description)
    print("You see the following exits:")
    for exit_dir in room.exits:
        print(exit_dir.capitalize())

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
