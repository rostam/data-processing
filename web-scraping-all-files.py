import bs4, os, pandas as pd, matplotlib.pyplot as plt

# import requests
# url = "https://www.rottentomatoes.com/m/et_the_extraterrestrial"
# response = requests.get(url)
# soup = BeatifulSoup(response.content, 'lxml')


df_list = []
folder = 'rt_html'
for movie_html in os.listdir(folder):
    with open(os.path.join(folder, movie_html)) as file:
        soup = bs4.BeautifulSoup(file, 'lxml')
        title = soup.find('title').contents[0][:-len(' - Rotten Tomatoes')]
        audience_score = soup.find('div', class_='audience-score meter').find('span').contents[0][:-1]
        num_audience = soup.find('div', class_='audience-info hidden-xs superPageFontColor').find_all('div')[1].contents[2].strip().replace(',', '')
        df_list.append({
            'title': title,
            'audience_score': int(audience_score),
            'num_audience': int(num_audience)
        })
        # print(title, audience_score, int(num_audience))
        # print(df_list)
        # break

df = pd.DataFrame(df_list, columns=['title', 'audience_score', 'num_audience'])
df.info()

plt.scatter(df.audience_score, df.critic_score)


