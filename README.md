# 🎬 IMDb Top 250 Scraper

This Python script scrapes the **IMDb Top 250 movies** using Selenium and saves the data to a CSV file.

It extracts:
- Rank
- Title
- Year
- IMDb Rating

The final CSV (`imdb_top_250.csv`) is saved directly to your Desktop.

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Script

```bash
python imdb_scraper.py
```

---

## 🧰 Requirements

This script uses:
- Selenium
- Pandas
- Webdriver Manager

Chrome is required. ChromeDriver installs automatically.

---

## 📁 Output

The script generates:

```
C:\Users\HP\Desktop\imdb_top_250.csv
```

---

## ⚠️ Notes

- IMDb frequently changes its HTML structure. If selectors break, update the XPaths.
- Headless mode can be enabled by passing `headless=True` to the function.

---

## 📄 License

Optional — add MIT License if you want.
