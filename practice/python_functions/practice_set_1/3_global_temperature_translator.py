# Using f-strings for output, and apply this to a practical scenario of temperature conversion.

# You are creating a feature for a travel app that allows users to view the temperature in both
# Celsius and Fahrenheit, so they can easily understand the weather forecast no matter where
# they travel.

# 1. Create a list of temperatures in Celsius that you want to convert.
# 2. Loop through the list, and for each temperature in Celsius, convert it to Fahrenheit.
# 3. Print out both the Celsius and Fahrenheit temperatures using f-strings for formatted output.

celsius_temperatures = [50, -14, 12, 20, 35]

for celsius in celsius_temperatures:
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}C is equivalent to {fahrenheit}F")

    