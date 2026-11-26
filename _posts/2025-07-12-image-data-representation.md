---
layout: post
title: "From Arrays to Graphs: Different Ways to Represent Image Data in Remote Sensing"
date: 2025-07-12 23:36:10
description: "A practical overview of image data structures in remote sensing (data cubes, flattened matrices, feature-space vectors, and graphs) and what each enables."
tags: [machine-learning, deep-learning, object-based-classification, image-analysis]
categories: ["Other"]
og_image: /assets/img/og/post_13_datacube.jpg
---


# Introduction

In the geospatial and remote sensing world, image files are typically referred to as raster files. These files store images in pixels, where each pixel is located at a specific row and column position and stores a single value representing intensity or reflectance. This structure resembles a 2D matrix or array. If each pixel is associated with multiple values (like in multispectral or hyperspectral data), they are stored across different bands, which are essentially multiple aligned layers, each representing one variable.

These raster files are always accompanied by metadata, which includes the coordinate system, pixel resolution, and the coordinates of a reference point in the image (typically the top-left corner). With this information, we can geolocate each pixel. Raster data is typically stored in .tif files, and when geospatial metadata is included, the file is referred to as a GeoTIFF. This format is widely supported and convenient for storing remote sensing data.

More modern formats like [Cloud Optimized GeoTIFFs (COGs)](https://cogeo.org/) allow for efficient workflows in cloud-based environments, which is crucial considering the rapidly increasing volume of satellite imagery. Still, at their core, these files follow the same basic structure: an array of pixel values.

As users of the data, we have the freedom to represent and structure it in different ways, depending on the needs of our analysis. Alternative representations can open up new ways of thinking about image analysis and allow us to apply analytical methods that may not work well with standard raster formats. In this post, we’ll discuss different ways to think about and structure our image data, and how these representations support different types of analysis.

For this example, we’ll use a small image patch with three bands to simplify the visualizations. We downsample this small patch of forest and grassland into a 5×5 pixel image, so the total shape is 5×5×3.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_13_resample.webp" 
            class="img-fluid rounded" 
            alt="Satellite imagery from Planet showing a patch of forest and grassland, downsampled to 5x5 pixels for simplicity in the data representation example."
        %}
    </div>
</div>
<div class="caption">
    Figure 1. The example image. For simplicity, we resample this image to 5 by 5 pixels and only use the RGB bands, resulting in an array with a shape of 5x5x3. 
</div>


# 1. Data Cube
The most natural way to represent multiband image data is probably as an array. Our previous image can be visualized as a 5×5×1 array like this:

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_13_composite.webp" 
            class="img-fluid rounded" 
            alt="RGB composite image visualized as 5x5x1 voxels."
        %}
    </div>
</div>
<div class="caption">
    Figure 2. The same image visualized as 5x5x1 voxels, where the three RGB bands are reduced into one color composite band.
</div>

In this case, the displayed pixel values, which are shown as colors, are not the original data but a composite of the RGB bands. Behind the scenes, the raw data is a stack of three 5×5 grids, where each layer represents the intensity of red, green, and blue light respectively. Since human eyes perceive light in these wavelengths, we see a combination of them as color. This RGB composite is helpful for visualization, as it compresses information in a way we can easily interpret. However, this compression also leads to some information loss. That’s why, for image analysis, we usually work with the raw, uncompressed form.

In raw form, the image is a 5×5×3 array. For the computer, this is just a structured sequence of numbers. But it helps us to imagine it as a cube, where the horizontal plane represents the x and y coordinates, and the vertical axis represents the intensity in each spectral band (in this case, red, green, and blue).

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_13_datacube.webp" 
            class="img-fluid rounded" 
            alt="5x5x3 voxel representation of the raw image array, often referred to as a data cube. Each band, representing the intensity of red, green, and blue light respectively, is stacked together."
        %}
    </div>
</div>
<div class="caption">
    Figure 3. The same image visualized as 5x5x3 voxels of the raw data. This is often referred to as a data cube.
</div>

This 3D structure is often referred to as a tensor. Representing data in this way is useful if we want to apply linear algebra or use models that rely on spatial and spectral structure. For example, in deep learning, [convolutional neural networks (CNNs)](https://en.wikipedia.org/wiki/Convolutional_neural_network) apply a series of convolution operations (visualized as yellow-lined voxels in Figure 4) to extract spatial and spectral features from the image. These filters slide over the image with the goal of capturing shapes, textures, and color combinations that define particular classes or objects.

This approach is very powerful and currently forms the state of the art in image analysis. However, it comes with limitations, especially the need for large labeled datasets and substantial computational power.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_13_convolution_anim.webp"
            animated=true
            class="img-fluid rounded" 
            alt="Simplified animation of how a convolutional layer in a CNN works."
        %}
    </div>
</div>
<div class="caption">
    Figure 4. Animated example of how a convolutional layer moves through the image to capture complex spatial and spectral patterns.
</div>


# 2. Spatially Flattened Matrix

Some machine learning algorithms like [SVM](https://scikit-learn.org/stable/modules/svm.html), [Random Forest](https://scikit-learn.org/stable/modules/ensemble.html#forest), and [XGBoost](https://xgboost.readthedocs.io/en/stable/tutorials/model.html) do not take spatial patterns into account. They treat each pixel independently and classify them based only on their spectral signatures.

If we’re using such methods, or any approach that works on a pixel-by-pixel basis, then maintaining the spatial relationship between pixels is unnecessary. Instead, we can restructure the image as a 2D array, where each column represents an individual pixel, and each row represents a spectral band.

The computer will interpret this as just another structured collection of numbers, though with a simpler 2D format.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_13_pixelwise_classification_anim.gif" 
            class="img-fluid rounded" 
            alt="Simplified animation of how a typical pixel-by-pixel classifier such as Random Forest, SVM, or XGBoost moves from one pixel to the next, treating each pixel as an individual vector in feature space."
        %}
    </div>
</div>
<div class="caption">
    Figure 5. Animated example of how a typical machine learning classifier moves from one pixel to another in the spatially flattened matrix, treating each pixel as a vector.
</div>

This representation allows the classifier to treat each column as a feature vector, and move from one pixel to another without worrying about their positions. It’s efficient and works well when spatial context isn't critical.


# 3. Collection of Vectors in Feature Space

In the previous example, we already treated each pixel as a vector, but we still thought of it mainly as numerical data. In this section, we look at how visualizing each pixel as a geometric object can be useful.

Using the same image, we now represent each pixel as a vector from the origin in RGB space.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_13_vectors.webp" 
            class="img-fluid rounded" 
            alt="Image pixels represented as vectors in feature space. This representation is useful for geometric analysis of the data, which is the basis of the Spectral Angle Mapper (SAM), K-means clustering, and Principal Component Analysis (PCA)."
        %}
    </div>
</div>
<div class="caption">
    Figure 6. In this representation, each pixel is visualized as a vector from the origin (0,0,0) to its data coordinate in RGB feature space.
</div>

This allows us to evaluate similarity between pixels based on the angle between vectors, also known as angular distance (I’ve discussed this in more detail [here](https://nasirlukman.github.io/blog/2024/distance/)). Pixels with the same color but different brightness will have the same direction (0° angular distance), and only differ in magnitude. This is particularly useful in remote sensing, where terrain and illumination changes can cause variations in brightness. Using the [Spectral Angle Mapper (SAM)](https://step.esa.int/main/wp-content/help/versions/9.0.0/snap-toolboxes/org.esa.s2tbx.s2tbx.spectral.angle.mapper.ui/sam/SAMProcessor.html) method, these brightness differences can be ignored.

This geometric interpretation of pixel vectors is also useful for other analytical methods like [K-means clustering](https://en.wikipedia.org/wiki/K-means_clustering) and [Principal Component Analysis (PCA)](https://pro.arcgis.com/en/pro-app/3.3/tool-reference/spatial-analyst/how-principal-components-works.htm), both of which are based on geometric analysis of pixels in feature space.


# 4. Graphs
Another way to represent an image is as a graph. A graph consists of nodes and edges. Each node represents a pixel and stores its spectral information. Edges represent connections between pixels, and each edge has a weight that reflects the similarity between the connected pixels.

We have flexibility in how we define these graphs. In this example, I use the pixel’s spatial coordinates for node positions. Each node connects to its 8 neighbors (horizontal, vertical, and diagonal), and the edge weight is calculated based on both spatial distance and spectral similarity (i.e., pixels that are closer to each other and have similar colors/spectra have the lowest weight).

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_13_spatial_graph.webp" 
            class="img-fluid rounded" 
            alt="Image represented as a graph in spatial space. Each node is located at the pixel's geographic coordinates and contains all of its spectral information, and each edge is weighted by spatial closeness and spectral similarity."
        %}
    </div>
</div>
<div class="caption">
    Figure 7. Graph representation of the image in spatial space.
</div>

Even with this simple setup, we can already capture the spatial and spectral structure of the image. For example, superpixel clustering can be done by cutting edges based on weight thresholds. More complex methods like graph-based deep learning also become possible with this structure.

In remote sensing, Object-Based Image Analysis (OBIA) is often used for tasks like land cover classification. OBIA captures both spatial and spectral patterns and is widely used because it’s less demanding than deep learning but still effective. Typically, clustering algorithms like [SNIC](https://developers.google.com/earth-engine/apidocs/ee-algorithms-image-segmentation-snic) are used first, followed by supervised classification methods like Random Forest or SVM applied to each cluster.

I think OBIA could be more naturally implemented using a graph-based approach, where clustering and classification happen simultaneously in a unified framework. However, I haven’t explored this idea in depth myself.

We can also define the graph purely in feature space, where nodes are pixels and edge weights are the Euclidean distance between spectral vectors. This structure makes it easy to apply unsupervised classification methods that group pixels based on spectral similarity, much like K-means.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_13_spectral_graph.webp" 
            class="img-fluid rounded" 
            alt="Image represented as a graph in feature space. Each node is located in feature space according to its feature values, and each edge is weighted by Euclidean distance."
        %}
    </div>
</div>
<div class="caption">
    Figure 8. Graph representation of the image in feature space.
</div>


# Takeaways

The way we represent image data can influence how we think about and analyze it. Whether we treat the image as a cube, a flat table, a set of vectors, or a graph, each perspective opens different possibilities and supports different types of methods. In practice, we often move between these representations depending on the task. Some problems require spatial context, some don’t, and some benefit from looking at geometry in feature space.

In this post, I simplified the image to just a few pixels and three bands so we can still visualize and reason about it in 3D space. In real-world remote sensing, however, we often work with millions of pixels and possibly hundreds of spectral bands, making direct visualization impossible. That’s why it’s helpful to build an intuitive understanding using simple 3D examples first. Once we grasp the core ideas in a space we can see, it becomes much easier to generalize those concepts mathematically to higher-dimensional data where we rely entirely on abstract reasoning and computation.

Personally, I find that understanding the data representation used in each analytical method helps us think more clearly about how the method works, and also gives us the ability to adjust our analysis according to our needs. Instead of just following a fixed workflow, we can be more intentional in how we prepare and structure our data. This flexibility becomes especially important as we deal with more complex remote sensing problems, where no single representation fits all use cases.