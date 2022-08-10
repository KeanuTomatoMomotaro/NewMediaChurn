import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('_mpl-gallery-nogrid')


# Use https://newsapi.org/ to fetch news in Indonesia
def fetch_headline_news():
    api_key = "your_api_key"

    url = "https://newsapi.org/v2/top-headlines?category=general&country=id&pageSize=100&apiKey="+api_key

    response = requests.get(url)

    arr_of_articles = response.json()["articles"]

    return arr_of_articles


# Output raw articles data to Excel for possible analysis / proving
def output_to_excel(arr_articles):
    # Some dictionary key are nested, I normalize them
    # to remove nested source key:value and store only source name, article title and short description.
    arr_norm = []

    for article in arr_articles:
        arr_norm.append({
            "source name": article["source"]["name"],
            "title": article["title"],
            "description": article["description"],
            "date": article["publishedAt"]
        })

    df = pd.DataFrame(data=arr_norm)
    df.to_excel("headlines.xlsx", index=False)


# Count amount of articles published by a certain publisher
def count_news_articles(arr_articles):
    arr_names = []
    arr_count = []

    for article in arr_articles:
        if article["source"]["name"] in arr_names:
            i = arr_names.index(article["source"]["name"])
            arr_count[i] += 1
        elif article["source"]["name"] not in arr_names:
            arr_names.append(article["source"]["name"])
            arr_count.append(1)

    return arr_names, arr_count


if __name__ == '__main__':
    articles = fetch_headline_news()

    output_to_excel(articles)

    names, count = count_news_articles(articles)

    # plot
    fig, ax = plt.subplots()
    colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(count)))

    ax.pie(count, colors=colors, labels=names, radius=3, center=(4, 4),
           wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(0, 8), yticks=np.arange(1, 8))

    plt.show()
