---
layout: default
title: Exact Match
parent: Question Answering
---
# Overview
Exact match question and answering is the process of looking for the answer to a question in a given context e.g. search for a particular part of a text document that contains the answer to a query. This technique has the advantage over generative approaches that the model cannot hallucinate an answer - the context document must will always contain the information that is returned. However it is important to view the full context around the answer found in the text to ensure that the expected answer is actually expected and not just part of the context document that sounds appropriate.

The [HuggingFace]() library can be used to build simple exact match question answering pipeline using pretrained models. In this example the following models are trialed:
- `roberta-base-squad2`
- `distilbert-base-cased-distilled-squad`
- `minilm-uncased-squad2`

These were chosen as they are 3 of the most popular models available through HuggingFace for the question answering task.

A set of sample documents (dataset descriptions) were selected and a small set of sample questions (that were answerable) were derived.  The answers provided from each of the models are displayed below and the python notebook used to generate these results can be found here: [`qa.ipynb`](https://github.com/NERC-CEH/discoverability/blob/main/qa.ipynb)

## Dataset: Location data of worker bumblebees across an agricultural landscape in Buckinghamshire, UK

*Description: This dataset contains locations of worker bumblebees of five species (Bombus terrestris, B. lapidarius, B. pascuorum, B. hortorum, B. ruderatus) across an agricultural landscape centred on the Hillesden Estate, Buckinghamshire, UK. Locations were recorded in the field using a handheld GPS unit. Workers were non-lethally DNA sampled between June and August 2011, and genetic analysis used to confirm species and assign individuals to full-sib groups (colonies). Data were collected as part of a project led by the Centre for Ecology & Hydrology, funded under the Insect Pollinators Initiative.*

| Question                                         | How was DNA sampling performed? | Who funded the project?        | Where was the data gathered?          |
|:-------------------------------------------------|:--------------------------------|:-------------------------------|:--------------------------------------|
| deepset/roberta-base-squad2                      | non-lethally                    | Centre for Ecology & Hydrology | Hillesden Estate, Buckinghamshire, UK |
| distilbert/distilbert-base-cased-distilled-squad | handheld GPS unit               | Insect Pollinators Initiative  | Hillesden Estate, Buckinghamshire, UK |
| deepset/minilm-uncased-squad2                    | non-lethally                    | Insect Pollinators Initiative  | Hillesden Estate, Buckinghamshire, UK |
| deepset/bert-base-cased-squad2                   | non-lethally                    | Insect Pollinators Initiative  | Hillesden Estate, Buckinghamshire, UK |
| Intel/dynamic_tinybert                           | using a handheld GPS unit       | Insect Pollinators Initiative  | Hillesden Estate, Buckinghamshire, UK |