---
layout: post
title: "Comparing Tanager-1 and EnMAP for Mineral Mapping"
date: 2026-09-04 21:36:10
description: A preliminary comparison of Tanager-1 and EnMAP hyperspectral imagery for mineral mapping, focusing on spectral similarity, spectral roughness, absorption feature depth, and subtle wavelength shifts.
tags: remote_sensing, hyperspectral, mineral_mapping, spectroscopy, tanager, enmap
---
Hyperspectral satellites are becoming increasingly available for geological and mineralogical applications. With more sensors providing imagery across the VNIR and SWIR regions, we now have more opportunities to observe the same geological targets using different instruments.

Because hyperspectral sensors differ in their spectral resolution, spectral sampling, signal-to-noise characteristics, spatial resolution, and acquisition conditions, it is interesting to examine how these differences affect the information that can be extracted from the same geological target. These differences may have limited impact when looking at broad spectral patterns, but can become important when trying to detect relatively small absorption features or subtle differences in their wavelength positions.

Recently, as part of my participation of (Tanger Open Data Competition)[https://learn.planet.com/2026-Tanager-Open-Data-Competition.html], I started working with Tanager-1 data and decided to compare it with EnMAP over the same geological target. The objective is not to perform a controlled sensor calibration or validation, but rather to explore how the two sensors represent the same mineralogical target and whether differences in their characteristics become apparent during spectral analysis and mineral mapping.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_19_tanager_enmap_sateellite.png" 
            class="img-fluid rounded" 
            alt="Image showing the ilustration of Tanager-1 and EnMap Satellite in the orbit"
        %}
    </div>
</div>
<div class="caption">
    Figure 1. Tanager-1 and EnMap Satellite
</div>

To make the comparison as reasonable as possible, I first needed to identify areas where open-access observations from both satellites overlap. I then further screened the candidate overlaps based on factors that could influence the measurements, including spatial overlap, temporal separation, solar elevation, viewing geometry, and cloud conditions. These filters cannot completely remove the effects of different acquisition conditions, but they help reduce some of the external factors that could otherwise complicate the comparison.


## Study Area Selection

The first challenge was finding suitable observations. A direct comparison between two satellite sensors is not as simple as finding two images covering the same location. Ideally, the observations should have a sufficiently large spatial overlap, relatively small temporal separation, similar illumination conditions, and similar viewing geometry.

This is particularly important for hyperspectral data because the spectrum measured by a sensor is not controlled by the material alone. Surface moisture, illumination, viewing geometry, atmospheric conditions, and small differences in the location represented by corresponding pixels can all affect the observed reflectance.

For this comparison, I prepared a function that scans the Tanager-1 and EnMAP STAC APIs to identify spatially overlapping observations and tabulates the results together with relevant acquisition metadata. The function can rapidly screen a large number of candidate observations based on their spatial and temporal relationships, while also calculating the actual overlapping area between acquisitions.

The resulting overlaps can then be filtered based on cloud cover, solar elevation, viewing geometry, and temporal separation. Finally, the candidate areas are inspected using interactive maps to identify overlaps containing interesting geological or mineralogical targets.

One of the most interesting overlaps was located near Salt Lake, Utah, USA (Figure 2). The selected area contains exposed surfaces associated with a small mining and disposal facility. These bright and relatively bare surfaces provide useful targets for hyperspectral analysis because they are less affected by vegetation than the surrounding areas and contain potentially diagnostic mineral spectral features.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_19_disposal_area.png" 
            class="img-fluid rounded" 
            alt="High Resolution Imagery of Bingham Canyon Disposal in Utah USA"
        %}
    </div>
</div>
<div class="caption">
    Figure 2. elected study area at a disposal facility north of the Bingham Canyon Mine, Utah, USA. Bingham Canyon is one of the largest and deepest open-pit mines in the world.
</div>


The selected Tanager-1 and EnMAP observations were acquired approximately 19 days apart. While the dates are not identical, the selected observations have relatively similar acquisition geometries, with a difference of about 5° in solar elevation and 3° in viewing geometry (Table 1). These criteria were used during the overlap screening to reduce differences caused by illumination and observation geometry. The remaining temporal difference may still introduce some variation in surface conditions, but the selected observations provide a reasonably comparable basis for exploring how the two sensors represent the same geological target.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_19_overlap_table.png" 
            class="img-fluid rounded" 
            alt="Metadata of the Tanager-1 and Enmap overlap"
        %}
    </div>
</div>
<div class="caption">
    Table 1. Metadata of the selected Tanger-1 and EnMap overlap.
</div>


Both datasets were processed to surface reflectance and subjected to basic quality masking, including handling of missing pixels and masking of cloud, cloud shadow, and cirrus pixels (Figure 3).

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_19_overlalp_coverage.png" 
            class="img-fluid rounded" 
            alt="Overlap between Tanager-1 and EnMAP coverage in western  part of Salt Lake City, utah, USA"
        %}
    </div>
</div>
<div class="caption">
    Figure 3. Overlap between Tanager-1 and EnMAP coverage in the selected study area. The red box indicates the disposal area selected for spectral comparison.
</div>



## COmparing the Spectra

Rather than trying to compare hundreds of bands at once, I first compared individual spectra from corresponding pixels within the overlapping area of Tanager-1 and EnMAP.

The easiest way to start comparing hyperspectral images is to look at the spectra directly. For this initial exploration, I developed a simple Python workflow in a Jupyter Notebook using ipyleaflet to interactively explore the imagery. By clicking on the map, the corresponding spectra from both sensors are extracted and plotted together. This provides a simple way to inspect the general spectral shape across the study area and identify any obvious differences between the two datasets. Figure 4 shows several example spectra sampled from the study area.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_19_spectra_sample.png" 
            class="img-fluid rounded" 
            alt="Ten selected spectra sample comapriosn between Tanager-1 and EnMap"
        %}
    </div>
</div>
<div class="caption">
    Figure 4. Ten selected sample location and its sepctra comparison.
</div>


The comparison shows that the spectra from both sensors are highly similar. Both sensors reproduce the general spectral response of the surface, and the main mineralogical features are recognizable in both datasets. In the VNIR, the absorption features around ~400, ~600, and ~900 nm are consistent with iron-oxide minerals, particularly goethite. In the SWIR, the absorption feature around ~2200 nm is associated with Al-OH minerals, with the distinctive doublet in this region being characteristic of kaolinite.

The overall albedo, or spectral brightness, was also broadly similar between the two sensors. Some differences in brightness were visible for individual pixels, which could be related to differences in solar illumination, viewing geometry, and local topography. These effects are expected when comparing observations acquired by different sensors and are difficult to completely separate from sensor-related differences

Since the disposal area appears to have relatively homogeneous surface composition, as indicated by the similar spectral shapes across the sampled pixels, I also calculated the mean spectrum for the entire area and compared the two sensors (Figure 5). This provides a more representative view of the overall spectral response while reducing some of the pixel-level variability.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_19_spectra_in_disposal_area.png" 
            class="img-fluid rounded" 
            alt="spectra of individual pixel and its average of the disposal area from Tanager-1 and EnMap"
        %}
    </div>
</div>
<div class="caption">
    Figure 5. Average and individual spectra within the selected disposal area from Tanager-1 and EnMAP imagery.
</div>


The most noticeable difference is that the Tanager-1 spectra generally appeared smoother, while the EnMAP spectra showed considerably more spectral variation, particularly around the 900–1000 nm region. To quantify this observation, I calculated spectral roughness using the variance of the first spectral derivative.

The first derivative emphasizes rapid changes between adjacent wavelengths. Therefore, its variance provides a simple measure of high-frequency spectral variation, or spectral roughness. I calculated this metric separately for different spectral regions to determine whether the difference was consistent across the spectrum. The result are shown in Table 2.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_19_spectra_in_disposal_area.png" 
            class="img-fluid rounded" 
            alt="Table of Spectra roughness in lower, middle, and upper range of the spectrum represented by variance of the first derivative as a proxy of noise
"
        %}
    </div>
</div>
<div class="caption">
    Table 2. Spectra roughness represented by variance of the first derivative as a proxy of noise
</div>


As shown in Table 2, noise levels are generally higher at shorter wavelengths. Tanager-1 consistently exhibits smoother, less noisy spectra compared to EnMAP across all spectral windows. This contrast is most significant in the VNIR range, where the spectral roughness of EnMAP is approximately an order of magnitude (10x) higher than that of Tanager-1.

Other spectral roughness, the depth of individual absorption features can also be examined quantitatively. To do this, the relevant wavelength regions were isolated, and continuum removal was applied to the spectra of pixels within the selected polygon. Continuum removal normalizes the local spectral background, allowing the position, depth, and shape of individual absorption features to be compared between Tanager-1 and EnMAP using a common baseline.

The continuum-removed spectra for the VNIR and SWIR regions from both sensors are presented in Figure 6. The distributions of the measured absorption depths are shown as histograms in Figure 7.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_19_continuum_removed_spectra.png" 
            class="img-fluid rounded" 
            alt="Continuum-removed spectra for the VNIR and SWIR regions. Each arrows shows deepest absorption feature of interest related with goethite (VNIR) and kaolinite (SWIR)"
        %}
    </div>
</div>
<div class="caption">
    Figure 6. Continuum-removed spectra for the VNIR and SWIR regions. Each arrows shows deepest absorption feature of interest related with goethite (VNIR) and kaolinite (SWIR)
</div>

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_19_feature_depth_histogram.png" 
            class="img-fluid rounded" 
            alt="Histograms displaying the distribution of absorption feature depths for goethite and kaolinite in teh study area."
        %}
    </div>
</div>
<div class="caption">
    Figure 7. Histograms displaying the distribution of absorption feature depths for goethite and kaolinite in teh study area.
</div>

Following continuum removal, the depth of the diagnostic absorption features was measured for both sensors. For the primary kaolinite feature around ~2200 nm, the absorption was generally deeper in Tanager-1. In contrast, the secondary kaolinite feature around ~2165 nm was slightly deeper in EnMAP. These differences may be related to differences in the exact band center positions and spectral bandwidths of the two sensors, which can affect how individual absorption features are sampled.

For the goethite-related absorption features, Tanager-1 also generally recorded deeper absorptions, with the exception of the broad feature around ~950 nm. This is also the wavelength region where the EnMAP spectra showed the greatest spectral variation (Figure 7). The increased spectral roughness in this region can therefore influence the continuum-removed feature depth and make the EnMAP measurement less stable. The apparent difference in feature depth around ~950 nm should consequently be interpreted with caution rather than as evidence of a stronger absorption in the EnMAP data.


## Additional Analysis: Minimum Wavelength Mapper

During the spectral data exploration in the Salt Lake, Utah study area, I observed that the deepest Al-OH absorption feature in the Tanager-1 spectra occasionally shifted between approximately 2206.2 and 2211.2 nm. Such subtle shifts in Al-OH absorption features are well documented and can provide useful information about mineral composition. Variations in the position of these features are related to changes in the chemical and structural environment of the mineral lattice, and can therefore be useful for identifying subtle compositional variations within hydrothermal alteration zones.

This shift was not readily observable in the corresponding EnMAP spectra, potentially due to differences in spectral sampling and resolution. This raised the question of whether the two sensors provide sufficient spectral information to capture and map these subtle wavelength variations. A comparison using the Minimum Wavelength Mapper (MWM) therefore provides a useful next step in the evaluation.

However, the Salt Lake study area is a mining stockpile with highly mixed and disturbed materials, making it less suitable for demonstrating subtle mineralogical wavelength variations. For this part of the analysis, I therefore shifted the study area to Cuprite, Nevada, a well-established benchmark site for hyperspectral mineral mapping.

The overlapping Cuprite scene had already been identified during the initial dataset query but was excluded by the geometric filtering because of a substantial difference in solar zenith angle between the two acquisitions. The Tanager-1 and EnMAP observations were acquired approximately six months apart, resulting in different seasonal and illumination conditions. These differences make the scene less suitable for the detailed pixel-level comparison performed at Salt Lake, but it remains useful for testing whether both sensors can capture and map subtle absorption wavelength variations.

The MWM analysis was performed using the open-source HypPy software suite rather than within the Jupyter Notebook workflow. MWM isolates a specified absorption region and uses a second-order polynomial fitted to the three deepest spectral points to estimate the minimum of the absorption feature. This allows the position of an absorption feature to be estimated at a sub-band level, rather than being restricted to the center wavelength of an individual sensor band.

I applied MWM to the 2150–2220 nm range to investigate subtle variations in the Al-OH absorption feature and to the 800–1000 nm range to examine variations in the Fe-related absorption feature. The resulting wavelength maps from Tanager-1 and EnMAP are presented in Figure 8.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_19_minnimum_wavelength_mapper.png" 
            class="img-fluid rounded" 
            alt="Minimum Wavelength Mapper results for the Cuprite study area across the 800–1000 nm and 2150–222 nm wavelength ranges, comparing EnMAP (left) and Tanager-1 (right)"
        %}
    </div>
</div>
<div class="caption">
    Figure 8. Minimum Wavelength Mapper results for the Cuprite study area across the 800–1000 nm and 2150–222 nm wavelength ranges, comparing EnMAP (left) and Tanager-1 (right).
</div>


In the SWIR, Tanager-1 demonstrates a higher sensitivity to subtle sub-band shifts within the Al-OH absorption feature. The Tanager-1 imagery shows a broad spatial gradient in the mapped wavelengths, ranging from approximately 2160 nm (cyan) to over 2210 nm (magenta). In contrast, the EnMAP result is considerably flatter, dominated by patches around ~2200 nm (orange) and ~2170 nm (green), with less clearly defined spatial variation.

The contrast between the two sensors is even more pronounced in the VNIR (800–1000 nm). The EnMAP result does not show a coherent spatial pattern and is instead highly speckled, which is likely related to the strong spectral noise observed in this wavelength region. In contrast, Tanager-1 resolves a distinct spatial pattern, with shorter absorption wavelengths in the northeast (yellow, ~925 nm) transitioning toward longer wavelengths in the southeast (red, ~950 nm). Although the pattern appears relatively subdued, this is expected given the shallow and broad nature of the iron-oxide absorption feature.

The observed wavelength variation may reflect changes in the iron-oxide mineral assemblage, potentially indicating a transition between goethite- and hematite-dominated materials. However, this interpretation should be treated as indicative rather than definitive, as wavelength position alone is insufficient to distinguish these minerals reliably. A more detailed mineralogical interpretation would require comparison with reference spectra and, ideally, field or laboratory measurements.

Overall, these results suggest that Tanager-1 is better able to resolve subtle absorption-wavelength variations in this dataset. Its finer spectral sampling and comparatively lower spectral roughness appear to provide greater sensitivity to sub-band shifts, particularly in the VNIR where the EnMAP data are strongly affected by spectral noise. This demonstrates a potential advantage of Tanager-1 for mineral mapping applications where subtle variations in absorption position are important.

## Remarks

Overall, both Tanager-1 and EnMAP captured the main spectral and mineralogical characteristics of the study area and demonstrated their capability for detailed mineral mapping. Tanager-1 showed an advantage in its smoother spectra and apparent ability to resolve finer spectral variations and subtle absorption-wavelength shifts. However, this does not indicate that Tanager-1 is generally superior to EnMAP. The differences observed here may also reflect the specific acquisition conditions and sensor characteristics. Further comparisons across different sites, datasets, and field measurements are needed to assess how consistent these results are and to validate their mineralogical significance.