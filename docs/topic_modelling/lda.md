---
layout: default
title: LDA
parent: Topic Modelling
---
# LDA

Latent Dirichlet Allocation (LDA) is a form of topic modelling that can be applied using many different tools. Here [Gensim](https://radimrehurek.com/gensim/) is used to generate topics. The text from the EIDC metadata descriptions is tokenised using [NLTK](https://www.nltk.org/) and then handed to Gensim's LDA model, specifying `6` topics. The topics are visualised below along the first 2 principle components. Hovering over each topic will show the most salient terms for that topic. The code for generate this model and visualisation can be found here: [`lda_gensim.ipynb`]()

{% raw %}
<iframe src="gensim_lda.html" width="1250px" height="900px" frameborder="no" left="0"/>
{% endraw %}
