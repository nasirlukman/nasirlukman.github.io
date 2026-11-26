---
layout: post
title: Testing Sentinel-2 Super Resolution Using S2DR3
date: 2025-05-09 23:36:10
description: "A quick look at the spatial and spectral integrity of the S2DR3 Sentinel-2 super-resolution model in mining, agricultural, and urban scenes."
tags: [super-resolution, sentinel-2, deep-learning]
categories: ["Other"]
---

Super-resolution generally refers to methods that increase the spatial resolution of an image using lower-resolution input. In other words, it's trying to make the pixels smaller so the image looks sharper and more detailed. I’ve always been skeptical of such approaches. Even with more conservative approaches like pan-sharpening, you often end up with spectral distortions, especially in longer wavelengths like NIR or SWIR.

When deep learning-based methods started showing up a few years ago, I was even more doubtful about the practical application of these approaches. The idea of forcing a computer to "hallucinate" an object otherwise invisible by the sensor didn’t sit well with me. Maybe it’s because I come from a spectral geology background, and I’m used to working with data where spectral integrity really matters. I prefer images to stay as unaltered as possible so they can be analyzed properly.

Lately, I saw a lot of people talking about a new super-resolution model called [S2DR3](https://medium.com/@ya_71389/sentinel-2-deep-resolution-3-0-c71a601a2253). It seems to get a good response from the remote sensing community. Probably because I recently started working on less niche applications of remote sensing, I've become more open-minded and curious about what this model can actually do, so I decided to give it a try.

The model essentially is a CNN-based deep learning model trained on artificial/synthetic high-resolution multispectral data (not entirely sure how that part was done, and it’s not fully disclosed as far as I can tell). The model takes Sentinel-2 images that have been resampled to 10 meters and produces output with 1 meter resolution. So, basically it turns each pixel into 100 new pixels per band.

I tested it in various locations across Indonesia covering scenes related to mining, agriculture, and urban areas. I wanted to run a quick test on its spatial and spectral integrity by doing visual comparisons with very high-resolution WorldView images and also sampling random points to compare spectra and compute RMSE.


## Spatial Integrity by Visual Comparison

Below are a few example scenes in various locations. The Sentinel-2 image has 10-meter spatial resolution, the S2DR3 result has 1-meter spatial resolution, and the WorldView image has 30-centimeter spatial resolution.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_11_asgm.webp" 
            class="img-fluid rounded" 
            alt="Satellite view of illegal artisanal small-scale gold mining area in Central Borneo using Sentinel-2 super-resolution model S2DR3, showing improved spatial details like mining pools and bare land patches"
        %}
    </div>
</div>
<div class="caption">
    Figure 1. Illegal artisanal small-scale gold mining area in Central Borneo
</div>

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_11_asgm_zoom.webp" 
            class="img-fluid rounded" 
            alt="Zoomed-in satellite image of illegal gold mining site in Central Borneo highlighting narrow partition between water-filled mining pits, showing S2DR3 model's capability to distinguish fine spatial features from Sentinel-2 data"
        %}
    </div>
</div>
<div class="caption">
    Figure 2. Zoomed-in version of Figure 1
</div>

Figures 1 and 2 show an illegal gold mining site in Central Borneo at different scales. Being able to detect each small pool is important, both for monitoring and for any restoration effort. Spectral information could also help differentiate pools with different physical and chemical properties. I find that in this case S2DR3 provides an excellent result that reasonably matches the very high-resolution WorldView image. In Figure 2, the red box highlights a narrow partition (less than 5 meters) between pools, which the model captures quite accurately.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_11_coal_mine.webp" 
            class="img-fluid rounded" 
            alt="Super-resolved satellite image of an active coal mine in East Borneo using S2DR3 model, enhancing visibility of haul roads and mine infrastructure compared to original Sentinel-2 image"
        %}
    </div>
</div>
<div class="caption">
    Figure 3. Active coal mine in Eastern Borneo
</div>

Figure 3 shows an active coal mine in East Borneo. The original Sentinel-2 barely shows the mining roads, but in the S2DR3 result, two main roads become clearly visible. A very useful detail, quite amazingly captured by the model.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_11_rice_field.webp" 
            class="img-fluid rounded" 
            alt="High-resolution satellite image of rice field partitions in Sembalun, Lombok generated using Sentinel-2 and S2DR3 deep learning super-resolution model, showing clear delineation of agricultural plots"
        %}
    </div>
</div>
<div class="caption">
    Figure 4. Rice fields in Sembalun, Lombok
</div>

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_11_palm_plantation.webp" 
            class="img-fluid rounded" 
            alt="Palm oil plantation in South Sumatra enhanced with S2DR3 model showing individual palm tree canopies, demonstrating the model’s effectiveness in detecting vegetation structure from Sentinel-2 data"
        %}
    </div>
</div>
<div class="caption">
    Figure 5. Palm plantation in South Sumatra
</div>

Figures 4 and 5 show examples related to agricultural fields. Figure 4 shows rice fields in Sembalun, where S2DR3 separates the individual partitions of the rice fields really well. Figure 5 shows even more impressive performance, where individual palm canopies in a palm plantation in South Sumatra are predicted with good accuracy.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_11_urban.webp" 
            class="img-fluid rounded" 
            alt="Dense urban area in Yogyakarta visualized using S2DR3 super-resolution model on Sentinel-2 imagery, revealing roads and building outlines while showing limitations in distinguishing adjacent rooftops with similar materials"
        %}
    </div>
</div>
<div class="caption">
    Figure 6. Dense built-up area in Yogyakarta
</div>

Figure 6 shows a dense urban area in the heart of Yogyakarta. This one is more challenging. If you zoom in, S2DR3 tends to merge adjacent buildings with the same roof material. However, bigger buildings, roads, and small buildings with roof materials different from their surroundings are still reconstructed with shapes close to the original condition.


## Spectral Integrity by Random Sample Comparison

To check spectral performance, I sampled points from each image and compared the original Sentinel-2 spectra with the S2DR3 result. The RMSE plots (Figure 7) show that RGB bands hold up better than the longer wavelengths. Probably has to do with how the synthetic high resolution training data was generated. Still, even in the longer wavelengths, the errors aren’t too bad. For many use cases, the results might be good enough.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_11_spectra_rmse.webp" 
            class="img-fluid rounded" 
            alt="Scatter plot showing RMSE of reflectance values across Sentinel-2 spectral bands comparing original and S2DR3 output, indicating better spectral fidelity in RGB bands and moderate errors in NIR and SWIR wavelengths"
        %}
    </div>
</div>
<div class="caption">
    Figure 7. Reflectance value comparison of each band of Sentinel-2 vs S2DR3 result.
</div>

## Final Thoughts

Honestly, I am really impressed. This feels like magic, or cheating reality. In any case, when using this model, it is important not to confuse the result with real 1-meter data. Think of it more like an *intelligent interpolation*. The model has learned spatial and spectral patterns from a massive dataset and is able to execute something like a context-aware non-linear interpolation of the input data with acceptable error. So far I haven’t seen anything that looks like an absurd hallucination out of the model, but we should stay cautious and interpret the results critically, especially if we’re using them for any decision-making.

I am quite optimistic that this is a useful model for a range of agricultural and environmental applications. Tasks like detecting small ponds, informal roads, crop plots, or even estimating canopy cover could benefit from the extra spatial detail. I wonder how far we are until we get the same model for hyperspectral images 👀.

If you're working with Sentinel-2 images, I strongly recommend checking out more [examples](https://storage.googleapis.com/0x7ff601307fa2/s2dr3menu2.html) and one of the authors’ [articles](https://medium.com/@ya_71389/sentinel-2-deep-resolution-3-0-c71a601a2253). Try the model yourself and see how it performs in your use case.

