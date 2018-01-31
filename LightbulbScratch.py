#My APCSP Create Project!
#This is intended to be a fantasy world random generator --> for creative inspiration in writing.

import random
#########Library of Lists######### Last updated April 29
#Each list contains adjectives, nouns, or phrases that will be used in later functions for the random generators.
#Some of these words (like the colors, textures, and traits) came from Internet browsing and random perusal of books.
#Most phrases, like "Bubble Orchid," are from personal creative license; several are nods to works like the Sims 3.
#Lists were separated into multiple lines for easier reading.

color = ["ashen", "ashy", "blazing", "amber", "amethyst", "aqua", "aquamarine", "avocado", "azure", "black", 
"blue", "brass", "bronze", "burgundy", "canary", "carnelian", "charcoal", "chartreuse", "chestnut", "chocolate", 
"chrome", "citrine", "cobalt", "copper", "coral", "cream", "crimson", "cyan", "dark", "drab", "dull", "dun", 
"ebony", "emerald", "flushed", "fuchsia", "garnet", "glassy", "gold", "green", "henna", "indigo", "turquoise",
"iridescent", "ivory", "jade", "jet", "lavender", "lemon", "light", "lilac", "lime", "magenta", "mahogany", 
"maize", "maroon", "mauve", "milky", "mint", "mustard", "navy", "obsidian", "olive", "onyx", "opaque",
"orange", "orchid", "pale", "peach", "pearly", "pink", "plum", "poppy", "primrose", "purple", "red", "rose",
"ruby", "ruddy", "rusty", "sable", "saffron", "salmon", "sapphire", "scarlet", "sepia", "shimmering", "sienna",
"silver", "slate", "smoky", "snowy", "sooty", "spruce", "tan", "topaz", "translucent", "transparent", 
"twinkling", "ultramarine", "umber", "vermilion", "violet", "walnut", "white", "wine", "yellow"]

texture = ["brittle", "buttery", "cellular", "chewy", "coarse", "compact", "complex", "creamy", "crisp", 
"crumbly", "crunchy", "crystalline", "delicate", "dense", "exquisite", "fibrous", "granular", "pulpy", 
"woolen", "fine", "plastic-like", "firm", "flimsy", "fluffy", "grainy", "granular", "great", "gritty", 
"hairy", "hard", "homogeneous", "interesting", "leathery", "light", "loose", "meaty", "moral", "natural", 
"peculiar", "perfect", "porous", "proper", "rich", "silken", "silky", "smooth", "soft", "soil", "solid", 
"spongy", "strong", "subtle", "tender", "thick", "thin", "thinner", "tough", "transparent", "uneven", 
"uniform", "unique", "velvety", "waxy", "woody"]

positive_trait = ["active", "adaptable", "alert", "ambitious", "analytical", "assertive", "attentive", 
"broad-minded", "capable", "challenge-oriented", "competent", "conscientious", "constructive", "cooperative", 
"courageous", "creative", "curious", "dedicated", "dependable", "determined", "diplomatic", "disciplined", 
"dynamic", "effective", "efficient", "energetic", "enterprising", "enthusiastic", "far-sighted", "imaginative", 
"independent", "logical", "motivated", "optimistic", "organized", "original", "perceptive", "personable", 
"pleasant", "poised", "positive", "practical", "productive", "proficient", "progressive", "punctual", 
"realistic", "reliable", "resourceful", "responsible", "risk-taker", "self-reliant", "sincere", "skilled", 
"sophisticated", "ambitious", "systematic", "tactful", "talented", "trustworthy"]

negative_trait = ["aggressive", "aloof", "arrogant", "boastful", "boring", "bossy", "callous", "cantankerous", 
"careless", "changeable", "clinging", "compulsive", "conservative", "cowardly", "cruel", "cunning", "cynical", 
"deceitful", "detached", "dishonest", "finicky", "flirtatious", "foolish", "foolhardy", "greedy", "grumpy", 
"gullible", "harsh", "impatient", "impolite", "impulsive", "inconsiderate", "inconsistent", "indecisive", 
"indiscreet", "inflexible", "interfering", "intolerant", "irresponsible", "jealous", "lazy", "lily-livered", 
"Machiavellian", "materialistic", "mean", "miserly", "moody", "narrow-minded", "nasty", "naughty", "nervous", 
"untidy", "untrustworthy", "vain", "vengeful", "vulgar", "weak-willed"]

snack = ["eggs", "muffins", "cheese", "smoothies", "mountain lion flesh", "cucumbers", "carrots", "rotten fish",
"dandelion milk", "fairy cakes", "almonds", "chocolate", "dates", "dove wings", "oranges", "watermelon", "spinach",
"marshmallows", "roasted weenies", "oysters", "pears", "sunflower seeds", "fried slugs", "demon blood", "cupcakes"]

first_name = ["Mirabelle", "Anna", "Theodora", "Rosalind", "Zadie", "Aviva", "Elizabeth", "Devon", "Indigo", "Cleo", 
"Pilar", "Pippa", "Georgiana", "Octavia", "Zinnia", "Winifred", "Marguerite", "Henrietta", "Greer", "Snow", "Boyce", 
"Hermione", "Lulu", "Tierney", "Lara", "Verity", "Juno", "Romy", "Dinah", "Seren", "Cassia", "Maple", "Polly", "Phoebe",
"Olympia", "Augusta", "Ilaria", "Vesper", "Vita", "Nico", "Shana", "Vivian", "Saskia", "Leonora", "Dorothea", "Fay", 
"Eulalia", "Marietta", "Calypso", "Flannery", "Indra", "Tamsin", "Bronwen", "Fleur", "Lev", "Constantine", "Rio", 
"Shepherd", "Caspian", "Ellison", "Auden", "West", "Chester", "Aurelio", "Robert", "Oliver", "Baxter", "Willis", "Leopold", 
"Teo", "Stellan", "Roscoe", "Bram", "Cassidy", "Penn", "Octavius", "Slater", "Pax", "Everest", "Rufus", "Orson", "Casimir", 
"Laszlo", "Hawk", "Pascal", "Fitzgerald", "Shaw", "Mercer", "Dorian", "Ozias", "Bowie", "Larson", "Cosmo", "Ellington", 
"Hart", "Griffith", "Whit", "Maguire", "Rafferty", "Sacha", "Florian", "Peregrine"]
#First names were found by randomly choosing from baby name books and inspiration from classmates' names.

last_name = ["Hatman", "Temples", "Raynott", "Woodbead," "Nithercott", "Rummage", "Southwark", "Harred", "Jarsdel", "Pober",
"Pavlovich", "Nuttall", "Nitt", "Tripoli", "Renko", "Coreander", "Dumond", "Maksimov", "Vauxhall", "Bumppo", "Douwes", 
"Lapp", "Houck", "Chasey", "Laverty", "Rizu", "Tregan", "Wyatts", "Bobblehead", "Tibs", "Randals", "Knight", "Belmore", 
"Nazir", "Fass", "Yelland", "Keke", "Wakatsuki", "Goshen", "Neslon", "Zayn", "Costella", "Dazzel", "Cellini", "Frick", 
"Siera", "Saika", "Utterson", "Movin", "Janney", "Dorsett", "Piace", "Sayed", "Weezer", "Elliots", "Mulhern", "Cathie", 
"Benzie", "Cosentino", "Trevers", "Aqui", "Sharpes", "Verge", "Lumpkin", "Cardellini", "Hawksworth", "Bedell", "Gennero", 
"Lebeu", "Calitri", "Farouk", "Guyrich"] 
#Last names were found through browsing through surname lists on the Internet and creative license.

like = ["teaching children", "swimming long distances", "foraging for berries", "climbing mango trees", "growing dandelions",
"graphing mathematical equations", "coding python", "laughing at philosophy jokes", "baking chocolate cakes",
"laughing at people falling", "cooking stew over a boisterous fire", "playing capture the flag", "petting puppies"]

quirk = ["whistling with blades of grass", "jumping over the cracks in the street", "finishing the sentences of other people", 
"randomly smiling at the sky", "crocheting only at midnight", "randomly laughing at inopportune moments",
"making tea by adding the water before the leaves", "using green ink exclusively for writing," "wearing duct tape on clothing"]

fatal_flaw = ["hubris", "too much ambition", "too much selflessness", "a constant sense of inferiority", "greed", "sloth",
"vanity", "an inability to accept change", "a tendency to panic", "a refusal to listen to mentors", "a tendency to blame others",
"an aggressive, war-focused disposition", "clumsiness around enemies and volcanoes", "too much curiosity", "holding grudges"
"an inability to develop emotional connections with others", "assuming too much self-importance"]

###Lists added for function land_plant() and beyond###
plant_name = ["Linaria", "Common Skullcap", "Alvera", "Peasegood", "Soul Mirror", "Belisarius", "Bubble Orchid", 
"Hot Lips", "Subterranean Espresso", "Parrot Blossom", "Alien Seed Pod", "Flying Duck Blossom", "Passion Fire", "Elanor",
"Chamberpot Delight", "Dovefeather", "Weberi Hiss", "Death's Kiss", "Last Lullaby", "Squirrel Gourd", "Ginger Spider"]
#Exist in nature: Hot Lips, Common Skullcap, Linaria (a genus); Death's Kiss inspired by Harry Potter, Alien Seed Pod by Sims 4.

location_name = ["Aetheria", "Miravelle", "Paragran", "the Grand Village", "Heavenstop", "Orange Bedlam",
"Ethylinia", "Cloud Atlanta", "Monarch's Grove", "Welwitschia", "Halli", "Goldendale", "Rothi Parata", "Franquer",
"Boing Boing", "Seasant", "Lothario", "Flogoshee", "Lizaba", "Zandipta"] 
#Cloud Atlanta derived from Cloud Atlas; Lothario from Sims 4; Aetheria from Greek mythology; Rothi Parata from roti prata (bread).

fauna = ["bees", "mountain goats", "slugs", "poisonous snails", "vipers", "fanged bats", "walnut bears", "foxes", "cows",
"moose", "ducks", "rainbow zebras", "polka-dot giraffes", "lions", "floating amoebae", "dart frogs", "wild dogs", 
"burrow rabbits", "butterflies", "deer", "chickens", "candycane lizards", "mystical spiders", "dragons", "red ants", 
"grasshoppers"]

plant_feature = ["purple pods filled with black ink", "glossy noodle hair roots", "butterfly antenna stamens"
"twinkling blue stars floating above the blooms", "nectar with the taste of lemon meringue"]

plant_reproduction = ["magical seeds shooting from the petals like a volcanic eruption", 
"seed pods shaped like human hearts brimming with green fluid", "hairy tubular threads unfurling from the roots", 
"oozing blue pus that can putrefy human flesh", "indigo seeds floating away in sparkly bubbles",
"pollination by red fireflies and blue-striped vipers", "orange blossoms with lumps that secrete golden ichor"]

###Lists added for function setting() and beyond###
terrain_type = ["active volcanoes", "volcanoes with mystical blue lava", "gentle rivers", "blood-tinted rivers", 
"lush rainforests", "grassy knolls", "silicon beaches", "explosive forests", "expansive plateaus", "grand canyons", 
"grainy plains", "arid, sandy deserts", "marshmallow marshes", "cranberry bogs", "desolate wastelands", 
"flower fields", "lakes of indigo", "almond-shaped hills", "natural mineral springs"]

terrain_name = ["Casperian Sea", "Aerian Desert", "Mushroom Forest", "Forbidden Lake", "the Valley of the Ancients", 
"Sonoma Beach", "the Land of the Dead", "the Grave of Angels", "Sunset Valley", "Devil's Garden", "Butterfly Paradise",
"Stalagtite Mine", "The Spine", "Fool's Mines"] #Sunset Valley from Sims 3; The Spine from Eragon

leader_title = ["Monarch", "Dictator", "Archmage", "Council Elder", "Supreme Overlord", "High Priest", "Prime Minister"]

home_type = ["quaint little cottage", "lavish mansion", "lovely house", "underground bunker"]

###Lists added for function cuisine() alone###
main_dish_name = ["Stuffed Truffled Casserole", "Rotten Piranha Delight", "Explosive Goose", "Miyaki Teriyaki", 
"Ravingly Rancid Tempura", "Creme de la Creme", "Turducken", "Ratatouilleeee", "Sprouted Smash", "Bubbling Bourbon Basket"]

seasoning_type = ["sea salt", "white pepper", "cinnamon", "dried sweat", "oregano", "parsley", "rosemary", "tumeric", 
"expensive saffron", "ground eye of newt", "thyme", "powdered snail shell", "ginger", "splintered bone", 
"frozen blood drops", "fairy tears", "rotten fishtail", "ground dragon scale", "cilantro", "sweet basil"]

cuisine_feature = ["off-white cream oozing burgundy filling", "bright red arteries circling the blue vegetables",
"orange tentacles reaching from the salad", "flaky green cubes sprouting pink flowers"]

cuisine_type = ["soup", "curry", "stir fry", "stew", "roast", "noodle bowl", "sandwich", "pot pie", "kabob plate"]

food_adjectives_dry = ["crusty", "burnt", "crispy", "crumbly", "crunchy"]
food_adjectives_wet = ["creamy", "hearty", "mushy", "slimy"]
food_adjectives_preparation = ["grilled", "oven-baked", "cauldron-boiled", "deep-fried", "dragonfire-roasted",
"fairy-charmed", "sliced", "wind-chilled"]

starch_type_general = ["bread", "pita", "tortilla chips", "rice", "saltine crackers", "potatoes", "quinoa"]
starch_type_pasta = ["buckwheat noodles", "tortellini", "linguini", "rice noodles", "ramen", "udon", "instant noodles"]

dairy_type = ["cheese", "whole milk", "2% fat milk", "sour cream", "ice cream", "yogurt", "custard"]

vegetable_type = ["cucumbers", "Puff Peppers", "mushrooms", "black corn", "artichokes", "carrots", "kale", "cauliflower",
"Lolly Lettuce", "broccoli", "brussel sprouts", "beets", "peas", "zucchini", "leeks", "Olly Onions"]

fruit_type = ["apple", "Burrowing Berry", "Wishful Watermelon", "apricot", "peach", "Flutterby Fruit", 
"dragonfruit", "blood orange", "Snowflake Coconut", "Persephone Pomegranate", "persimmon", "mango", "soursop"]

protein_type = ["mutton", "tofu", "duck", "bacon", "shrimp wontons", "beef tri-tip", "ground pork", "mountain lion", 
"chicken", "egg", "pork sirloin", "pinto beans", "goose",  "octopus", "salmon", "tilapia"]

#########These are the functions that refer to each of the four random generators!########## Last updated April 29
#Each function can be used separately to generate the text box on its own. 
#Each random generator for an element, like "Cuisine", has a function that will refer back to the library of lists.
def character_description():
	print "Character Description"
	character_name = random.choice(first_name) #To establish the same character name throughout the printed text.
	print """Your character %s %s (my, what a unique name!) has a(n) %s personality. According to peers, %s is also %s and %s. 
%s does have a few unfortunate traits, like the tendency to be consumed by a(n) %s streak or be %s with other people.
During downtime, %s enjoys eating %s and has a fondness for %s. One fascinating quirk is %s's love for %s!
But watch out! %s has the fatal flaw of %s, which will be sure to bring %s harm if not carefully curbed!
	""" %(character_name, random.choice(last_name), random.choice(positive_trait), character_name, random.choice(positive_trait), 
	random.choice(positive_trait), character_name, random.choice(negative_trait), random.choice(negative_trait), 
	character_name, random.choice(snack), random.choice(like), character_name, random.choice(quirk), 
	character_name, random.choice(fatal_flaw), character_name)

def land_plant():
	print "Plant Description"
	plant1 = random.choice(plant_name) #To establish the same plant name throughout the printed text.
	print """Ah, your protagonist has stumbled upon a plant with the name of the %s, which is %d feet tall and is quite abundant in regions such as %s.
The plant has %d %s leaves of %s texture and %d %s %s petals, which means the %s is likely to attract both curious scientists and %s.
Notably, the %s has the special physical feature of %s and is famous for its unique method of reproduction, which involves %s. 
Perhaps your protagonist would like to create a bouquet of %s for a significant other?
	""" %(plant1, random.randrange(0,919,1), random.choice(location_name), random.randrange(0,519,1), random.choice(color), 
	random.choice(texture), random.randrange(0,519,1), random.choice(texture), random.choice(color), plant1, random.choice(fauna),
	plant1, random.choice(plant_feature), random.choice(plant_reproduction), plant1)

def setting():
	print "Setting Description"
	location = random.choice(location_name) #To establish the same location name throughout the printed text.
	print """The story must take place somewhere! Your protagonist lives in the land of %s, which is famous for its abundance of %s.
Remarkably, the terrain contains several %s and %s, and the famed %s which brings many travelers from all across the world. (Some don't return home, for better or for worse.)
Plants such as the %s and %s flourish in %s as well. The head of government is %s %s, who is regarded as both a(n) %s and %s ruler.
Hopefully, your protagonist will survive your story and return home safely to a %s in %s!
	""" %(location, random.choice(fauna), random.choice(terrain_type), random.choice(terrain_type), random.choice(terrain_name),
	random.choice(plant_name), random.choice(plant_name), location, random.choice(leader_title), random.choice(first_name), 
	random.choice(positive_trait), random.choice(negative_trait), random.choice(home_type), location)

def cuisine():
	print "Cuisine Description"
	dish1 = random.choice(main_dish_name) #To establish the same dish name throughout the printed text.
	cuisine_type1 = random.choice(cuisine_type) #Adjectives to describe the food and the carb used vary by cuisine type
	if cuisine_type1 in ("soup", "stew", "curry", "noodle bowl"): #"Wet" dishes have a corresponding adjective and carb (noodle-related)
		food_adjective1 = random.choice(food_adjectives_wet)
		carb1 = random.choice(starch_type_pasta)
	elif cuisine_type1 in ("stir fry", "sandwich", "pot pie"):
		food_adjective1 = random.choice(food_adjectives_dry)
		carb1 = random.choice(starch_type_general) #Must be included here, as carb1 is more restrictive than food_adjective1
	elif cuisine_type1 in ("soup", "noodle bowl", "pasta"):
		carb1 = random.choice(starch_type_pasta)
	else: #Executed when Boolean expression is false (not any of the above mentioned cuisine types)
		food_adjective1 = random.choice(food_adjectives_wet) or random.choice(food_adjectives_dry)
		carb1 = random.choice(starch_type_general)
	print """Your character is sitting down to a meal known as the %s, a special delicacy in the land of %s.
While the chef claims it is a delicious %s %s, it has something on the surface that just doesn't seem edible: %s.
At least it is well-balanced; the protein is %s %s, which is situated above a bed of %s and surrounded by %s %s.
It's all seasoned with %s and garnished with a special %s flower. There is also a nice %s salad and some %s for to go! 
Your character digs into the %s. YUM! (Hopefully there are no adverse side effects!)
	""" %(dish1, random.choice(location_name), food_adjective1, cuisine_type1, random.choice(cuisine_feature), 
	random.choice(food_adjectives_preparation), random.choice(protein_type), carb1, random.choice(food_adjectives_preparation), 
	random.choice(vegetable_type), random.choice(seasoning_type), random.choice(plant_name), random.choice(fruit_type), 
	random.choice(dairy_type), dish1)

#########Additional functions (for user access within the program).######### Last updated April 27
#This is the main function in which all the others are nested (for easier viewing and editing).
#This is the algorithm that the user goes through (the main page) in order to choose which generator to use.
def main_func():
	print """Here is a list of different topics I can generate for you, %s. Preferably, please type the NUMBER only.
1.Characters\n2.Plants\n3.Setting\n4.Cuisine""" %name 
	
	main_choice = raw_input(">")
	if main_choice in ("1", "1.", "One", "one", "ONE", "Characters", "characters"):
		character_description() #From the defined functions above that randomly generate text.
		return_main() #This is at the end of each separate generator to reenter the main program.
		
	elif main_choice in ("2", "2.", "Two", "two", "TWO", "Plants", "plants"):
		land_plant() #From the defined functions above that randomly generate text.
		return_main() #This is at the end of each separate generator to reenter the main program.
		
	elif main_choice in ("3", "3.", "Three", "three", "THREE", "Setting", "setting"):
		setting() #From the defined functions above that randomly generate text.
		return_main() #This is at the end of each separate generator to reenter the main program.

	elif main_choice in ("4", "4.", "Four", "four", "FOUR", "Cuisine", "cuisine"):
		cuisine() #From the defined functions above that randomly generate text.
		return_main() #This is at the end of each separate generator to reenter the main program.
	
	else:
		print "Hey, you didn't follow instructions, so you don't get to use my program. Come back only when you're ready!"	
	
#This is the function used to keep the program running until the user decides to quit (user can return to main page).
#This is the algorithm that allows the user to return to the main page (and choose another random generator).
def return_main(): #This is the function used to decide if user wants to quit (end program) or return through main_func().
	print "To return to the random generator main page (with the table of contents), please type 'yes' or 'no'!" 
	print "To repeat or move directly to another sub-generator, please type the corresponding number (1, 2, 3, or 4)."
	return_choice = raw_input(">")
	if return_choice in ("yes", "yES", "YeS", "Yes", "Y", "y", "YES", "Ye", "ye", "YAS"):
		main_func() #Returns to main page (with all four generator possibilities).
	elif return_choice in ("no", "No", "NO", "N", "n", "nO", "NAY"):
		print "Thank you for using this program, I hope you have a nice day!" 
		
	#In order to streamline the process for those who want multiple descriptions of one aspect, I added four more options.
	#If the user types one of these four choices, they will go directly to the sub-generator.
	#Afterwards, return_main() will offer the choice again, to directly proceed or return to the main menu.
	elif return_choice in ("1", "1.", "One", "one", "ONE", "Characters", "characters"):
		character_description()
		return_main()
	elif return_choice in ("2", "2.", "Two", "two", "TWO", "Plants", "plants"):
		land_plant()
		return_main()
	elif return_choice in ("3", "3.", "Three", "three", "THREE", "Setting", "setting"):
		setting()
		return_main()
	elif return_choice in ("4", "4.", "Four", "four", "FOUR", "Cuisine", "cuisine"):
		cuisine()
		return_main()
	else:
		print "I will take that answer as a 'no'; thank you for using this program, I hope you have a nice day!"

#I put this section separately (not nested in program) as it's just a polite introduction when booting. Variable name is saved.
name = raw_input("Hello, dear user. What is your name?\n>")
print """Hello, %s! I am your assistant in this world-building generator for creative writing! 
My name is Pseudo Kode, and how may I help you?""" %name #The user will be referred by this name throughout the program.

#This is the abstracted main function that is the spine of the whole program.
main_func()