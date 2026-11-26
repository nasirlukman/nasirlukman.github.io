---
layout: post
title: "Satellite Embeddings and the Rise of Foundation Models in Earth Observation"
date: 2025-11-07 23:36:10
description: "Evaluating Google Satellite Embeddings (AlphaEarth) for large-scale land cover classification in Indonesia, and what foundation models mean for remote sensing."
tags: [foundation-models, land-cover, machine-learning, google-earth-engine, indonesia]
categories: ["Environment"]
og_image: /assets/img/og/post_17_land_cover.jpg
---

Remote sensing has a feature engineering problem. For years, building good land cover models meant spending enormous effort designing spectral indices, texture metrics, and temporal features. Satellite embeddings may change that.
A few months ago, Google DeepMind released [Google Satellite Embeddings](https://medium.com/google-earth/ai-powered-pixels-introducing-googles-satellite-embedding-dataset-31744c1f4650), a large dataset designed to provide general-purpose representations of the Earth’s surface.

Just hours after the announcement, I read the white paper and started testing the data myself. I was genuinely impressed. Soon after, I attended the [Geo for Good 2025 Summit](https://earthoutreachonair.withgoogle.com/events/geoforgood25-singapore) in Singapore, where the dataset was introduced and demonstrated in person.

To be clear, the idea of building foundation models from Earth observation data is not new. Several research groups have already developed foundation models from satellite imagery to better represent Earth’s surface. Some open-source models, such as [TerraMind](https://github.com/IBM/terramind), have also been available for some time.
What makes Google’s embeddings different is not the concept itself, but the scale, consistency, accessibility, and the integration of multiple satellite sensors used to produce them.

There are already many technical explanations of how these embeddings are produced (e.g., their [white paper](https://arxiv.org/abs/2507.22291)), so I won’t repeat them here.
A simple way to think about embeddings is “PCA on steroids.” They transform raw satellite imagery into a compact representation that preserves useful information while making patterns easier for machines to learn.
Unlike PCA, these features are learned by deep neural networks and can capture complex relationships in the data, including spatial context and temporal patterns. The downside is that these representations lose their physical meaning and become harder for humans to interpret. In a sense, are we [sacrificing knowledge for power](https://bmiddleton1.substack.com/p/the-ouroboros-effect-how-ai-threatens)? 

Recently, I started working on a rather ambitious project: building an annual nationwide land use/land cover (LULC) model for Indonesia.
The idea is simple: draw a polygon anywhere in the country, choose a year, and the system automatically generates a land cover map for that area.

The model aims for detailed classification, covering major agricultural commodities such as oil palm, acacia, coffee, and rubber, along with several forest types and other land cover classes.

Before satellite embeddings were available, I built my [land cover model](https://nasirlukman.github.io/blog/2025/OBIA-LULC/) using a combination of multispectral and radar datasets, combined with additional feature engineering including spectral and textural feature extraction, followed by dimensionality reduction, image segmentation, and then supervised classification. This approach works reasonably well, but it requires a lot of effort and starts to become prohibitively expensive when the area is very large (i.e., national/regional scale).

Using Google Satellite Embeddings, I can skip most of these steps, and training and inference start to become feasible over very large areas. The model also produced maps with high overall accuracy, reasonably clean class boundaries, and consistent performance over time.

This suggests that the embeddings already capture much of the spectral, spatial, and temporal information that we normally try to engineer manually, allowing relatively simple pixel-based machine learning models to perform much better.

Below is an example of my model in action:

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_14_classification_result.webp" 
            class="img-fluid rounded" 
            alt="Google basemap, Google Satellite Embeddings false-color composite, and land use/land cover classification results for a patch of land in Borneo."
        %}
    </div>
</div>
<div class="caption">
    Figure 1. Example of the classification result on a small patch of land in Borneo (Google basemap on top, Google Satellite Embeddings false-color composite in the middle, and land use/land cover classification result at the bottom). 
</div>

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_14_accuracy_assesment.webp" 
            class="img-fluid rounded" 
            alt="Table showing the accuracy metrics (precision, recall, F1 score, and support) for each land cover class."
        %}
    </div>
</div>
<div class="caption">
    Figure 2. Accuracy metrics. The overall accuracy (OA) is 0.85.
</div>

## Looking Ahead

Satellite embeddings are only an early glimpse of a broader shift toward foundation models for Earth observation. A growing number of organizations, including research institutes, space agencies, and major technology companies, are now investing heavily in building large-scale models trained on vast archives of satellite imagery.

These models aim to learn general representations of the Earth’s surface, which can then be reused across many downstream tasks such as land cover mapping, crop monitoring, environmental monitoring, and change detection. Instead of designing task-specific features for every new project, practitioners will increasingly rely on pretrained representations and focus on building lightweight models on top of them.

As these foundation models continue to improve, incorporating more sensors, longer time series, and richer data sources, they will likely reshape how remote sensing workflows are built. Much of the traditional effort spent on feature engineering and data preprocessing may gradually shift toward model adaptation, evaluation, and domain-specific interpretation.

For the remote sensing community, this represents a significant change. Capabilities that once required large teams, specialized infrastructure, and extensive engineering may soon become accessible to smaller research groups, startups, and individual scientists.
