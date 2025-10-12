import datetime
def distance_time(distance, speed):
    time_hours = distance / speed
    time_seconds = time_hours * 3600
    return time_seconds
def convert(seconds):
    return str(datetime.timedelta(seconds = seconds))
places = {
    "1": ("Siem Reap", 314),
    "2": ("Bokor", 189),
    "3": ("Kirirum", 117),
    "4": ("Kampot", 148),
    "5": ("Krong Kep", 174),
    "6": ("Sihanoukville", 230),
    "7": ("Kampong Chnang", 91),
    "8": ("Pursat", 189),
    "9": ("Battambang", 291),
    "10": ("Pailin", 371),
    "11": ("Banteay Meanchey", 359),
    "12": ("Kampong Thom", 167),
    "13": ("Kampong Cham", 124),
    "14": ("Prey Veng", 90),
    "15": ("Svay Rieng", 122),
    "16": ("Takeo", 78),
    "17": ("Kandal", 11),
    "18": ("Kampong Speu", 48),
    "19": ("Kratie", 315),
    "20": ("Steung Treng", 455),
    "21": ("Mondulkiri", 521),
    "22": ("Preah Vihear", 294),
    "23": ("Ratanakiri", 588),
    "24": ("Koh Kong", 271),
    "25": ("Oddar Meanchey", 469)
}
print("Select a destination:")
for key, (place, dist) in places.items():
    print(f"{key}. Phnom Penh to {place} - {dist} km")
choice = input("\nEnter number for place: ")
if choice in places:
    destination, distance = places[choice]
    speed = int(input("Enter speed in km/h: "))
    time_seconds = distance_time(distance, speed)
    print(f"\nTime taken to travel from Phnom Penh to {destination} is: {convert(time_seconds)}")
else:
    print("Invalid selection.")
