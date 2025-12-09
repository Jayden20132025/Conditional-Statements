def suggest_clothing(temperature_celsius):
    """
    Suggests appropriate clothing based on the given temperature in Celsius.

    Args:
        temperature_celsius (float): The temperature in Celsius.

    Returns:
        str: A suggestion for what to wear.
    """

    if temperature_celsius > 25:
        return "It's warm! Wear light and breathable clothing like shorts and a t-shirt."
    elif 20 <= temperature_celsius <= 25:
        return "It's a pleasant temperature.  A light shirt and pants or a skirt would be comfortable."
    elif 15 <= temperature_celsius < 20:
        return "It's getting a bit cooler. Consider a light jacket or sweater with long sleeves."
    elif 10 <= temperature_celsius < 15:
        return "It's cool. Wear a jacket or a light coat."
    else:
        return "It's cold! Wear a warm coat, gloves, and a hat."

# Get temperature input from the user
try:
    temperature = float(input("Enter the temperature in Celsius: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

# Get clothing suggestion
clothing_suggestion = suggest_clothing(temperature)

# Print the suggestion
print(clothing_suggestion)