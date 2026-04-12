---
layout: post
title: Annual Gross Production Value of Indonesia Crude Palm Oil
date: 2026-04-11 20:36:10
description: Estimating
tags: remote_sensing, monitoring, mining, security, data_science, machine_learning, deep_learning, multispectral, radar, GIS, environment
---

## Humble Beginnings
*Elaeis guineensis*, also known locally as **Kelapa Sawit** is arguably the most successful immigrant in Indonesian history. Native to Western Africa, it first arrived in the Dutch East Indies in the mid-19th century as just four seedlings planted in the Bogor Botanical Gardens intended as a scientific specimens for the Botanical Garden Collecions.

From those four ancestors, a biological and economic empire was born. Cultivation spread from the estates of Sumatra to the vast reaches of Papua, forming a unique symbiosis with human ambition. At the entrance of my office building is a quote by the poet Robert Hass: "All lands dream of becoming a forest." It is a beautiful sentiment, but ironic when contrasted with the dream of many landowners in Indonesia: to turn their land into a palm plantation. If you drive through the lowlands of Sumatra or Kalimantan, the horizon is rarely anything else but palm oil plantations. Today, Indonesian palm oil plantations already cover millions of hectares: a footprint larger than many European nations!

## Conquering the Nation
Using my national land cover model, I estimate there are approximately 14.7 million hectares of palm oil plantations in Indonesia (Figure 1). While some official estimates lean toward 16-17 million, my model is intentionally conservative; it specifically captures mature, healthy trees across both industrial estates and smallholder plots.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_16_palm_plantation.png" 
            class="img-fluid rounded" 
            alt="Map of the extent of oil plam plantation in Indonesia for the year 2025"
        %}
    </div>
</div>
<div class="caption">
    Figure 1. Productive oil palm plantation in Indonesia for the year 2025
</div>

To put that in perspective: considering standard plantation spacing, there are more than **2 billion palm oil trees** alive in Indonesia right now. They vastly outnumber the human population. They are probably the most populous large organism in the country. Essentialy, they are the winner in the game of life.

## Estimating Annual Gross Production Value of Crude Palm Oil (CPO)
Beyond the green canopy visible from satellite imagery lies a massive economic engine. I wanted to estimate the actual Gross Production Value (GPV) of this landscape at a national level. Because we are dealing with a country as large as Indonesia, we cannot be exact. Instead, we use a Probabilistic Model. We admit what we do not know for sure, such as the specific yields or the 2026 price, and define them as ranges based on our best estimates. These are our priors. By running thousands of simulations, we account for the full spectrum of possible outcomes.

# The Bayesian Formulation

To do this, we can't consider all of palm plantation in Indonesia to be identical. We have to account for the reality that not all hectares are created equal. To simplify, we divide the palm plantations into three distinct management tiers:

    1. Independent Smallholders: The frontier farmers with the highest variability.

    2. Plasma Smallholders: Farmers supported by company partnerships.

    3. Industrial Estates: The high-efficiency, high-yield engines of the industry.

To calculate the total value, we don't just sum up the numbers; we treat every component as a random variable. The national Gross Production Value ($V$) is the sum of the production from each management tier ($i$), multiplied by the global price ($P$).Mathematically, the relationship for each tier is:

$$GPV_{i} = A \cdot s_{i} \cdot Y_{i} \cdot ER_{i} \cdot f_{i} \cdot P$$

**Where:**

* **$A$**: Total national palm oil area (hectares).
* **$s_{i}$**: The share of total area belonging to tier $i$ (Independent, Plasma, or Estate).
* **$Y_{i}$**: Average Fresh Fruit Bunch (FFB) yield (tons/ha).
* **$ER_{i}$**: Extraction Rate (the efficiency of turning fruit into CPO).
* **$f_{i}$**: A management/spatial correction factor (accounting for tree health and age).
* **$P$**: The market price of CPO (USD per ton).

By defining each of these as a probability distribution (e.g., $Y_{i} \sim \text{Normal}(\mu, \sigma)$), the model iterates through thousands of possible scenarios to find the most likely national total.

# Parameters and Assumptions

The table below outlines the specific priors used in the 2026 simulation. These values are derived from a combination of BPS (Statistics Indonesia) historical data, industry benchmarks, and 2025 market trends.

| Parameter | Management Tier | Prior Distribution / Range | Assumption Logic |
| :--- | :--- | :--- | :--- |
| **Yield ($Y$)** | Independent | $\text{Normal}(13, 4)$ | High variance due to varied seed quality. |
| | Plasma | $\text{Normal}(17, 3)$ | Improved yields through company support. |
| | Industrial | $\text{Normal}(23, 2)$ | High-input, consistent industrial management. |
| **Extraction ($ER$)** | Independent | $\text{Uniform}(0.18, 0.22)$ | Lower efficiency in smallholder milling links. |
| | Plasma | $\text{Normal}(0.23, 0.01)$ | Standardized mill processing. |
| | Industrial | $\text{Normal}(0.245, 0.01)$ | Optimized industrial-scale extraction. |
| **Adjustment ($f$)** | All Tiers | $\text{TruncatedNormal}$ | Corrects for non-productive/young trees. |
| **Price ($P$)** | Global | $\text{Lognormal}(\ln(950), 0.15)$ | Reflects CPO price volatility for 2026. |


Figure 2 below visualize the priors for our model parameters. he tight distribution for Industrial Estates reflects a highly standardized, high-input machine designed for maximum output. Conversely, the wide spread of the Independent Smallholder prior captures the reality of a frontier economy—where factors like seed quality, infrastructure access, and local management create a massive range of performance. By defining these ranges, we trying to reduce bias by acknowledging the sturctural diversity of how different plam oil plantation is utilized.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_16_prior.png" 
            class="img-fluid rounded" 
            alt="Prior distribution of the model parameter"
        %}
    </div>
</div>
<div class="caption">
    Figure 2. Prior distribution of the model parameter
</div>

When we aggregate these hectares across the entire 14.7 million hectare footprint, we get the big picture. The model estimates a National Gross Production Value for 2026 with a mean of approximately $55 Billion USD (Figure 3). However, the "truth" is a range. The 95% Confidence Interval suggests that even under conservative estimates, the value is unlikely to drop below $35 Billion, while a "perfect storm" of high yields and prices could push it toward $80 Billion. This is the economic weight of those ~2 billion trees.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_16_Annual_CPO_GPV_estimate.png" 
            class="img-fluid rounded" 
            alt="Annual CPO GPV Estimate Indonesia 2025"
        %}
    </div>
</div>
<div class="caption">
    Figure 3. Annual CPO GPV Estimate for Indonesia in 2025
</div>

Breaking the results down per hectare reveals three distinct economic profiles. As shown in Figure 4, independent smallholders generate around $2,200/ha/year, plasma $3,458, and industrial estates $5,315.

These numbers give us a baseline. Not a moral argument, not a policy stance. Just a constraint. Any alternative land use competing with palm oil has to match, or justify falling short of, this level of economic output.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_16_benchmark_per_ha_per_year_per_classification.png" 
            class="img-fluid rounded" 
            alt="GPV/ha/year/plantation type"
        %}
    </div>
</div>
<div class="caption">
    Figure 4. Benchmark GPV/ha/year/plantation type
</div>



## Closing: The Paradox of Success
A ~$55 billion system is not easy to replace. That is the uncomfortable reality.

By mapping these values, we now know exactly what we gain by sacrificing our biodiversity and optimizing a unique, complex and diverse landscape for a single species at scale.

With this baseline in hand, we can finally begin the real work: comparing this model against alternative land-use schemes to see if a more sustainable, less exploitative path can truly compete under current market mechanisms.



