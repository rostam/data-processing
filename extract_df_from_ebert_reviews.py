import glob, pandas as pd

df_list = []
for ebert_review in glob.glob('ebert_reviews/*.txt'):
    with open(ebert_review, encoding='utf-8') as file:
        title = file.readline()[:-1]
        review_url = file.readline()
        review_text = file.read()
        df_list.append({
            'title': title,
            'review_url': review_url,
            'review_text': review_text
        })

df = pd.DataFrame(df_list, columns=['title','review_url','review_text'])

df.info()


