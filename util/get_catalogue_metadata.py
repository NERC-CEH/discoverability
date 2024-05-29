#!/usr/bin/env python

import yaml, requests, json


def download_and_save_catalogue_metadata(url, output_file):
    print(f'Retrieving data from {url}')
    params = {'term': 'state:published AND view:public AND recordType:Dataset', 'rows': '2000'}
    response = requests.get(url, params=params)
    with open(output_file, 'w') as f:
        json.dump(response.json(), f, indent=4)
    print(f'Response save to {output_file}')


if __name__ == '__main__':
    config = yaml.safe_load(open('config.yml'))
    download_and_save_catalogue_metadata(config['url'], config['metadata_file'])
    