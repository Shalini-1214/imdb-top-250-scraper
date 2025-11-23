from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
import os

def scrape_imdb_top_250(headless=False):
    # Chrome options
    options = Options()
    if headless:
        options.add_argument("--headless=new")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    url = "https://www.imdb.com/chart/top/"
    print("Loading IMDb Top 250 page...")
    driver.get(url)
    time.sleep(3)

    # Movie blocks (stable selector)
    movies = driver.find_elements(
        By.XPATH, "//li[contains(@class,'ipc-metadata-list-summary-item')]"
    )

    titles, years, ratings, ranks = [], [], [], []

    print("Extracting movie data...")
    for rank, movie in enumerate(movies, start=1):

        # ---------------------
        # TITLE (SAFE PARSING)
        # ---------------------
        title_raw = movie.find_element(By.XPATH, ".//h3").text
        if ". " in title_raw:
            title = title_raw.split(". ", 1)[1]
        else:
            title = title_raw

        # ---------------------
        # YEAR (correct class)
        # ---------------------
        year = movie.find_element(
            By.XPATH, ".//span[contains(@class,'cli-title-metadata-item')][1]"
        ).text

        # ---------------------
        # IMDb RATING
        # ---------------------
        rating = movie.find_element(
            By.XPATH, ".//span[contains(@class,'ipc-rating-star--rating')]"
        ).text

        titles.append(title)
        years.append(year)
        ratings.append(rating)
        ranks.append(rank)

    driver.quit()

    # Convert to DataFrame
    df = pd.DataFrame({
        "Rank": ranks,
        "Title": titles,
        "Year": years,
        "IMDb Rating": ratings
    })

    # ----------------------------------------
    # SAVE DIRECTLY TO DESKTOP (fixed)
    # ----------------------------------------
    save_path = r"C:\Users\HP\Desktop\imdb_top_250.csv"
    df.to_csv(save_path, index=False)

    print(f"\nSaved → {save_path}\n")
    return df


if __name__ == "__main__":
    df = scrape_imdb_top_250(headless=False)
    print(df.head())
