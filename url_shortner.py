import json
import random
import string

urls = {}

def generate_code():
    while True:
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        if short_url not in urls:
            return short_url

def add_url(code, original_url):
    urls[code] = original_url

def save_urls():
    with open("urls.json", "w") as f:
        json.dump(urls, f, indent=4)

def load_urls():
    global urls
    try:
        with open("urls.json", "r") as f:
            urls = json.load(f)
            print("URLs loaded successfully!")
    except FileNotFoundError:
        urls = {}
        print("No existing URLs found. Starting with an empty URL list.")

load_urls()

while True:
    print("\n===== URL Shortener =====")
    print("1. Shorten URL")
    print("2. Retrieve Original URL")
    print("3. View All URLs")
    print("4. Rename Short Code")
    print("5. Delete URL")
    print("6. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        url = input("Enter the URL: ")
        if url == "":
            print("URL cannot be empty. Please enter a valid URL.")
            continue    
        elif not url.startswith("http://") and not url.startswith("https://"):
            print("Invalid URL format. Please enter a valid URL.")
            continue
        while True:
            print("Do you want to provide a custom code? (y/n)")
            custom_code_choice = input().strip().lower()
            if custom_code_choice == 'y':
                while True:
                    code = input("Enter custom code: ").strip()
                    if code == "":
                        print("Code cannot be empty. Please enter a valid code.")
                    elif code in urls:
                        print("Code already exists. Please choose a different code.")
                    else:
                        break
                break
            elif custom_code_choice == 'n':
                code = generate_code()
                break
            else:
                print("Invalid choice. Please enter 'y' or 'n'.")
                continue
        add_url(code, url)
        save_urls()
        print("URL shortened successfully!\nShort code:", code, "\nOriginal URL:", url)


    elif choice == "2":
        code = input("Enter the short code: ").strip()
        if code in urls:
            print("Original URL:", urls[code])
        else:
            print("Short code not found.")

    elif choice == "3":
        if not urls:
            print("No URLs found.")
        else:
            for short_code, original_url in urls.items():
                print(f"Short Code: {short_code}")
                print(f"Original URL: {original_url}")
                print()

    elif choice == "4":
        old_code = input("Enter the current short code: ").strip()
        if old_code in urls:
            new_code = input("Enter the new short code: ").strip()
            if new_code == "":
                print("New code cannot be empty.")
            elif new_code in urls:
                print("New code already exists. Please choose a different code.")
            else:
                urls[new_code] = urls.pop(old_code)
                save_urls()
                print(f"Short code '{old_code}' has been renamed to '{new_code}'.")
        else:
            print("Short code not found.")

    elif choice == "5":
        code = input("Enter the short code to delete: ").strip()
        if code in urls:
            del urls[code]
            save_urls()
            print(f"Short code '{code}' has been deleted.")
        else:
            print("Short code not found.")

    elif choice == "6":
        print("Goodbye!")
        save_urls()
        break

    else:
        print("Invalid choice. Please try again.")

