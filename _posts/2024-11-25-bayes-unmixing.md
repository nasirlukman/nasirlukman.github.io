---
layout: post
title: Different Distance Metrics Example in Spectral Unmixing
date: 2024-11-15 23:36:10
description: Comparison between Euclidean distance, Manhattan distance, and angular distance in spectral unmixing
---

In the [last post](https://nasirlukman.github.io/blog/2024/distance/) we've talk a little bit about how spectral unmixing in practice will always suffer from a certain level of uncertainty both related to the data and the model that we are using. Optimization approach to such problem such as the one used in previous post assume that the data and the model are perfect, or at least the uncertainty related to both are negligible. In this post we will look briefly at the Bayesian approach on spectral unmixing, where we explicitly model the uncertainty related to our problem and pass the uncertainty to the final results of our unmixing. So instead of getting a vector of mineral abundances as the result of our unmixing, we got the full probability distribution of the results. 

In this post we will not going into too much detail related to the math, but some formulations are necessary to laid down the problem. First, we can formulate linear mixture model as:

$$ \mathbf{y} = \mathbf{E} \mathbf{a} + \mathbf{e} $$

where:
- $$ \mathbf{y} $$ is the observed spectrum,
- $$ \mathbf{E} $$ is the endmembers matrix,
- $$ \mathbf{a} $$ is the abundance vector,
- $$ \mathbf{e} $$ represents error terms/uncertainty.

> Note for the context of this post, we will be dealing with the unmixing problem for minerals in a particulate surface (such as rocks surface). Due to multtiple scattering-effect the linear relationship above breaks down for reflectance. Instead of reflectance, we will be using [Single Scattering Albedo (SSA)](https://en.wikipedia.org/wiki/Single-scattering_albedo) which derived from Hapke's Model for the remaining of this post. For further information the reader are advised to read [](), [](), or other sources available online (including my [thesis](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=http://essay.utwente.nl/101556/1/Lukman_MA_ITC.pdf&ved=2ahUKEwjqlY-m8faJAxUdw6ACHRUJKj0QFnoECBkQAQ&usg=AOvVaw3Tbo1LEGrTchQ7edNZoxGt)🤪)

Following [Bayes Theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem) we can formulate this problems as:

$$ bayes formula $$

where:
(descrition of symbols)

here we will assume that $$ \mathbf{e} $$ is normally distributed, hence we will use a normal likelihood. We will use a dirichlet prior for $$ \mathbf{a} $$ since it respect the non-negativity and sum-to-one constraint of the abundance vector, and half cauchy prior for the  && \sigma_2 $$ with uniform distribution for its scale hyperparameter $$ \beta $$. the heirarchical structure of the random variable are:

(show the heirarchical structure)

start
Following [Bayes' Theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem), we can formulate this problem as:

$$
P(\mathbf{a}, \sigma^2 \mid \mathbf{y}, \mathbf{E}) = \frac{P(\mathbf{y} \mid \mathbf{a}, \sigma^2, \mathbf{E}) P(\mathbf{a}) P(\sigma^2)}{P(\mathbf{y} \mid \mathbf{E})}
$$

where:
- \(P(\mathbf{a}, \sigma^2 \mid \mathbf{y}, \mathbf{E})\) is the posterior distribution of the abundance vector and error variance given the observed spectrum and endmembers,
- \(P(\mathbf{y} \mid \mathbf{a}, \sigma^2, \mathbf{E})\) is the likelihood of the observed spectrum,
- \(P(\mathbf{a})\) is the prior distribution of the abundance vector,
- \(P(\sigma^2)\) is the prior distribution of the error variance,
- \(P(\mathbf{y} \mid \mathbf{E})\) is the evidence (or marginal likelihood) which normalizes the posterior.

Here we assume that the error term \(\mathbf{e}\) is normally distributed, so we use a normal likelihood:

$$
P(\mathbf{y} \mid \mathbf{a}, \sigma^2, \mathbf{E}) = \mathcal{N}(\mathbf{y} \mid \mathbf{E}\mathbf{a}, \sigma^2\mathbf{I}),
$$

where \(\mathbf{I}\) is the identity matrix. 

For the abundance vector \(\mathbf{a}\), we use a [Dirichlet prior](https://en.wikipedia.org/wiki/Dirichlet_distribution), which respects the non-negativity and sum-to-one constraints:

$$
P(\mathbf{a}) = \text{Dirichlet}(\mathbf{a} \mid \boldsymbol{\alpha}),
$$

where \(\boldsymbol{\alpha}\) is the concentration parameter. 

For the variance \(\sigma^2\), we use a Half-Cauchy prior:

$$
P(\sigma^2) = \text{Half-Cauchy}(\sigma^2 \mid \beta),
$$

where \(\beta\) is the scale hyperparameter, and we assume a uniform prior for \(\beta\):

$$
P(\beta) = \text{Uniform}(\beta \mid 0, \infty).
$$

The hierarchical structure of the random variables is:

- \(\mathbf{y} \sim \mathcal{N}(\mathbf{E}\mathbf{a}, \sigma^2\mathbf{I})\),
- \(\mathbf{a} \sim \text{Dirichlet}(\boldsymbol{\alpha})\),
- \(\sigma^2 \sim \text{Half-Cauchy}(\beta)\),
- \(\beta \sim \text{Uniform}(0, \infty)\).

end



<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/post_2_random_walk.gif" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    Image 1. Random Walk Example on synthetic target distribution
</div>

### Practical Example

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/post_2_data.png" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    Image 2. Endmember spectra for Carbonate, Quartz, Clay minerals, and the observed mixed spectra
</div>


<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/post_2_trace_plot.png" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    Image 3. Marginal posterior distribution of each endmembers abundance and its trace plots
</div>

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/post_2_corner_plot.png" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    Image 4. Corner plot of the marginal posterior showing correlations between each endmember abundances
</div>

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/post_2_ternary.png" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    Image 5. Ternary plot 
</div>

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/post_2_modeled_spectra.png" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    Image 6. Observed spectra vs distribution of the modeled spectra 
</div>

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/post_2_rokc_sample.png" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    Image 7. Bayesian spectral unmixing result on a hyperspectral image of a rock sample
</div>