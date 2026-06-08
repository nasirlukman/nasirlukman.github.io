---
layout: post
title: "Satellites, Stats, and SEZs: Did the Mandalika MotoGP Circuit Transform Southern Lombok?"
date: 2026-06-06 16:36:10
description: Using a decade of satellite imagery, demographic data, and spatial analysis to assess how the Mandalika MotoGP Circuit reshaped economic activity, infrastructure, and local development in Southern Lombok.
tags: remote_sensing, socicoeconomic, image_analysis, night_light
---

# The Promise of Mega-Infrastructure

When governments invest in mega-infrastructure projects, they are making a bet: that strategic physical interventions can accelerate regional economic growth. By directing large amounts of capital into transportation networks, utilities, and public facilities, policymakers aim to transform underdeveloped regions into engines of investment, employment, and productivity.

In southern Lombok, this vision materialized through the development of the Mandalika tourism area and the Mandalika MotoGP Circuit. Plans to develop southern Lombok as a priority tourism destination had been under discussion since at least 2010. The effort gained momentum in 2016 with the formal establishment of the Mandalika Special Economic Zone (SEZ), an initiative designed to transform a largely agricultural and relatively isolated coastal region into an internationally recognized tourism hub.

A year later, the government announced that the SEZ would host Indonesia's first MotoGP circuit. Construction soon began, culminating in the completion of the Mandalika International Street Circuit in 2021. The track hosted its first MotoGP race in 2022, placing southern Lombok on the global motorsport stage.

With several years now having passed since the first race, an important question emerges: has the massive public investment delivered measurable regional development benefits?

This article examines that question using a decade of open geospatial and socio-economic data. By combining satellite observations, crowdsourced geographic information, and official demographic statistics, we can assess whether the Mandalika project generated detectable changes in economic activity, infrastructure growth, commercial development, and population dynamics across southern Lombok.

# Data and Proxies: Measuring Development from Space
Measuring regional development is surprisingly difficult. Traditional socio-economic indicators often suffer from two major limitations. First, official statistics are typically published with significant delays, making it difficult to assess recent changes. Second, many economic activities in developing regions occur outside formal reporting systems. Small family businesses, roadside vendors, local warungs, and informal service providers often form a substantial part of the local economy but remain largely invisible in government records.

To overcome these limitations, this analysis combines multiple open geospatial and demographic datasets spanning 2015–2025. Each dataset captures a different dimension of development, allowing us to observe economic activity, physical expansion, commercial growth, and demographic change from complementary perspectives.

The analysis is conducted across multiple spatial scales. First, we compare Pujut Subdistrict—the location of the Mandalika Special Economic Zone (SEZ)—against other subdistricts in Central Lombok Regency to assess whether development trends in Pujut differ from the broader region. Second, we examine village-level patterns within Pujut itself to identify how the impacts of the Mandalika development are distributed across local communities. This multi-scale approach allows us to evaluate both regional and localized development dynamics over the past decade.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_15_administrative.png" 
            class="img-fluid rounded" 
            alt="Subdistrict and Village level administrative map of the study area"
        %}
    </div>
</div>
<div class="caption">
    Image 1. Administrative boundaries at the subdistrict and village levels in the study area.
</div>

## VIIRS Nighttime Lights: A Proxy for Economic Activity

Nighttime light intensity has become one of the most widely used remote sensing indicators for measuring economic activity.

The data originates from the Visible Infrared Imaging Radiometer Suite (VIIRS), carried aboard the Suomi-NPP and NOAA satellite missions. Its Day/Night Band (DNB) sensor is capable of detecting extremely low levels of illumination, ranging from urban lighting networks to isolated infrastructure developments.

Raw nighttime observations are affected by clouds, moonlight, atmospheric conditions, and temporary light sources such as fires. To reduce these effects, this study uses annual VIIRS Nighttime Lights composites produced by the Earth Observation Group (EOG). These products aggregate observations throughout the year while filtering transient sources and background noise, leaving only stable human-generated illumination.

Because lighting intensity is closely linked to electrification, energy consumption, infrastructure utilization, and commercial activity, nighttime lights provide a valuable proxy for localized economic development.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_15_viirs_night_light.png" 
            class="img-fluid rounded" 
            alt="Comparison of 2015 adn 2025 VIIRS Night Light data in kecataman Pujut"
        %}
    </div>
</div>
<div class="caption">
    Image 2. VIIRS night light intensity of Pujut Subdistrict from 2015 to 2025. The red star indicates the year of the first MotoGP race at the Mandalika International Street Circuit.
</div>

## Built-Up Area Mapping: A Proxy for Physical Development

Economic growth is often accompanied by visible changes in the physical landscape. New roads, hotels, commercial facilities, and residential developments leave a measurable footprint that can be detected from space.

To monitor these changes, this study uses satellite imagery from the European Space Agency's Sentinel-1 and Sentinel-2 missions. 

Sentinel-2 provides high-resolution multispectral observations of the Earth's surface, capturing information across visible, near-infrared, and shortwave infrared wavelengths. Sentinel-1 complements these observations with Synthetic Aperture Radar (SAR) measurements, which are capable of penetrating cloud cover and are highly sensitive to the geometric characteristics of buildings and other man-made structures.

A machine learning model was trained to recognize built-up areas from the combined satellite observations, allowing the automated mapping of buildings, roads, and other developed surfaces across the study region.

Annual built-up area maps were generated for the 2015–2025 period, enabling us to track how physical development expanded over time. By comparing changes before and after the construction of the Mandalika circuit, we can observe whether major infrastructure investments were accompanied by broader patterns of land development.

While built-up area does not directly measure economic output, it provides a useful indicator of long-term capital investment and physical infrastructure growth. Sustained increases in built-up extent often reflect the construction of new facilities, transportation networks, tourism infrastructure, and supporting urban services.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_15_build_up.png" 
            class="img-fluid rounded" 
            alt="Comparison of 2015 and 2025 Build up area extent"
        %}
    </div>
</div>
<div class="caption">
    Image 3. Build up area extent of Pujut Subdistrict from 2015 to 2025. The red star indicates the year of the first MotoGP race at the Mandalika International Street Circuit.
</div>

## OpenStreetMap History: Tracking Commercial Expansion

Infrastructure alone does not create economic value. The presence of businesses and commercial services provides another important indicator of regional development.

For this purpose, the analysis utilizes historical records from OpenStreetMap (OSM), the world's largest crowdsourced geospatial database. Rather than relying on a single map snapshot, we query the OpenStreetMap History API, which preserves the complete editing history of mapped features. This allows us to reconstruct when businesses and points of interest were first added to the database and track how commercial activity evolved over time.

The analysis focuses on three categories that are particularly relevant to tourism-driven development:

- Hotels
- Restaurants and cafés
- Retail shops

Tracking the growth and spatial distribution of these establishments provides insight into how commercial activity has expanded around the Mandalika development area. Unlike traditional business registries, OpenStreetMap often captures both formal enterprises and smaller informal businesses that play an important role in local economies.

One important limitation should be noted: OpenStreetMap reflects both real-world development and mapping activity. Increases in mapped businesses may partly result from greater participation by contributors. Nevertheless, when interpreted alongside satellite observations and other independent datasets, OSM provides a valuable signal of commercial expansion and economic transformation.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_15_commercial_building.png" 
            class="img-fluid rounded" 
            alt="Comparison of 2015 and 2025 total commercial building from OpenStreetMap"
        %}
    </div>
</div>
<div class="caption">
    Image 4. Total commercial building (hotels, restaurants, cafés, and retail shops) of Pujut Subdistrict from 2015 to 2025. The red star indicates the year of the first MotoGP race at the Mandalika International Street Circuit.
</div>

## BPS Demographic Data: The Human Baseline

Satellite imagery can reveal changes in infrastructure and economic activity, but development ultimately affects people.

To capture demographic trends, this study incorporates population statistics from Badan Pusat Statistik (BPS), Indonesia's national statistical agency. These data provide official population estimates at the sub-district level throughout the study period.

Population data serves as an important baseline for interpreting observed changes. If infrastructure expansion and economic growth are occurring simultaneously with population increases, the evidence for broader regional transformation becomes stronger. Conversely, substantial physical investment without corresponding demographic change may suggest a more limited local impact.

Together, these four datasets provide complementary perspectives on development, enabling a multi-dimensional assessment of how the Mandalika project has reshaped southern Lombok over the past decade.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_15_population.png" 
            class="img-fluid rounded" 
            alt="Comparison of 2015 and 2025 total population from Indonesia Statistical Agency"
        %}
    </div>
</div>
<div class="caption">
    Image 5. Total population of Pujut Subdistrict from 2015 to 2025. The red star indicates the year of the first MotoGP race at the Mandalika International Street Circuit.
</div>

# The Macro View: Subdistrict Divergence

Our first analytical checkpoint examines development at the subdistrict level. To assess whether the Mandalika project altered the trajectory of regional growth, we isolated Pujut Subdistrict (hwere Mandalika is located) and compared it against the combined average of all other subdistricts in Central Lombok Regency.

To quantify this effect, we applied a Difference-in-Differences (DiD) regression framework using two indicators: VIIRS nighttime lights as a proxy for economic activity and built-up area as a measure of physical development.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_15_subdistrict_control.png" 
            class="img-fluid rounded" 
            alt="Comparison of Night Light and Buildup data in Pujut and other subdistrict "
        %}
    </div>
</div>
<div class="caption">
    Image 6. Ten-year comparison (2015–2025) of economic activity and physical development trends between Pujut Subdistrict and other subdistricts in Central Lombok, measured using VIIRS nighttime lights and satellite-derived built-up area estimates.

</div>

## Regression Results

_VIIRS Nighttime Lights_

- For nighttime lights, Pujut Subdistrict consistently exhibited significantly higher levels of economic activity than the average of other subdistricts in Central Lombok. The estimated difference is 3.93 units and is highly statistically significant (p < 0.001).
- The additional change in Pujut after 2021, relative to the change experienced by other subdistricts, is estimated at 0.36 units. However, this effect is not statistically significant (p = 0.361), suggesting no clear evidence of an extra post-2021 acceleration.

_Built-Up Area_

- For built-up area, Pujut also maintained significantly higher levels of physical development than the rest of Central Lombok throughout the study period. The estimated difference is 4.22 units and is highly statistically significant (p < 0.001).
- The additional increase in Pujut after 2021, relative to other subdistricts, is estimated at 0.25 units, but this effect is not statistically significant (p = 0.581), indicating no strong evidence of a distinct post-2021 boost in development.
Interpretation

At first glance, the time-series trends appear to suggest that the opening of the Mandalika circuit in 2021 triggered a sharp divergence between Pujut and the rest of Central Lombok. However, the regression results tell a more nuanced story.

The interaction term (the component that measures whether Pujut experienced an additional growth acceleration after 2021) is statistically insignificant for both nighttime lights and built-up area. In other words, the data does not provide strong evidence that the completion of the circuit itself created a distinct post-2021 jump relative to neighboring subdistricts.

By contrast, the standalone Pujut coefficient is strongly positive and highly significant across both indicators. This suggests that Pujut had already established a substantially different development trajectory long before the first MotoGP race was held.

The findings are consistent with the broader timeline of the Mandalika project. Large-scale land acquisition, road construction, supporting infrastructure development, and public investment began several years before the circuit became operational. From a regional perspective, the economic and physical transformation of Pujut appears to have been underway well before the first motorcycle entered the starting grid.

The implication is important: if Mandalika generated regional growth, much of that impact likely occurred during the development and construction phase rather than after the circuit opened to international racing events.

# The Micro View: Village-Level Dynamics

While the subdistrict-level analysis revealed that Pujut diverged from the rest of Central Lombok years before the first MotoGP race, an important question remains: how was this growth distributed across local communities?

To answer this, we moved from the subdistrict scale to the village scale. For each village, we calculated the distance between its geographic centroid and the Mandalika International Street Circuit. This allows us to examine how development changes as we move away from the project's economic core.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_15_distance_decay.png" 
            class="img-fluid rounded" 
            alt="Spatial decay coefficients showing how development indicators change with increasing distance from the Mandalika International Street Circuit"
        %}
    </div>
</div>
<div class="caption">
    Image 7. Spatial decay coefficients showing how development indicators change with increasing distance from the Mandalika International Street Circuit. Hotels and restaurants exhibit the strongest distance effects, indicating a highly localized tourism economy, while built-up area, population, retail activity, and nighttime lights display broader regional spillover patterns.


Tourism-oriented businesses display the strongest distance effect. Restaurant and café density declines by approximately 16.5% for every kilometer away from the circuit, while hotel density declines by 14.6% per kilometer. These are by far the steepest coefficients observed in the dataset.

In contrast, indicators associated with broader regional development exhibit much weaker decay rates. Built-up area declines by only 3.7% per kilometer, retail shops by 6.9%, while population and nighttime lights show relatively modest spatial gradients.

The result suggests that Mandalika operates through two distinct development channels. The first is a tourism enclave concentrated around the coastal SEZ area. High-end hospitality investments, including hotels and tourism-oriented restaurants, remain tightly clustered around the circuit and nearby beaches. The second is a broader regional spillover effect. Physical development, local commerce, and human activity extend much further inland, indicating that some benefits of the project reach communities beyond the immediate tourism zone.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_15_buildings.png" 
            class="img-fluid rounded" 
            alt="Growth of tourism accommodations and commercial shops across three distance bands from the Mandalika Circuit"
        %}
    </div>
</div>
<div class="caption">
    Image 8. Growth of tourism accommodations and commercial shops across three distance bands from the Mandalika Circuit: the Epicenter (0–5 km), Transit Corridor (5–12 km), and Rural Periphery (12+ km). Hotel development remains concentrated near the circuit, while retail activity expands more broadly into surrounding communities, suggesting stronger local economic spillovers.


Where Did Growth Actually Occur? The distance-band analysis provides a more intuitive view of these patterns. Hotel development is overwhelmingly concentrated within the 0–5 km epicenter surrounding the circuit. By 2025, this zone contains more than seventy registered accommodations, while the transit corridor and rural periphery remain largely unchanged.

Retail growth follows a different trajectory. Although the epicenter experiences the strongest expansion, commercial shops also increase within the transit corridor and, to a lesser extent, the rural periphery. This suggests that local businesses are more capable of capturing indirect economic opportunities generated by tourism-related development.

Perhaps most importantly, both figures show that the majority of growth occurred between the project's announcement in 2016 and the circuit's completion in 2021. Hotel construction, commercial expansion, and physical development accelerated rapidly during the construction phase before transitioning into a slower, more mature growth pattern after the circuit became operational.

This finding echoes the results from the previous chapter. The economic transformation associated with Mandalika appears to have been driven not only by tourism activity itself, but also by the massive wave of investment and construction that preceded the first race.

# Discussion and Synthesis

When the regional trends, village-level patterns, and temporal analyses are viewed together, a consistent picture emerges: Mandalika functions simultaneously as a localized tourism enclave and a broader regional development catalyst.

On one hand, tourism-related investments remain highly concentrated around the Special Economic Zone and the coastal corridor. Hotels and restaurants exhibit the strongest distance-decay effects in the analysis, indicating that high-end hospitality capital remains closely tied to the beach-front tourism economy.

On the other hand, the benefits of the project are not confined entirely to the coast. Physical development, commercial shops, population growth, and nighttime economic activity display much weaker spatial decay. This suggests that the infrastructure investments supporting the SEZ like roads, utilities, transportation links, and public services have influenced a much wider area than the tourism zone itself.

Perhaps the most important finding concerns timing. Across multiple indicators, the strongest period of growth occurred during the construction phase rather than after the circuit became operational. The years between 2017 and 2020 saw rapid expansion in built-up areas, commercial activity, and local economic development. By comparison, the post-2021 period is characterized by continued growth, but at a slower and more stable pace.

This suggests that a substantial portion of Mandalika's economic impact was generated not by the MotoGP events themselves, but by the large-scale investments required to build the project. Land acquisition, construction activities, supporting infrastructure, and associated economic opportunities appear to have produced the most significant development effects.

Taken together, the evidence challenges the common perception that large tourism developments are either complete successes or isolated enclaves. In Mandalika's case, both dynamics are visible at the same time. Tourism capital remains concentrated near the coast, yet the supporting infrastructure has helped connect inland communities to new commercial opportunities and physical development.

The Mandalika experience therefore highlights an important lesson for regional development policy: the long-term impact of a mega-project may depend as much on the infrastructure built around it as on the headline attraction itself.