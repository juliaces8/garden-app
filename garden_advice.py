def get_gardening_advice(season, plant_type):
    """
    Returns gardening advice based on the season and type of plant.
    Uses dictionaries to map inputs to specific advice strings.
    """
    # 1. Store advice in a dictionary (Satisfies TODO)
    seasonal_data = {
        "summer": "Water your plants regularly and provide some shade.",
        "winter": "Protect your plants from frost with covers.",
        "spring": "Prepare the soil and start planting new seeds.",
        "autumn": "Mulch your garden to protect roots for the winter."
    }

    plant_data = {
        "flower": "Use fertiliser to encourage blooms.",
        "vegetable": "Keep an eye out for pests!",
        "herb": "Trim regularly to encourage bushy growth."
    }

    # 2. Use .get() to find advice or return a default message
    s_advice = seasonal_data.get(season, "No specific advice for this season.")
    p_advice = plant_data.get(plant_type, "No specific advice for this plant.")

    return f"{s_advice}\n{p_advice}"


def main():
    """Main function to handle user interaction and output."""
    print("--- Welcome to the Gardening Enthusiast App ---")

    # 3. Get User Input (Satisfies TODO)
    user_season = input("Enter the current season: ").strip().lower()
    user_plant = input("Enter your plant type: ").strip().lower()

    # 4. Generate and display advice
    result = get_gardening_advice(user_season, user_plant)

    print("\n--- Your Gardening Advice ---")
    print(result)


if __name__ == "__main__":
    main()
