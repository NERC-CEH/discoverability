import json


def load_titles_and_descriptions(file_path):
    texts = []
    with open(file_path, 'r') as f:
        data = json.load(f)
        for item in data.get('results'):
            desc = item['description']
            title = item['title']
            texts.append(f'{title}\n{desc}')
    return texts


if __name__ == '__main__':
    texts = load_titles_and_descriptions('../eidc_data_scraping/catalogue_metadata.json')
    print(len(texts))