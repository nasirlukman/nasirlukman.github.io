---
layout: post
title: Different Distance Metrics Example in Spectral Unmixing
date: 2024-11-15 21:01:00
description: 
tags: formatting images
categories: sample-posts
thumbnail: assets/img/9.jpg
---
In data space, distance typically measures similarity between data points. For instance, if points \(a\) and \(b\) are "close" to each other (i.e., have a small distance), they are considered more similar. When distance equals zero, data points \(a\) and \(b\) are exactly the same. This concept is essential in machine learning and data analysis as it quantifies similarity between datasets.

In two dimensions, it's easy to visualize data points and assess their distances, such as in this example:

**Visualization of two data points**

Visually, most of us would agree that points \(a\) and \(b\) appear closer to each other compared to \(a\) and \(c\). But is this really the case? To confirm, we need to define what we mean by "distance" and calculate the distance between each point.

In this post, we will examine three different distance metrics and compare their performance in a hypothetical spectral unmixing problem: Euclidean distance, Manhattan distance, and angular distance. The illustration of these three distance measurements is shown below.

#### Euclidean Distance

The most common and intuitive distance is Euclidean distance, also often referred to as \(L_2\) distance. Between two points \(a\) and \(b\) in data space, Euclidean distance is simply the straight-line distance between the points, which can be expressed mathematically as:

\[
d_{L_2}(a, b) = \sqrt{\sum_{i=1}^n (a_i - b_i)^2}
\]

#### Manhattan Distance

Another way to measure distance from a to b is to follow a path parallel to the axes. For example, in the image below, we first move parallel to the y-axis for 1 units, followed by a parallel path along the x-axis for 1 units, and then sum the total path length. This type of "gridded" path is called Manhattan distance (after the gridded road pattern of Manhattan) or \(L_1\) distance. Mathematically, it can be expressed as:

\[
d_{L_1}(a, b) = \sum_{i=1}^n |a_i - b_i|
\]

#### Angular Distance

For angular distance, we treat points \(a\) and \(b\) as two vectors originating from the origin \((0,0)\). The angular distance is simply the angle between the two vectors, expressed as: 

\[
\theta = \arccos \left( \frac{a \cdot b}{\|a\| \|b\|} \right)
\]

In machine learning, angular distance is more commonly referred to as cosine similarity (measured as the cosine of the angle). In spectral analysis, this is often called Spectral Angle Mapping (SAM) and is widely used for spectral matching. Mathematically, angular distance is only valid as a metric if we normalize our data to unit vectors. For unit vectors, this measurement gives the same result as Euclidean distance after normalizing the data.

### Practical Example: Linear Spectral Unmixing

To illustrate cases in which each distance metric is more appropriate, let's use linear spectral unmixing as an example. Assuming a linear mixture model, a mixed spectrum of several different objects (or "endmembers") is defined as: 

\[
y = E a + n
\]

where:
- \(y\) is the observed spectrum,
- \(E\) is the endmember matrix,
- \(a\) is the abundance vector,
- \(n\) represents noise.

In this equation, \(y\) is known from observation, and for simplicity, we assume that a matrix of possible endmembers \(E\) is also known, and noise \(n\) is negligible.
The goal is to solve for \(a\) by minimizing the difference between the modeled spectrum \(E a\) and the observed spectrum \(y\), under the conditions that all values of \(a\) are non-negative and sum to one. This may achieved by solving this optimization problem:



This is where distance metrics come in. The difference we are trying to minimize can be calculated using different distance metrics, also known as loss functions in optimization contexts. Different distance metrics can lead to different results. Now, let's run some tests under various scenarios to see how each distance metric performs.

---

or the first test, suppose we have four mineral endmembers, as shown below. We'll generate 1000 synthetic mixtures with the following conditions:

    The endmembers used are chosen randomly between 2 and 4.
    Noise is normally distributed with a mean of 0 and a standard deviation chosen randomly between 1e-5 and 1e-3.
    The mixtures follow the linear mixture model equation [linear mixture model equation].

The results of the spectral unmixing using the three distance metrics are shown below:

In this case, Euclidean distance clearly outperforms the other two metrics, as it is well-suited for data with normally distributed noise. Under these conditions, minimizing Euclidean distance is equivalent to maximum likelihood estimation.

For the second test, we use the same synthetic mixtures, but this time we add random "spikes," where each wavelength band has a 1% chance of being randomly increased or decreased by a value between 0.05 and 0.2. While this type of noise is not common in remote sensing or spectroscopy, it will help us illustrate the strengths of Manhattan distance. The results of the spectral unmixing are shown below:

Here, Manhattan distance outperforms the other metrics. Manhattan distance is known to be more robust to extreme outliers than Euclidean distance, which squares the error term, making it sensitive to outliers. In contrast, Manhattan distance only takes the absolute value of location differences, making it less affected by outliers.

While random spikes in reflectance values may not be common in spectroscopy or remote sensing, brightness differences and inaccurate endmember spectra are issues that often arise with real datasets. To illustrate this problem, let’s use two sets of endmember spectra from the USGS spectral library. We use the first set to generate synthetic mixtures and the second set to solve the unmixing problem. This experiment simulates the real-world scenario where exact endmember spectra are challenging to obtain, and the available spectra may differ in brightness from the actual spectra.

The results are shown below:

In this case, angular distance (or SAM) has the lowest error, as it essentially ignores magnitude (brightness) differences and focuses on the shape of the spectra. To illustrate further, two spectra may be considered different by Manhattan and Euclidean distances, but angular distance would see them as identical if they have the same shape, regardless of magnitude. This feature is one reason why angular distance is widely used in remote sensing applications, where brightness differences are common.

Returning to our initial visualization: Is point a closer to point b than to point c? Again, the answer depends on the distance metric. Using Euclidean and Manhattan distances, this statement holds true. However, with angular distance, it is false, as points a and c have an angular distance of 0, while a and b have a non-zero angular distance.


<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/9.jpg" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/7.jpg" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    A simple, elegant caption looks good between image rows, after each row, or doesn't have to be there at all.
</div>

Images can be made zoomable.
Simply add `data-zoomable` to `<img>` tags that you want to make zoomable.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/8.jpg" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/10.jpg" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>

The rest of the images in this post are all zoomable, arranged into different mini-galleries.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/11.jpg" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/12.jpg" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/7.jpg" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>