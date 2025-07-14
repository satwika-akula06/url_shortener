import random
import string

# Dictionary to store short code from original url 
url_database = {}

# Function to generate random 6-character short code
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

# Function to shorten a URL
def shorten_url():
    original_url = input("Enter the long URL: ").strip()
    short_code = generate_short_code()
    url_database[short_code] = original_url
    print(f"Short URL: short.ly/{short_code}\n")

# Function to retrieve the original URL
def retrieve_url():
    full_input = input("Enter the short code or full short URL: ").strip()

    # If full short URL is entered, extract only the short code
    if full_input.startswith("short.ly/"):
        short_code = full_input.split("short.ly/")[-1]
    else:
        short_code = full_input

    if short_code in url_database:
        print(f"Original URL: {url_database[short_code]}\n")
    else:
        print("Short code not found.\n")

# Main loop
def main():
    print("🔗 Welcome to the URL Shortener!\n")

    while True:
        print("Choose an option:")
        print("1. Shorten a new URL")
        print("2. Retrieve original URL")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            shorten_url()
        elif choice == '2':
            retrieve_url()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

# Run the program
if __name__ == "__main__":
    main()
