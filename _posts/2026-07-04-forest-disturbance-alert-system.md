---
layout: post
title: "Operational Near Real Time Forest Disturbance Alert System using Radar Satelite"
date: 2026-07-04 16:36:10
description: Building a lightweeight regional radar-based early warning system by combining Bayesian change detection with deforestation risk maps and dynamic land cover information.
tags: radar, deforestation, forest_disturbance
---

# Introduction
Forest disturbance is one of the earliest indicators of deforestation and forest degradation. Detecting these changes quickly is important for conservation, carbon projects, law enforcement, and sustainable land management. The sooner a disturbance is detected, the sooner field verification and mitigation actions can be taken.

In practice, the terms forest disturbance alerts and deforestation alerts are often used interchangeably. Here, however, I make a subtle distinction between the two. 

A deforestation alert system focuses on detecting abrupt and substantial changes in forest cover that are highly indicative of land-clearing activities. These systems are generally designed to identify events that are very likely to represent permanent forest loss.

A forest disturbance alert system, on the other hand, also aims to detect more subtle changes in forest structure. These disturbances may result from selective logging, small-scale clearing, small road deevelopmenet, early stages of deforestation, etc. Because the goal is to detect changes as early as possible, disturbance monitoring typically requires higher detection sensitivity. The trade-off is that it is also more susceptible to noise and false positives, making careful filtering and validation essential.

Optical satellites such as [Sentinel-2](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-2) and [LANDSAT](https://science.nasa.gov/mission/landsat/) have become the standard for forest monitoring, but they suffer from one major limitation in tropical regions: cloud cover. Radar satellites, particularly [Sentinel-1](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-1), overcome this problem by providing observations regardless of weather or daylight, making them ideal for operational near real-time monitoring.


## Why build another alert system?

Several excellent [global deforestation alert](https://data.globalforestwatch.org/datasets/gfw::integrated-deforestation-alerts/about) products already exist. One of the most notable is the Radar for Detecting Deforestation [(RADD)](https://www.wur.nl/en/research/products-services/radd-forest-disturbance-alert) alert system, which provides global near real-time disturbance alerts based on Sentinel-1 data. So why develop another system?

Global products are designed to work reasonably well everywhere. Local systems, however, can be optimized for a specific region and integrated with local datasets that are unavailable to global products. This allows:

- tuning detection thresholds for local forest conditions,
- integrating locally developed land cover maps,
- masking known non-forest areas more accurately,
- incorporating local deforestation risk information, and
- adapting the balance between sensitivity and false alarms.

The goal is not to replace global alerts, but to build a system that is better suited for operational monitoring within a specific landscape.


# My previous approach

I previously developed a [Sentinel-1 forest disturbance monitoring workflow](https://nasirlukman.github.io/blog/2025/sentinel1-change-detection/) based on long radar time series.

That approach relied on extensive preprocessing for every satellite overpass, including speckle reduction and corrections for seasonal variation before detecting anomalies.

Although the method produced reliable results, it had two important limitations:

- it was computationally expensive, making large-scale operational deployment difficult, and
- the heavy temporal smoothing reduced sensitivity to small or early disturbances.

This motivated me to explore a lighter and more operational approach.


# Current methodology

The current system follows the general framework of the [RADD algorithm](https://iopscience.iop.org/article/10.1088/1748-9326/abd0a8). Instead of modeling the entire radar time series, it uses a [Bayesian](https://en.wikipedia.org/wiki/Bayesian_inference) approach that updates the probability of forest disturbance as new Sentinel-1 observations become available. This greatly reduces computational cost while remaining suitable for continuous monitoring over large areas.

Since my focus is regional rather than global monitoring, I introduced several modifications.

## 1. Harmonic baseline to capture wet and dry seeason condition

A two-year rolling baseline is used to model the expected radar backscatter for each pixel. For every new observation, a harmonic function is fitted to the previous two years of Sentinel-1 data to capture the seasonal variation associated with wet and dry conditions (Image 1).

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_17_harmonic_baseline.png" 
            class="img-fluid rounded" 
            alt="A graph showing 2 years data of Sentinel-1 VH backscattere and a harmonic line that fitt the data"
        %}
    </div>
</div>
<div class="caption">
    Image 1. Fitted harmonic baselinee for a single foreste pixel as an example
</div>

By explicitly modeling these seasonal fluctuations, the system can distinguish normal environmental variability from genuine forest disturbance. This reduces false alerts that would otherwise occur during transitions between the wet and dry seasons, when changes in soil and vegetation moisture naturally affect radar backscatter.

## 2. Spatial prior based on deforestation risk

Rather than using a static prior probability, the Bayesian model uses a spatially varying prior derived from a deforestation risk map that I developed previously.

The risk model incorporates factors such as:

- distance to roads
- distance to rivers and waterways
- distance to forest edges
- historical deforestation

Areas with higher baseline risk therefore require less evidence before being flagged as potential disturbances, while remote intact forests require stronger evidence.

## 3. Dynamic land cover masking

The alert system is also integrated with [annual national land cover model](https://nasirlukman.github.io/blog/2025/satellite-embeddings/) {Image 2}.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_17_land_cover.png" 
            class="img-fluid rounded" 
            alt="Snippet of national land cover model showing various land cover class in Kalimantan/Borneo"
        %}
    </div>
</div>
<div class="caption">
    Image 2. Snippet of land cover map integrated with the alert system. This land cover map is automatically updatd every year to make sure that thee system always use the latest land cover data.
</div>

Instead of relying on a fixed forest mask, the system uses an updated land cover map each year, allowing it to adapt to changing landscapes while reducing alerts over non-forest areas.

## 4. Class-specific parameter tuning

Different land cover classes exhibit different radar variability.

Rather than applying a single detection threshold everywhere, I use land-cover-specific parameters to adjust:

- expected radar noise
- detection sensitivity
- alert confidence thresholds

This makes the system more sensitive where genuine disturbances are expected while reducing false positives in naturally noisy environments.


# Result

The result example are presented in Image 3 below. The new framework is substantially lighter computationally than my previous implementation while improving sensitivity to small forest disturbances. Integrating spatial risk information and dynamic land cover masks also reduces false alarms compared with a uniform detection strategy.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_17_12_days_alert.gif" 
            class="img-fluid rounded" 
            alt="Animation of the forest disturbance alert from 2023 to 2025 showing the eexpansion of palm oil plantation to the surrounding forests"
        %}
    </div>
</div>
<div class="caption">
    Image 3. Animation of the forest disturbance alert from 2023 to 2025 showing the rapid expansion of palm oil plantation to the surrounding forests since latee 2023 to end of 2025.
</div>

The alerts were visually validated using Planet Monthly Basemaps and show good agreement with observed forest disturbances, suggesting that the system is capable of producing timely and reliable alerts.

Without additional post-processing, the resulting alert map does not produce perfectly clean deforestation patches. However, this is by not a failure in the system. The objective of the system is not to generate accurate deforestation polygons or estimate deforested area. Instead, it is intended to provide early, reliable alerts that can trigger further investigation or field verification. Delineating the final extent of disturbance can be handled in a separate mapping workflow.


# Future outlook

The current system is limited by the revisit frequency of a single Sentinel-1 orbit, resulting in updates approximately every 12 days. While this is sufficient for many monitoring applications, there is significant potential to reduce the time between observations.

One promising direction is to integrate additional radar missions such as NISAR and Biomass, both expected to become operational around late 2026 or early 2027. Combining observations from multiple SAR satellites would substantially increase observation frequency while preserving the all-weather capability of radar monitoring.

Another opportunity is to fuse radar-based alerts with optical observations from Sentinel-2 and Landsat. Although optical imagery is frequently affected by cloud cover in tropical regions, it provides complementary information whenever cloud-free observations are available. Combining evidence from both radar and optical sensors could improve both detection confidence and temporal coverage.

If these satellite constellations are successfully integrated, it may become possible to receive new observations almost every day in many regions, enabling much faster detection and verification of forest disturbances.

Global forest alert systems have transformed the way we monitor forests. However, there is still considerable value in developing regional systems that can leverage local datasets, local knowledge, and application-specific tuning.

For organizations managing protected areas, carbon projects, or concession monitoring, these local adaptations can produce alerts that are both more sensitive and more operationally useful than a one-size-fits-all global solution..