---
layout: post
title: From GEDI Footprints to Wall-to-Wall Canopy Height Maps
date: 2026-07-05 16:36:10
description: Comparing traditional remote sensing features and Google AlphaEarth Embeddings for canopy height modeling using GEDI.
tags: remote_sensing, lidar, gedi, canopy_height, machine_learning, foundation_models
---


# Introduction

One of the biggest challenges in forest monitoring is measuring canopy height over large areas. Airborne LiDAR provides highly accurate measurements, but acquiring LiDAR data is expensive, time-consuming, and difficult to scale over large regions.

To overcome this limitation, NASA launched the [Global Ecosystem Dynamics Investigation (GEDI)]() mission in 2018. Unlike most Earth observation missions, GEDI is not mounted on a satellite. Instead, it is attached to the [International Space Station (ISS)](https://www.eoportal.org/satellite-missions/iss-gedi#eop-quick-facts-section) (Image 1), allowing it to collect LiDAR measurements of forests around the world.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_18_GEDI_on_ISS.jpeg" 
            class="img-fluid rounded" 
            alt="GEDI instrument mounted on International Space Station"
        %}
    </div>
</div>
<div class="caption">
    Image 1. GEDI instrument mounted on International Space Station
</div>

GEDI is a full-waveform LiDAR, meaning it records the entire returned laser signal rather than just a few discrete returns. This allows it to measure the vertical structure of forests with remarkable accuracy.

The downside is that GEDI does not produce a continuous, wall-to-wall map of the Earth's surface. Instead, it collects measurements only along the ISS orbital tracks, resulting in millions of highly accurate footprints separated by large gaps.

A common solution is to use the GEDI footprints as training data and satellite imagery as predictor variables. Once the model learns the relationship between the two, it can be applied to every pixel to generate a continuous canopy height map.

In this post, I compare two different approaches:

- Traditional remote sensing features derived from Sentinel-1, Sentinel-2, and ALOS PALSAR.
- Google AlphaEarth Embeddings, which are learned representations from a satellite foundation model.

I also compare several machine learning algorithms to see which combination performs best.


# Meet GEDI

Before using GEDI as training data, it's worth taking a moment to understand how it actually works. Unlike Sentinel-2, which records reflected sunlight, or Sentinel-1, which measures microwave backscatter, GEDI actively sends laser pulses toward the Earth's surface.

When a laser pulse reaches a forest, the first reflections come from the top of the canopy. Some of the remaining energy continues downward, interacting with branches, understory vegetation, and eventually the ground. Rather than recording only a single return, GEDI records the entire returned waveform, capturing how much energy is reflected at different heights within the forest.

Image 2 shows an example of a GEDI waveform. The vertical axis represents height relative to the ground, while the horizontal axis shows the strength of the returned signal. Each peak corresponds to a large amount of reflected laser energy. In this example, the upper peak represents reflections from the forest canopy, while the lower peak corresponds to the ground return. The shaded area between these peaks contains information about the vertical distribution of vegetation, including leaves, branches, and understory.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_18_example_gedi_full_waveform_profile.png" 
            class="img-fluid rounded" 
            alt="Example of GEDI full waveform profile representing the forest structure."
        %}
    </div>
</div>
<div class="caption">
    Image 2. Example of a GEDI L1B full waveform profile capturing forest vertical structure within a ~25-meter circular ground footprint. The y-axis represents relative distance (meters) from the instrument's recording window, and the x-axis represents the return signal amplitude (ADC counts).
</div>

From this waveform, GEDI derives several structural metrics. One of the most commonly used is RH95, which represents the height at which 95% of the cumulative returned laser energy has been reached, measured relative to the ground return. Because RH95 is usually very close to the top of the canopy, it is widely used as a proxy for canopy height and serves as the target variable in this study.

The measurements are remarkably accurate, but they come with one important limitation. Since GEDI is mounted on the International Space Station, it only samples the Earth's surface along the ISS orbital tracks. Instead of producing a continuous canopy height map, GEDI provides millions of individual footprints separated by large gaps (Image 3). This is where machine learning becomes useful: by learning the relationship between GEDI measurements and satellite imagery, we can estimate canopy height for the areas between the footprints.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_18_LC.png" 
            class="img-fluid rounded" 
            alt="Example of a GEDI footprints on the study area with land cover map as basemap."
        %}
    </div>
</div>
<div class="caption">
    Image 3. Example of a GEDI footprints on the study area with land cover map as basemap.
</div>

# Models and Datasets

To estimate canopy height across the entire study area, GEDI footprints were used as the reference canopy height measurements, while satellite data served as the predictor variables. In this experiment, I compared two different input datasets.

The first uses [Google AlphaEarth Embeddings](https://deepmind.google/blog/alphaearth-foundations-helps-map-our-planet-in-unprecedented-detail/), which are learned representations generated by a foundation model trained on large amounts of satellite imagery.

The second uses a more conventional feature stack consisting of [Sentinel-1](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-1), [Sentinel-2](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-2), [ALOS PALSAR](https://www.eorc.jaxa.jp/ALOS-2/en/about/palsar2.htm), together with several commonly used spectral indices.

Before training the models, the GEDI dataset underwent several preprocessing steps. First, I filtered the data to retain only high-quality footprints, removing observations flagged as low quality or having unreliable height estimates. Since the distribution of canopy heights was uneven across different vegetation types, I then performed stratified binning based on both land cover and RH95. This ensured that the training and testing datasets contained a representative range of land cover classes and canopy heights.

Using these samples, I evaluated five regression models:

- [Linear Regression](https://en.wikipedia.org/wiki/Linear_regression)
- [Support Vector Regression (SVR)](https://en.wikipedia.org/wiki/Support_vector_machine)
- [Random Forest](https://en.wikipedia.org/wiki/Random_forest)
- [XGBoost](https://en.wikipedia.org/wiki/XGBoost)
- [Artificial Neural Network (ANN)](https://en.wikipedia.org/wiki/Multilayer_perceptron)

To ensure a fair comparison, every model used exactly the same training and testing split, generated with the same random seed. The only variables that changed between experiments were the input features and the regression model itself, allowing the performance differences to be attributed directly to those factors.

This setup provides a fair comparison between traditional remote sensing features and foundation model embeddings.


# Result
Across every machine learning model, the AlphaEarth Embeddings consistently outperformed the traditional satellite features (Table 1, Image 4).

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_18_accuracy_table.png" 
            class="img-fluid rounded" 
            alt="Table showing RMSE comparison between varous different machine learning method."
        %}
    </div>
</div>
<div class="caption">
    Table 1. Quantitative performance metrics for canopy height (RH95) validation. Models are evaluated using Spatial Cross-Validation RMSE (CV RMSE), Test RMSE, Test MAE, and Test R² across two distinct input feature sets: AlphaEarth Embeddings and a multi-sensor combination (Sentinel-1 + Sentinel-2 + ALOS PALSAR). Bold values indicate the optimal performance metrics achieved for each dataset tier.
</div>

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_18_rmse_plot.png" 
            class="img-fluid rounded" 
            alt="Scatter plots comparing observed versus predicted forest canopy height (RH95) across five machine learning architectures: Linear Regression, Support Vector Regression (SVR), Random Forest (RF), XGBoost, and Artificial Neural Networks (ANN). The top row displays performance using AlphaEarth Embeddings, while the bottom row displays performance using a conventional multi-sensor baseline (Sentinel-1 + Sentinel-2 + ALOS PALSAR). The red dashed line indicates the 1:1 line of perfect agreement, with individual test set RMSE and R² values noted in each panel."
        %}
    </div>
</div>
<div class="caption">
    Figure 4. Scatter plots comparing observed versus predicted forest canopy height (RH95) across five machine learning architectures: Linear Regression, Support Vector Regression (SVR), Random Forest (RF), XGBoost, and Artificial Neural Networks (ANN). The top row displays performance using AlphaEarth Embeddings, while the bottom row displays performance using a conventional multi-sensor baseline (Sentinel-1 + Sentinel-2 + ALOS PALSAR). The red dashed line indicates the 1:1 line of perfect agreement, with individual test set RMSE and R² values noted in each panel.   
</div>

The best result was achieved using XGBoost with AlphaEarth Embeddings, producing the lowest RMSE and the highest R² among all tested models.

Using this best-performing model, I generated a continuous canopy height map for the study area (Image 5).

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_18_tree_height.png" 
            class="img-fluid rounded" 
            alt="Resulting tree height model in the study area"
        %}
    </div>
</div>
<div class="caption">
    Figure 5. Canopy height model (CHM) of the study area. Cross-referencing this model with the land cover classification from Image 2 indicates that palm plantations exhibit the lowest canopy heights due to their relative youth, followed closely by shrublands. In contrast, the mature Acacia plantations reach heights of nearly 20 meters, while the isolated forest patch in the center exhibits the highest canopy values, topping out at approximately 20 meters.
</div>


# Discussion

One of the clearest findings from this experiment is that the choice of input features had a much larger impact than the choice of machine learning algorithm. While XGBoost achieved the best overall performance, every regression model benefited from replacing the traditional remote sensing features with AlphaEarth Embeddings. This suggests that the information contained in the input representation is more important than squeezing out marginal improvements by trying different regression algorithms.

A likely explanation is that the embeddings already encode much of the information that we usually try to engineer manually. In a traditional remote sensing workflow, we spend considerable effort selecting spectral bands, calculating vegetation indices, adding SAR backscatter, texture measures, and other handcrafted variables. Foundation models approach the problem differently. Instead of relying on manually designed features, they learn a compact representation from enormous collections of satellite imagery. Although these embeddings are not specifically trained for canopy height estimation, they appear to capture landscape characteristics that are strongly related to vegetation structure.

The strong performance of XGBoost is also not particularly surprising. Tree-based ensemble methods have long been one of the most reliable choices for tabular remote sensing data. They naturally model nonlinear relationships, require relatively little feature scaling, and are robust to redundant or correlated variables. When combined with high-quality embeddings, XGBoost seems able to extract the remaining information needed to predict canopy height.


## On the Data Leakage Question

One topic that often comes up when using AlphaEarth Embeddings for canopy height estimation is the possibility of data leakage.

The concern stems from the fact that the AlphaEarth Foundation model was pretrained using multiple Earth observation datasets, including GEDI RH metrics. If the downstream task also uses GEDI footprints as the training and validation labels, it raises an important question: is the model being evaluated on information it has already seen during pretraining?

Unfortunately, Google DeepMind does not disclose exactly which GEDI observations were used during pretraining. Because of this lack of information, it is difficult to determine whether there is any overlap between the GEDI footprints used in this study and those used to train the foundation model. As a result, I think it is more conservative to assume that some degree of overlap may exist rather than assuming there is none.

That said, this issue mainly affects canopy height models generated for years that overlap with the foundation model's pretraining period. AlphaEarth Foundations was released in 2025 and was pretrained using historical Earth observation data available before then. Once pretrained, however, the model generates embeddings for new years using only satellite imagery (e.g., Sentinel-1, Sentinel-2, and Landsat) without requiring new GEDI observations.

This means that if the embeddings are generated for imagery acquired after the pretraining period, the model has never seen the corresponding GEDI measurements because they did not yet exist during training. In those cases, the risk of leakage is substantially reduced, making post-2025 canopy height mapping a much cleaner evaluation of the foundation model's ability to generalize.

Ultimately, this question cannot be answered conclusively without more details about the foundation model's pretraining dataset.


# Closing Thoughts

GEDI has fundamentally changed our ability to map forest structure from space. By combining its accurate but sparse LiDAR measurements with wall-to-wall satellite imagery, we can now generate continuous canopy height maps at regional scales.

This experiment also reflects a broader shift in remote sensing. Instead of spending most of our effort designing handcrafted features, foundation model embeddings are beginning to provide powerful general-purpose representations that work across many downstream tasks. While questions around pretraining and data leakage still deserve careful attention, these models have the potential to simplify remote sensing workflows and push the accuracy of many applications even further.

I'm excited to see how these foundation models evolve over the next few years—and whether they eventually become the default starting point for Earth observation analysis.
