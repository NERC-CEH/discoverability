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

|    | paraphrase-MiniLM-L3-v2                                                 | all-MiniLM-L6-v2                                                                                | multi-qa-MiniLM-L6-cos-v1                                                                                                                   |
|---:|:------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | Soil physico-chemical properties from eight UK agricultural sites, 2022 | Topsoil physico-chemical properties from the UKCEH Countryside Survey, Great Britain, 2020, v2  | Hydraulic and hydrological data from surface and subsurface soils across the Thames catchment, UK, 2021                                     |
|  1 | Soil physico-chemical properties 1978 [Countryside Survey]              | Topsoil physico-chemical properties from the UKCEH Countryside Survey, Great Britain, 2021      | Soil water release curves and hydraulic conductivity measurements at four long-term grassland-to-woodland land use contrasts across England |
|  2 | Soil physico-chemical properties 2007 [Countryside Survey]              | Topsoil physico-chemical properties from the UKCEH Countryside Survey, Great Britain, 2018-2019 | Topsoil physico-chemical properties from the UKCEH Countryside Survey, Great Britain, 2022                                                  |

### Where is water quality worst in the UK?

|    | paraphrase-MiniLM-L3-v2                                                                                   | all-MiniLM-L6-v2                                                                                              | multi-qa-MiniLM-L6-cos-v1                                        |
|---:|:----------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------|
|  0 | Baseflow chemistry of streams draining rural and agricultural land in the Wolds region of eastern England | Water quality data from the Ribble and Wyre catchments 2008-2010                                              | Thames catchment hydrometric and water quality data 2013-17      |
|  1 | Thames catchment hydrometric and water quality data 2013-17                                               | Weekly water quality data from the River Thames and its major tributaries (2009-2017)                         | Water quality data from the Ribble and Wyre catchments 2008-2010 |
|  2 | Water quality data from the Ribble and Wyre catchments 2008-2010                                          | Weekly water quality data from the River Thames and its major tributaries (2009-2013) [CEH Thames Initiative] | Conwy catchment - spatial water chemistry dataset                |

### Where are bird populations declining in the UK?

|    | paraphrase-MiniLM-L3-v2                                                                   | all-MiniLM-L6-v2                                                                                        | multi-qa-MiniLM-L6-cos-v1                                                                               |
|---:|:------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------|
|  0 | Avian data from the South Fork McKenzie River in Oregon, USA after a wildfire event, 2021 | Diet, timing of egg laying and breeding success data for Isle of May European shag population 1985-2015 | UK Environmental Change Network (ECN) common breeding birds data 1971-2007                              |
|  1 | UK Environmental Change Network (ECN) common breeding birds data 1971-2007                | The Isle of May long-term study (IMLOTS) seabird annual breeding success 1982-2012                      | Diet, timing of egg laying and breeding success data for Isle of May European shag population 1985-2015 |
|  2 | UK Environmental Change Network (ECN) bird data: 1995-2012                                | The Isle of May long-term study (IMLOTS) seabird annual breeding success 1982-2016                      | UK Environmental Change Network (ECN) bird data: 1995-2012                                              |

### Where in the UK are bumblebees most at risk from neonicotinoids?

|    | paraphrase-MiniLM-L3-v2                                                                                        | all-MiniLM-L6-v2                                                                                                                 | multi-qa-MiniLM-L6-cos-v1                                                                                      |
|---:|:---------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------|
|  0 | Population responses of honeybees to oilseed rape neonicotinoid seed treatments in Hungary, Germany and the UK | Location data of worker bumblebees across an agricultural landscape in Buckinghamshire, UK                                       | Population responses of wild bees to oilseed rape neonicotinoid seed treatments in Hungary, Germany and the UK |
|  1 | Population responses of wild bees to oilseed rape neonicotinoid seed treatments in Hungary, Germany and the UK | Population responses of honeybees to oilseed rape neonicotinoid seed treatments in Hungary, Germany and the UK                   | Invasive and native bumblebee abundance along a latitudinal gradient within Argentina and Chile, 2019-2020     |
|  2 | Invasive and native bumblebee abundance along a latitudinal gradient within Argentina and Chile, 2019-2020     | The number and individual weight of bumblebees (Bombus terrestris audax) from nests containing neonicotinoids in Wester Ross, UK | Population responses of honeybees to oilseed rape neonicotinoid seed treatments in Hungary, Germany and the UK |

### Which county in the UK has the most rivers?

|    | paraphrase-MiniLM-L3-v2                                                    | all-MiniLM-L6-v2                                                        | multi-qa-MiniLM-L6-cos-v1                                               |
|---:|:---------------------------------------------------------------------------|:------------------------------------------------------------------------|:------------------------------------------------------------------------|
|  0 | Water temperatures for the period 1984 to 2007 at 35 sites on 21 UK rivers | Integrated Hydrological Units of the United Kingdom: Groups             | Spot gauged flows on the lower River Frome, Dorset, April-November 2022 |
|  1 | Plynlimon research catchments: river network                               | Spot gauged flows on the lower River Frome, Dorset, April-November 2022 | Hydraulics data for the River Lambourn at Boxford, 2008 to 2014         |
|  2 | Thames catchment hydrometric and water quality data 2013-17                | River Habitat Survey (RHS) data 2007 [Countryside Survey]               | Gridded (1km) physical river characteristics for the UK v2              |