import pandas as pd

# Get 30th titles + cleaning
def titles30(URL):
    web_page = pd.read_html(URL)

    titles= web_page[2]
    titles.dropna(how = "all", inplace = True)
    titles.dropna(axis = 1, how = "all", inplace = True)
    titles.columns = ["Rank", "Title"]
    titles = titles[0:len(titles):2]
    titles.drop(91, inplace = True)
    titles.reset_index(inplace = True)
    titles.drop(titles.columns[0], axis = 1, inplace = True)

    mistakes = {"â": "'", "â": "-", "â": '"', "â\x80\x9d": '"', "Ä": "Ć"}
    titles["Title"] = titles["Title"].replace(mistakes, regex = True)

    return titles


# Get 60th titles and drop irrelevant columns
first30 = titles30("https://news.ycombinator.com/")
last30 = titles30("https://news.ycombinator.com/news?p=2")
all_titles = pd.concat([first30, last30], axis=0).set_index("Rank")
all_titles = all_titles[:40]

print(all_titles)