---
layout: page
title: What to do with tailings that's already there?
description: a project with a background image
img: assets/img/12.jpg
importance: 1
category: work
related_publications: true
---

Our current best efforts to achieve a greener future is weirdly enough dependent upon the mining activity of critical raw materials, at least until foreseeable future where fully circular economy may be possible[1](https://www.nature.com/articles/s41578-021-00325-9). A great deal of care needs to be taken so this "new demand" of critical raw materials will not causes new environement and societal problems. One important frontier on this aspect is to take another look at the (mostly) neglected and problematic mine tailings.

Tailings are waste materials left after the target mineral is extracted from a mining activity. Its often contain heavy metals which may causes risks for environemnt and human health if it's not properly managed. And let's be honest, it's just ugly to look at.
Managing tailings should be one of the responsibility for the mining company with the main goal to fianlly do revegation and rehabilitation of the tailings stockpiles and restor natural habitats on the affected areas. While this can be really challenging and expensive in practice, In most country, it is strictly regulated to do so, as it should be. In some regions, thought, some external factors (economy, policies, lobbies) make it more complicated to enforced.

While causing a great deal of risks, a lot of tailings are reported to still contain a high consentration of critical raw material that still potentially economically mineable[2](https://theintelligentminer.com/2024/01/17/take-two-why-mine-tailings-are-worth-another-look/). This remaining of econocmically mineable critical raw materials may resulted from various reasons. For example, it may be at the time of mining activity occur, the cut of grade of ores are different to the difference of prices in the market, and also different cost related to mining activity. It may also related to insufienece technology or capital to mine or process other secondary minerals in a mine. All of this is ofcourse against today's good mining practice which pushes the miner to extract any potentially valuable minerals from the dugged dirt.



In this project I was looking at the possibilities of using Sentinel-2A time series data. The Idea was to exploit the absorption feature of a certain REE metals that is reported to present in mining tailing in Bangka Island in a times series images. assuming a constant influx of materials to the tailings, 

    ---
    layout: page
    title: project
    description: a project with a background image
    img: /assets/img/12.jpg
    ---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/1.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/3.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/5.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Caption photos easily. On the left, a road goes through a tunnel. Middle, leaves artistically fall in a hipster photoshoot. Right, in another hipster photoshoot, a lumberjack grasps a handful of pine needles.
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/5.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    This image can also have a caption. It's like magic.
</div>

You can also put regular text between your rows of images, even citations {% cite einstein1950meaning %}.
Say you wanted to write a bit about your project before you posted the rest of the images.
You describe how you toiled, sweated, _bled_ for your project, and then... you reveal its glory in the next row of images.

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    You can also have artistically styled 2/3 + 1/3 images, like these.
</div>

The code is simple.
Just wrap your images with `<div class="col-sm">` and place them inside `<div class="row">` (read more about the <a href="https://getbootstrap.com/docs/4.4/layout/grid/">Bootstrap Grid</a> system).
To make images responsive, add `img-fluid` class to each; for rounded corners and shadows use `rounded` and `z-depth-1` classes.
Here's the code for the last row of images above:

{% raw %}

```html
<div class="row justify-content-sm-center">
  <div class="col-sm-8 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
```

{% endraw %}
