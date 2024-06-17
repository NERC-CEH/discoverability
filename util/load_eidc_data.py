import json
import pandas as pd


def load_title_description_lineage(file_path):
    titles = []
    texts = []
    with open(file_path, 'r') as f:
        data = json.load(f)
        for item in data.get('results'):
            desc = item['description']
            title = item['title']
            lineage = item['lineage']
            titles.append(title)
            texts.append(f'{title}\n{desc}\n{lineage}')
    return texts, titles


def load_as_df(file_path, fields=['title', 'description', 'lineage']):
    datasets = []
    with open(file_path, 'r') as f:
        data = json.load(f)
        for item in data.get('results'):
            dataset = []
            for field in fields:
                dataset.append(item[field])
            datasets.append(dataset)
    return pd.DataFrame(datasets, columns=fields)


if __name__ == '__main__':
    texts = load_title_description_lineage('../eidc_data_scraping/catalogue_metadata.json')
    print(len(texts))