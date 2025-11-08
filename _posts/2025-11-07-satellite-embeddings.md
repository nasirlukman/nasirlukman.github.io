---
layout: post
title: "Satellite Embeddings and Large Scale Model"
date: 2025-11-07 23:36:10
description: Brief note on my experience in upscaling my model using Google Satelite Embedings
tags: remote_sensing, machine_learning, image_analysis
---

A few months ago, the remote sensing world was shaken by one of Google DeepMind’s most ambitious Earth observation projects: the official release of [Google Satellite Embeddings](https://medium.com/google-earth/ai-powered-pixels-introducing-googles-satellite-embedding-dataset-31744c1f4650).
Just hours after the announcement, I dove into the white paper and tested the data myself, and I was genuinely blown away. I was also lucky enough to get a seat in the [Geo for Good 2025 Summit](https://earthoutreachonair.withgoogle.com/events/geoforgood25-singapore) in Singapore, where they introduced the dataset and showcased its capabilities in person.

To be fair, the concept of embeddings isn’t new. Even in remote sensing, several research groups have developed their own embeddings from satellite data to better represent Earth’s surface.
But what makes Google’s version stand out is its sheer scale and global coverage. It’s the first dataset (to my knowledge) that captures such a broad and consistent representation of the planet at once.

There are already plenty of great technical explanations about how satellite embeddings are produced (their [white paper](https://arxiv.org/abs/2507.22291) is the main source of good information, of course), so I won’t repeat them here.
To put it simply: I like to think of embeddings as “PCA on steroids.” They transform data into a new (usually lower-dimensional) space that preserves essential information while making it easier for machines to process. The tradeoff is that each dimension becomes more abstract. It is harder for us mortals to interpret, but far more powerful for computers to use. By the way, why does it sounds like we are (sacrificing knowledge for power)[https://bmiddleton1.substack.com/p/the-ouroboros-effect-how-ai-threatens]? 

Anway, recently I’ve been working on a rather ambitious project which involves in building an annual, nationwide land use/land cover (LULC) model for Indonesia.
The idea is simple: users can draw a boundary anywhere in Indonesia, and the system will automatically generate a land cover map for that area, historically (from 2017) up to the latest available year. Ready for further analysis.

I aim for detailed classification, covering major agricultural commodities such as palm oil, acacia, coffee, and rubber, along with different forest types and other distinctive land covers.

Before embeddings were available, I had built several LULC models (like the one I wrote about [here](https://nasirlukman.github.io/blog/2025/OBIA-LULC/)) but they were mostly localized due to resource constraints constraints.

Now, with satellite embeddings, and of course along with other advances like open labeled datasets, multi-sensor imagery, and Google Earth Engine, building large-scale models has become much more achievable for small organizations or individual researchers like myself.
Embeddings remove most of the heavy feature engineering and feature selection work, while also encoding spatial context (neighborhood relationships) and temporal patterns that capture vegetation phenology. These make simpler pixel based machine learning methdod on top of it become so much better and more powerful.

Below is an example of my model in action, along with its accuracy metrics:

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_14_classification_result.png" 
            class="img-fluid rounded" 
            alt="Sentinel 2 Annual Cloudless Composite, Google satellite embeddings, and land use land cover classification results"
        %}
    </div>
</div>
<div class="caption">
    Image 1. Example of classification result on a small patch of land in Borneo. (Sentinel 2 annual cloudless mosaic on top, Google Satelite embedings false color composite in the middle, and land use/land cover classification result at the bottom). 
</div>

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_14_classification_result.png" 
            class="img-fluid rounded" 
            alt="Tabel showing the accuracy metrics (preccision, recall, f1 score, and support for each class. the model have 0 )"
        %}
    </div>
</div>
<div class="caption">
    Image 2. Accuracy metric. The Overall Accuracy (OA) is 0.88. Not bad for a large scale model 😉.
</div>

## Looking Ahead

What’s next for Earth observation?
I believe this is only the beginning. Soon, we’ll likely see open embeddings with shorter temporal spans (maybe  monthly?) and even embeddings incorporating richer data input such as hyperspectral data for example.

As a remote sensing scientist, this kind of progress excites me. It feels like we’re entering a new era where powerful global datasets allow small teams or even individuals to tackle problems that once required huge resources.
