---
layout: post
title: Sentinel-2 Bare Earth Mosaics
date: 2025-02-19 23:36:10
description: First trial to build Sentinel-2 bare earth mosaics for Indonesia in Earth Engine
tags: 
---
As a tropical country, Indonesia faces challenges in using optical remote sensing data for geological analysis due to extensive vegetation cover. According to the Indonesia Land Use/Land Cover (LULC) Map of 2019, only 1.8% of the land is classified as bare land. However, a significant portion of vegetated area (38.2%) consists of agricultural land. During land use changes, particularly in the early stages of agricultural development, land clearing exposes the bare soil. Additionally, many agricultural areas follow cultivation cycles, periodically revealing the soil beneath.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/post_6_landuse_chart.png" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    Image 1. Indonesia Land Use percetage, reclassified from Indonesia LULC Map 2019.
</div>

By leveraging dense time-series satellite images, we can generate a bare earth mosaic, which combines pixels from different acquisition times to maximize the exposure of the ground surface. [Geoscience Australia](https://www.eftf.ga.gov.au/case-study/sentinel-2-reveals-barest-earth) has created such maps for the entire continent using Landsat and Sentinel-2 images. Inspired by this, I recently experimented with a method to build a bare earth mosaic for Indonesia using Google Earth Engine.


## Approach

This approach selects only the driest, non-vegetated pixels from the time-series collection while masking out permanently vegetated, wet, and built-up areas. The process involves:

1. Cloud Masking: Cloudmasking using [s2Cloudless](https://developers.google.com/earth-engine/tutorials/community/sentinel-2-s2cloudless)

2. Pixel Filtering: Using various spectral indices for vegetation, water, and soil to exclude unwanted pixels.

2. Geometric Median Computation: Calculating the median of the remaining pixels to minimize noise and cloud contamination.

3. Final Masking: Removing residual built-up areas using LULC maps.

The resulting image is a bare earth mosaic, highlighting exposed soil and geological features. For visualization purpose, masked vegetation, water, and built-up pixels can be reintroduced.


## Comparison with Standard Cloudless Mosaics

The images below compare a standard cloudless mosaic with a bare earth mosaic derived from Sentinel-2 images. The latter effectively selects the barest pixels within agricultural areas and built-up zones.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/post_6_agriculutre.png" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    Image 2. Comparison between cloudless mosaic and bare earth mosaic in agriculural land.
</div>

This method also reveals earth surfaces in permanently forested areas, such as landslide-exposed soil and sandbars in rivers during droughts or after heavy rainfall, when sediment is deposited.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/post_6_river_and_landslide.png" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    Image 3. Comparison between cloudless mosaic and bare earth mosaic showing additional in river and landslide.
</div>


## Applications and Challenges

For further geological and soil analysis, it is best to use the masked image. For example in the image below, a simple false color-composite already show:

1. Soil composition variations in southern hills (greensih color), with some material transported north via river systems.

2. Differences between eastern (yellowish) and western plains (orange).

3. Distinct compositions within mining pits (very bright color).

This color composite highlight the potential of bare earth moscais for geological/soil analysis.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/post_6_false_color.png" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    Image 4. Cloudless composite, and bare earth composite, and false color of masked bare earth composite for analysis and interpretation.
</div>

The main challenge in generating a nationwide bare earth composite for Indonesia is scalability. My current approach exceeds Google Earth Engine’s computational limits when applied at scale. To overcome this, I need to optimize the process or split the computation into hundreds of smaller patches.

This is an ongoing experiment, and I hope to refine the method further. If you have suggestions or insights, feel free to share.

