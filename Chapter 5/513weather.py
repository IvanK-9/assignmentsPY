def get_weather_input():
    """Get weather information from user"""
    print("=== Weather Clothing Advisor ===")
    
    # Get temperature
    while True:
        try:
            temperature = float(input("Enter current temperature in Celsius: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Get weather type
    weather_types = ['sunny', 'rainy', 'cloudy', 'snowy', 'windy']
    weather = input(f"Enter weather type ({'/'.join(weather_types)}): ").lower()
    while weather not in weather_types:
        print(f"Please choose from: {', '.join(weather_types)}")
        weather = input("Enter weather type: ").lower()
    
    return temperature, weather

def recommend_clothing(temperature):
    """Recommend clothing based on temperature"""
    # Your code here
    pass

def recommend_umbrella(weather):
    """Recommend if umbrella is needed"""
    # Your code here
    pass

def main():
    # Get weather data
    temperature, weather = get_weather_input()
    
    # Get recommendations
    clothing = recommend_clothing(temperature)
    umbrella = recommend_umbrella(weather)
    
    # Display results
    print("\n=== RECOMMENDATIONS ===")
    print(f"Temperature: {temperature}°C")
    print(f"Weather: {weather.capitalize()}")
    print(f"Clothing: {clothing}")
    print(f"Umbrella: {umbrella}")

if __name__ == "__main__":
    main()