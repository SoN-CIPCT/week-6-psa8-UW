# Conditional Lists Exercise
# 1. Create a list with five or more user names
web_users = ["john123", "sarah_m", "mike_cool", "emma_w", "alex_2024"]
# 2. Create a second list with five user names (two should match web_users)
new_users = ["sarah_m", "chris_p", "alex_2024", "jordan_k", "taylor_s"]
# 3. Loop through new_users and check if each name is already used
for username in new_users:
    if username in web_users:
        print("This user name is already in use. Please choose a different user name.")
    else:
        print("This user name is available.")


        # Nested Dictionaries Exercise
# 1. Create a dictionary with three cities
cities = {}
# 2. For each city, create a nested dictionary
cities["Tokyo"] = {
    "country": "Japan",
    "population": 14000000,
    "fact": "Tokyo is the world's largest metropolitan area"
}
cities["Paris"] = {
    "country": "France",
    "population": 2100000,
    "fact": "Paris is known as the City of Light"
}
cities["Cairo"] = {
    "country": "Egypt",
    "population": 9500000,
    "fact": "Cairo is home to the ancient pyramids of Giza"
}
# 4. Print the information in the specified format
for city, info in cities.items():
    print(f"City: {city}; Country: {info['country']}; Population: {info['population']}; Fact: {info['fact']};", end=" ")
    