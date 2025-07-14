import requests
import random
from datetime import datetime, timedelta

# 40 groups, 10 transactions each
base_descriptions = [
    "grocery shopping at Walmart",
    "fuel purchase at Shell",
    "monthly rent payment",
    "dining at McDonald's",
    "online shopping at Amazon",
    "coffee at Starbucks",
    "movie tickets at AMC",
    "gym membership payment",
    "pharmacy purchase at CVS",
    "utility bill payment",
    "electronics at Best Buy",
    "clothing at H&M",
    "book purchase at Barnes & Noble",
    "flight booking with Delta",
    "hotel stay at Marriott",
    "car maintenance at Jiffy Lube",
    "public transport fare",
    "insurance premium payment",
    "subscription to Netflix",
    "concert tickets at Ticketmaster",
    "pet supplies at PetSmart",
    "home improvement at Home Depot",
    "fast food at Burger King",
    "mobile recharge",
    "parking fee payment",
    "donation to Red Cross",
    "spa treatment at Bliss Spa",
    "toy purchase at Toys R Us",
    "furniture at IKEA",
    "garden supplies at Lowe's",
    "music streaming at Spotify",
    "hardware tools at Ace Hardware",
    "taxi ride with Uber",
    "haircut at Supercuts",
    "laundry service",
    "gift shopping at Hallmark",
    "sports gear at Decathlon",
    "art supplies at Michaels",
    "baking goods at Whole Foods",
    "pet grooming at Petco",
    "office supplies at Staples"
]

# Variations for each group
variations = [
    "bought groceries at {}",
    "weekly grocery run at {}",
    "purchased food at {}",
    "supermarket shopping at {}",
    "grocery shopping at {}",
    "restocked pantry at {}",
    "food shopping at {}",
    "grocery haul from {}",
    "picked up groceries at {}",
    "shopping for food at {}"
]

merchants = [
    "Walmart", "Shell", "Landlord", "McDonald's", "Amazon", "Starbucks", "AMC", "Gold's Gym", "CVS", "Utility Co",
    "Best Buy", "H&M", "Barnes & Noble", "Delta", "Marriott", "Jiffy Lube", "Metro", "Insurance Co", "Netflix", "Ticketmaster",
    "PetSmart", "Home Depot", "Burger King", "AT&T", "City Parking", "Red Cross", "Bliss Spa", "Toys R Us", "IKEA", "Lowe's",
    "Spotify", "Ace Hardware", "Uber", "Supercuts", "Laundry Co", "Hallmark", "Decathlon", "Michaels", "Whole Foods", "Petco", "Staples"
]

# Generate dates from July to December 2025
def random_date_2025():
    month = random.randint(7, 12)
    day = random.randint(1, 28)  # To avoid invalid dates
    return f"2025-{month:02d}-{day:02d}"

for group in range(40):
    base_desc = base_descriptions[group % len(base_descriptions)]
    merchant = merchants[group % len(merchants)]
    for i in range(10):
        desc = variations[i].format(merchant) if group == 0 else f"{base_desc} ({i+1})"
        tx = {
            "date": random_date_2025(),
            "amount": round(random.uniform(10, 200), 2),
            "category": base_desc.split()[0].capitalize(),
            "description": desc,
            "merchant": merchant
        }
        r = requests.post("http://localhost:8000/transactions/", json=tx)
        print(f"Group {group+1}, Tx {i+1}: {r.status_code} - {r.json() if r.status_code == 200 else r.text}") 