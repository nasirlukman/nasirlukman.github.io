---
layout: post
title: Bayesian Spectral Unmixing
date: 2024-11-24 12:36:10
description: Bayesian approach on spectral unmixing with an example case using hyperspectral images of sandstone drill core sample.
---

In the [previous post](https://nasirlukman.github.io/blog/2024/distance/) we discussed how spectral unmixing inherently suffers from uncertainty—stemming both from the data and the model. Traditional optimization approaches, like the one we used earlier, often assume that these uncertainties are either negligible or nonexistent. However, in practice, this is rarely the case.

In this post, we'll take a brief look at the Bayesian approach to spectral unmixing, which explicitly accounts for these uncertainties. By incorporating them into the model, we propagate the uncertainty through to the final results. Instead of a single vector of mineral abundances, the Bayesian approach provides a probability distribution for these abundances, offering deeper insight into the confidence we have in our estimates.

While we won’t dive too deeply into the math, a basic formulation helps set the stage. The linear mixture model can be expressed as:

$$ \mathbf{y} = \mathbf{E} \mathbf{a} + \mathbf{e} $$

where:
- $$ \mathbf{y} $$ is the observed spectrum,
- $$ \mathbf{E} $$ is the endmembers matrix,
- $$ \mathbf{a} $$ is the abundance vector,
- $$ \mathbf{e} $$ represents error terms/uncertainty.

> Context for this post: We are focusing on unmixing for minerals on particulate surfaces (e.g., rock surfaces). Due to multiple-scattering effects, the linear relationship above does not hold when using reflectance data. Instead, we will use the [Single Scattering Albedo (SSA)](https://en.wikipedia.org/wiki/Single-scattering_albedo) which derived from Hapke's Model, as it better handles these effect. For those interested in the underlying theory, I highly recommend consulting [this book](https://www.cambridge.org/core/books/theory-of-reflectance-and-emittance-spectroscopy/C266E1164D5E14DA18141F03D0E0EAB0); these two papers that really helps me a lot with the subject: [[1]](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/JB094iB10p13619), [[2]](https://www.researchgate.net/publication/264564339_A_Review_of_Nonlinear_Hyperspectral_Unmixing_Methods); or other sources (including my [thesis](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=http://essay.utwente.nl/101556/1/Lukman_MA_ITC.pdf&ved=2ahUKEwjqlY-m8faJAxUdw6ACHRUJKj0QFnoECBkQAQ&usg=AOvVaw3Tbo1LEGrTchQ7edNZoxGt)😉)


### bayesian Framework

Following [Bayes' Theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem), we can represent the spectral unmixing problem as:

$$
P(\mathbf{a}, \sigma^2 \mid \mathbf{y}, \mathbf{E}) \propto P(\mathbf{y} \mid \mathbf{a}, \sigma^2, \mathbf{E}) P(\mathbf{a}) P(\sigma^2)
$$

where:
- $$ P(\mathbf{a}, \sigma^2 \mid \mathbf{y}, \mathbf{E}) $$ is the posterior distribution of the abundance vector and error variance given the observed spectrum and endmembers,
- $$ P(\mathbf{y} \mid \mathbf{a}, \sigma^2, \mathbf{E}) $$ is the likelihood of the observed spectrum,
- $$ P(\mathbf{a}) $$ is the prior distribution of the abundance vector,
- $$ P(\sigma^2) $$ is the prior distribution of the error variance,
- and $$ \propto $$ denote proportionality

We assume that the error term $$ \mathbf{e} $$ is normally distributed, giving us a [Normal](https://distribution-explorer.github.io/continuous/normal.html) likelihood:

$$
P(\mathbf{y} \mid \mathbf{a}, \sigma^2, \mathbf{E}) = \mathcal{N}(\mathbf{y} \mid \mathbf{E}\mathbf{a}, \sigma^2\mathbf{I}),
$$

where $$ \mathbf{I} $$ is the identity matrix. 

For the abundance vector $$ \mathbf{a} $$, we use a [Dirichlet](https://distribution-explorer.github.io/multivariate_continuous/dirichlet.html) prior to enforce the non-negativity and sum-to-one constraints:

$$
P(\mathbf{a}) = \mathcal{D}(\mathbf{a} \mid \boldsymbol{\alpha}),
$$

where $$ \boldsymbol{\alpha} $$ is the concentration parameter. 

For the error variance $$ \sigma^2 $$, we assign a [Half-Cauchy](https://distribution-explorer.github.io/continuous/halfcauchy.html) prior:

$$
P(\sigma^2) = \mathcal{HC}(\sigma^2 \mid \beta),
$$

with the scale hyperparamter $$ \beta $$ given a [Unifrom](https://distribution-explorer.github.io/continuous/uniform.html) prior such as:

$$
P(\beta) = \mathcal{U}(\beta \mid 0, 0^{-4}).
$$

Terefore, we can summarize the hierarchical structure of the random variables as:

$$ \mathbf{y} \sim \mathcal{N}(\mathbf{E}\mathbf{a}, \sigma^2\mathbf{I}) $$,

$$ \mathbf{a} \sim \mathcal{D}(\boldsymbol{\alpha}) $$,

$$ \sigma^2 \sim \mathcal{HC}(\beta) $$,

$$ \beta \sim \mathcal{U}(0, 10^{-4}) $$.

As you might guess, this formulation of the posterior distribution cannot be solved analytically. Instead, we use [*Markov Chain Monte Caelo (MCMC)*](https://en.wikipedia.org/wiki/Markov_chain_Monte_Carlo) to sample and estimate the posterior. For educational purposes, I’ve implemented a custom sampler based on the [*Metropolis-Hastings Random Walk*](https://en.wikipedia.org/wiki/Metropolis%E2%80%93Hastings_algorithm) in Python. In practice, however, modern samplers like *NUTS (No-U-Turn Sampler)* in an established library such as [PyMC](https://www.pymc.io/welcome.html) are often preferable. They offer a more efficient and streamlined sampling process, sparing users the burden of directly managing the nasty mathematics behind these algorithms.

In the Metropolis-Hastings algorithm, we iteratively draw samples from the posterior. For each new sample, we evaluate its probability relative to the previous sample. The sample is either accepted or rejected based on this evaluation. Over many iterations, the density of accepted samples approximates the true posterior distribution.

To illustrate, the animation below shows the random walk process for sampling three abundance parameters in a mixture of three endmembers. The blue regions represent the true posterior distribution. Notice how the sampler, starting from a random point in the parameter space, gradually converges to the high-probability regions:

![Random Walk Example](assets/img/post_2_random_walk.gif)
<div class="caption">
    Image 1. Random Walk Example on a known target distribution
</div>


### Practical Example

In this example, we are dealing with a sandstone rock sample. We have three minerals that represent the three main component of sandstone rock which quartz as the grains, clay as the matrix and carbonates as the cement. We assume that the endmember spectra is known for this mineral either by direct measurement in laboratory, from a spectral library, or from an endmember extraction algorithm if we are dealing with hyperspectral imagery. We wil begin the example with a single mixed spectra as shown in image below:

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/post_2_data.png" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    Image 2. Endmember spectra for Carbonate, Quartz, Clay minerals, and the observed mixed spectra
</div>


pharagraph

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/post_2_trace_plot.png" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    Image 3. Marginal posterior distribution of each endmembers abundance and its trace plots
</div>


pharagraph

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/post_2_corner_plot.png" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    Image 4. Corner plot of the marginal posterior showing correlations between each endmember abundances
</div>

pharagraph

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/post_2_ternary.png" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    Image 5. Ternary plot 
</div>

pharagraph

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/post_2_modeled_spectra.png" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    Image 6. Observed spectra vs distribution of the modeled spectra 
</div>

pharagraph

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/post_2_rock_sample.png" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    Image 7. Bayesian spectral unmixing result on a hyperspectral image of a rock sample
</div>