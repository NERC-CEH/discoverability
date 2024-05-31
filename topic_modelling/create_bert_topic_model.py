#!/usr/bin/env python

# This is just a hacky work around to run the scripts - eventually everything should be packaged up nicely
import sys
sys.path.append('../')

import yaml
from util import load_eidc_data
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer
from umap import UMAP
from hdbscan import HDBSCAN
from sklearn.feature_extraction.text import CountVectorizer
from bertopic.representation import KeyBERTInspired, PartOfSpeech, MaximalMarginalRelevance


def create_bert_topic_model(data_file, output):
    print('Loading texts...')
    texts = load_eidc_data.load_title_description_lineage(data_file)
    print('Creating embeddings...')
    embedding_model, embeddings = create_embeddings(texts)
    print('Creating topic model...')
    topic_model = create_topic_model(embedding_model)
    print('Fitting topic model...')
    topics, probs = topic_model.fit_transform(texts, embeddings)
    print(topic_model.get_topic_info())
    print('Creating visualisation...')
    fig = topic_model.visualize_document_datamap(texts, embeddings=embeddings)
    fig.savefig(f'{output}/topic_datamap.png', bbox_inches='tight')


def create_embeddings(texts):
    embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = embedding_model.encode(texts)
    return embedding_model, embeddings


def create_topic_model(embedding_model):
    umap_model = UMAP(n_neighbors=15, n_components=5, min_dist=0.0, metric='cosine', random_state=42)
    hdbscan_model = HDBSCAN(min_cluster_size=20, metric='euclidean', cluster_selection_method='eom', prediction_data=True)
    keybert_model = KeyBERTInspired()
    pos_model = PartOfSpeech('en_core_web_sm')
    mmr_model = MaximalMarginalRelevance(diversity=0.3)
    representation_model={
        'POS': pos_model,
        'MMR': mmr_model,
        'KeyBERT': keybert_model
    }
    vectorizer_model = CountVectorizer(stop_words='english', min_df=2, ngram_range=(1,2))
    return BERTopic(
        embedding_model=embedding_model,
        umap_model=umap_model,
        hdbscan_model=hdbscan_model,
        vectorizer_model=vectorizer_model,
        representation_model=representation_model,
        top_n_words=10,
        verbose=True
    )


if __name__ == '__main__':
    config = yaml.safe_load(open('../config.yml'))
    create_bert_topic_model(f"../{config['metadata_file']}", f"../{config['save_path']}")