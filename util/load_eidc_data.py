import json


def load_title_description_lineage(file_path):
    texts = []
    with open(file_path, 'r') as f:
        data = json.load(f)
        for item in data.get('results'):
            desc = item['description']
            title = item['title']
            lineage = item['lineage']
            texts.append(f'{title}\n{desc}\n{lineage}')
    return texts


if __name__ == '__main__':
    texts = load_title_description_lineage('../eidc_data_scraping/catalogue_metadata.json')
    print(len(texts))