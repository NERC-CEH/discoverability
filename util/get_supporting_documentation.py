#!/usr/bin/env python

import yaml, requests, json, os


def download_supporting_documentation(url, metadata_file, save_path):
    with open(metadata_file, 'r') as f:
        data = json.load(f)
        for item in data.get('results'):
            id = item['identifier']
            file = f'{id}.zip'
            link = f'{url}{file}'
            save = f'{save_path}/{file}'
            download_item(link, save)


def download_item(url, save_file):
    print(f'Downloading {url} -> {save_file}...')
    resp = requests.get(url)
    os.makedirs(os.path.dirname(save_file), exist_ok=True)
    with open(save_file, 'wb') as f:
        f.write(resp.content)
    

if __name__ == '__main__':
    config = yaml.safe_load(open('config.yml'))
    download_supporting_documentation(config['supporting_url'], config['metadata_file'], config['save_path'])