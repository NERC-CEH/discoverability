---
layout: default
title: Semantic Similarity
---
# Semantic Similarity
## Overview
Semantic similarity can be used to compare the similarity of 2 documents based on their documents embeddings. Here the document embeddings are encoded using the [SentenceTransformers](https://www.sbert.net/index.html) library. Several smaller models were trialed, the embeddings using each model were computed on the description of each dataset available in the EIDC. The models trialed were:

- `paraphrase-albert-small-v2`
- `all-MiniLM-L6-v2`

The example workbook uses the following questions (based on previous scoping work conducted by Lily Gouldbrough):

- **Where is the wettest soil in the UK?**
- **Where is water quality worst in the UK?**
- **Where are bird populations declining in the UK?**
- **Where in the UK are bumblebees most at risk from neonicotinoids?**
- **Which county in the UK has the most rivers?**

The embedding for each question is generated and the top 3 datasets from the EIDC (best cosine similarity) are returned.

*It should be noted that although the datasets returned may have semantic similarities - they may not actually contain the answers to the questions posed. For question and answering, a more comprehensive pipeline of retrieval augmented generation (RAG) could be considered.*

The python notebook used to generate these results can be found here: [`semantic_similarity.ipynb`](https://github.com/NERC-CEH/discoverability/blob/main/semantic_similarity.ipynb)

## Results

The title of the top 3 datasets, found using each model, for each question, can be seen below. For most questions the top datasets seem to be relevant to the query. A more thorough evaluation might involve building a test set of specific questions from domain experts and manually picking out the most appropriate datasets from the EIDC - this would allow the advantage of being able to apply some form of recall metric which would enable a more quanititaive comparison of different models, for now a qualitative comparison is all that is feasible.

### Where is the wettest soil in the UK?

|    | paraphrase-albert-small-v2                                 | all-MiniLM-L6-v2                                                                                |
|---:|:-----------------------------------------------------------|:------------------------------------------------------------------------------------------------|
|  0 | Soil invertebrate data 2007 [Countryside Survey]           | Topsoil physico-chemical properties from the UKCEH Countryside Survey, Great Britain, 2020, v2  |
|  1 | Soil physico-chemical properties 1998 [Countryside Survey] | Topsoil physico-chemical properties from the UKCEH Countryside Survey, Great Britain, 2021      |
|  2 | Soil invertebrate data 1998 [Countryside Survey]           | Topsoil physico-chemical properties from the UKCEH Countryside Survey, Great Britain, 2018-2019 |

### Where is water quality worst in the UK?

|    | paraphrase-albert-small-v2                                          | all-MiniLM-L6-v2                                                                                              |
|---:|:--------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------|
|  0 | Water quality data from the Ribble and Wyre catchments 2008-2010    | Water quality data from the Ribble and Wyre catchments 2008-2010                                              |
|  1 | Thames catchment hydrometric and water quality data 2013-17         | Weekly water quality data from the River Thames and its major tributaries (2009-2017)                         |
|  2 | Water quality data for the River Frome catchment, Dorset, 1976-2022 | Weekly water quality data from the River Thames and its major tributaries (2009-2013) [CEH Thames Initiative] |

### Where are bird populations declining in the UK?

|    | paraphrase-albert-small-v2                                                                                                      | all-MiniLM-L6-v2                                                                                        |
|---:|:--------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------|
|  0 | Annual estimates of occupancy for bryophytes, lichens and invertebrates in the UK (1970-2015)                                   | Diet, timing of egg laying and breeding success data for Isle of May European shag population 1985-2015 |
|  1 | UK ecological status map version 2                                                                                              | The Isle of May long-term study (IMLOTS) seabird annual breeding success 1982-2012                      |
|  2 | Annual estimates of occupancy for six invertebrate taxa in areas of high, low and no cropland cover in Great Britain, 1990-2019 | The Isle of May long-term study (IMLOTS) seabird annual breeding success 1982-2016                      |

### Where in the UK are bumblebees most at risk from neonicotinoids?

|    | paraphrase-albert-small-v2                                                                                         | all-MiniLM-L6-v2                                                                                                                 |
|---:|:-------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|
|  0 | Location data of worker bumblebees across an agricultural landscape in Buckinghamshire, UK                         | Location data of worker bumblebees across an agricultural landscape in Buckinghamshire, UK                                       |
|  1 | Microsatellite genotype data for five species of bumblebee across an agricultural landscape in Buckinghamshire, UK | Population responses of honeybees to oilseed rape neonicotinoid seed treatments in Hungary, Germany and the UK                   |
|  2 | Population responses of wild bees to oilseed rape neonicotinoid seed treatments in Hungary, Germany and the UK     | The number and individual weight of bumblebees (Bombus terrestris audax) from nests containing neonicotinoids in Wester Ross, UK |

### Which county in the UK has the most rivers?

|    | paraphrase-albert-small-v2                                                                                    | all-MiniLM-L6-v2                                                        |
|---:|:--------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------|
|  0 | UKCEH digital river network of Great Britain (1:50,000)                                                       | Integrated Hydrological Units of the United Kingdom: Groups             |
|  1 | Monthly measurements of major and trace elements in 41 rivers in Great Britain, 2017, from the LOCATE project | Spot gauged flows on the lower River Frome, Dorset, April-November 2022 |
|  2 | Gridded (1km) physical river characteristics for the UK v2                                                    | River Habitat Survey (RHS) data 2007 [Countryside Survey]               |
