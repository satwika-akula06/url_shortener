# 🔗 Console URL Shortener

A simple command-line Python application to shorten long URLs and retrieve the original URLs using short codes — just like `bit.ly`, but in your terminal.

---

## 🚀 How It Works

1. **Shorten URL**: You enter a long URL, and the program gives you a random short code like `short.ly/XyZ123`
2. **Retrieve URL**: You can enter either the short code or full short URL to get back the original long URL
3. All data is stored temporarily during the session using Python dictionaries

---

## 📌 Features

- Generate short codes for long URLs
- Retrieve original URLs using short codes or full short URLs
- Interactive CLI menu
- Basic error handling

---

## 🧠 Technologies Used

- Python 3
- Built-in modules: `random`, `string`
- Data structures: dictionaries
- Command Line Interface (CLI)

---

## 🖥️ How to Run

1. Clone or download this repository
2. Open terminal in the project folder
3. Run the app using:

```bash
python url_shortener.py
```

##  🧪 Sample Output

🔗 Welcome to the URL Shortener!

Choose an option:
1. Shorten a new URL
2. Retrieve original URL
3. Exit
> 1

Enter the long URL: https://example.com/blog/article

Short URL: short.ly/Ak2Gh7

> 2
Enter the short code or full short URL: short.ly/Ak2Gh7

Original URL: https://example.com/blog/article

## 📁 Project Structure

console-url-shortener/

├── url_shortener.py     # Main Python file

└── README.md            # Project description

## 📎 Note

- Data is stored only during a single run — if you restart the script, previous mappings will be lost.

- You can enter either:

    - Just the short code: Ak2Gh7

    - Or the full short URL: short.ly/Ak2Gh7
