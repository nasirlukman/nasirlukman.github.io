---
layout: post
title: "Watching an Open-Pit Mine From Space: Growth, Active Fronts, and Ground Movement"
date: 2026-11-20 20:36:10
description: "Mapping an open-pit mine's growth, monthly changes, active fronts, and centimeter-scale ground movement (InSAR) using only free satellite data."
tags: [mine-monitoring, insar, sar, sentinel-1, land-cover, machine-learning, indonesia]
categories: ["Geoscience", "Environment"]
og_image: /assets/img/og/post_17_ground_movement_map.jpg
---

For the past few weeks, I've been building a monitoring system for an open-pit mine in Indonesia. Mapping a mine from space is not new; I have written about it [before](https://nasirlukman.github.io/blog/2025/illegal-mining/). Most mine maps, though, answer only one question: *how big is the mine?* Once you start talking to the people who actually run (or oversee) a mine, the questions become more specific. What changed this month? Where are they actually digging right now? And is the ground they are *not* touching staying put?

So instead of a single map, I ended up with four layers, each answering one of those questions. All of them are built from free satellite data: Landsat and Sentinel-2 (as [HLS](https://hls.gsfc.nasa.gov/)), Sentinel-1 radar, ALOS PALSAR-2 ScanSAR, and interferometric products from [ASF HyP3](https://hyp3-docs.asf.alaska.edu/). This post walks through them one by one.

## 1. The Annual Map: How Big Is the Mine?

The foundation is an annual land cover map. For every year from 2015 to 2025, I built a yearly stack on a 30 m grid: medians of optical bands and indices from HLS, Sentinel-1 backscatter statistics, and PALSAR-2 L-band backscatter. A Random Forest model trained on labeled points then classifies each pixel as forest/other, mining, water, built-up, or vegetation clearing. A bit of post-processing (majority filter, removing tiny speckles) cleans up the result.

Combining sensors matters here. Optical data tells bare ground apart from vegetation very well, but the tropics are cloudy, so some years have big gaps. Radar sees through clouds and adds information about surface roughness and structure, which helps to separate, for example, a fresh clearing from an actual mine pit.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_17_annual_land_cover.webp"
            animated=true
            class="img-fluid rounded" 
            alt="Animation from 2015 to 2025. Left: yearly median HLS true color image of an open-pit mine surrounded by forest. Right: the land cover map of the same year, with the mine in brown on a pale green background, water in blue and built-up in dark gray. The mine grows from a small patch in the south-west to a large complex."
        %}
    </div>
</div>
<div class="caption">
    Figure 1. Yearly HLS true color composite (left) and the land cover map (right), 2015 to 2025.
</div>

The mine grew from about **200 ha in 2015 to 1,440 ha in 2025**, roughly seven times bigger in ten years (Figure 2). The growth is not constant: it accelerated after 2022, with around 250 ha opened per year between 2022 and 2024.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_17_annual_area.webp" 
            class="img-fluid rounded" 
            alt="Line chart of the mine area per year from 2015 to 2025, rising from 201 ha to 1,440 ha, with steeper growth after 2022."
        %}
    </div>
</div>
<div class="caption">
    Figure 2. Mine area per year from the annual land cover maps.
</div>

Mines don't only grow, though. Looking closely at the animation, some parts of the mine turn green again over the years. Counting them takes a bit of care, because a classifier can easily flicker between "mine" and "vegetation" from one year to the next. So I only counted a pixel as revegetated if it was mine for at least two years in a row, and then vegetation for at least two years in a row. These pixels really are greening: their NDVI goes from about 0.5 to about 0.7 within two years. That is still below the surrounding forest (around 0.85), so this is young vegetation. Unfortunately, from space, planted reclamation and natural regrowth look the same.

Between 2017 and 2024, about **195 ha** of mine land turned green again, with a peak of 41 ha in 2024 (Figure 3). For comparison, about 1,600 ha were opened in the same period, so roughly one hectare turns green for every eight hectares opened. The 2025 bar is provisional: we need the 2026 map to know whether it stays green.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_17_annual_revegetation.webp" 
            class="img-fluid rounded" 
            alt="Bar chart of mine land turning green again per year: 9 ha in 2017, 19 in 2018, 27 in 2019, 31 in 2020, 20 in 2021, 28 in 2022, 20 in 2023 and 41 in 2024, about 195 ha in total. The 2025 bar, 56 ha, is hatched and marked provisional."
        %}
    </div>
</div>
<div class="caption">
    Figure 3. Mine land turning green again per year (reclamation or natural regrowth). A pixel counts if it was mine for at least two years and then vegetation for at least two years; 2025 cannot be confirmed yet.
</div>

## 2. The Monthly Update: What Changed This Month?

An annual map is great for the big picture, but a mine can open tens of hectares in a single month. For 2025, I took the 2024 annual map as a starting point and updated it image by image: every Sentinel-1 acquisition (every 12 days) and every HLS image with enough clear sky.

The rules are deliberately simple:

1. *Evidence of a new opening*: a bare-ground look in an optical image (NDVI drops, the bare soil index rises), or a drop in radar backscatter (VH) that is still there 12 days later.

2. *New mining*: within 600 m of the existing mine, with two bare optical looks, or one bare look plus a confirmed radar drop. Farther away, the same evidence is called *vegetation clearing* instead.

3. *Unconfirmed opening*: evidence that is not confirmed yet. If the evidence disappears (the area turns green again), the candidate is simply removed.

4. *Water*: pits filling up and ponds drying out are followed too, because water hides what is going on underneath.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_17_monthly_maps.webp"
            animated=true
            class="img-fluid rounded" 
            alt="Monthly animation for 2025 showing the mine in brown, unconfirmed openings in purple, vegetation openings in ochre, water in blue and buildings in dark gray on a pale green vegetation background. New openings appear at the mine edges through the year."
        %}
    </div>
</div>
<div class="caption">
    Figure 4. Monthly map updates for 2025. Purple patches are openings that are not confirmed yet; ochre patches are vegetation clearings far from the mine.
</div>

In 2025, the system found about **300 ha of new mining** (Figure 5). The months are not equal, and part of that is the weather rather than the mine. There was not a single clear optical image from January to March (rainy season). Radar kept seeing the changes, and they appear as *unconfirmed* openings in the animation, but they had to wait for the first clear optical look in April to be confirmed. That is a good part of the big April bar. July was the busiest month.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_17_monthly_new_mining.webp" 
            class="img-fluid rounded" 
            alt="Bar chart of new mining per month in 2025: zero from January to March, 88 ha in April, 40 in May, 31 in June, 97 in July, then between 2 and 18 ha per month until December. About 298 ha in the year."
        %}
    </div>
</div>
<div class="caption">
    Figure 5. Confirmed new mining per month in 2025.
</div>

How good is it? I checked an earlier version of the detector visually, patch by patch: about 86% of the new-mining patches were correct, or 99% by area, because the wrong ones were mostly small fragments at the mine edges. Good enough for monthly reporting.

## 3. Active vs. Inactive Front: Where Are They Actually Digging?

Here is something the mine area alone does not tell you. A 1,600 ha mine is not 1,600 ha of digging. Large parts are old benches, waste dumps, haul roads or areas waiting for the next phase. So where is the actual activity?

For this, I used **InSAR coherence**. A simple way to think about it: each radar pixel has a sort of "fingerprint", and coherence measures how much that fingerprint changed between two Sentinel-1 passes 12 days apart. Bare ground that nobody touches keeps its fingerprint (coherence around 0.9). Ground that is dug, dumped or driven over loses it (around 0.3, the same as forest, where the leaves never stop moving). So, inside the mine, *low coherence = active*.

Of course, it is not that simple. Rain between the two dates also destroys coherence, everywhere. To deal with that, each 12-day pair is rescaled between two references: stable forest (0) and the undisturbed part of the mine (1). Pairs where even the undisturbed mine lost its coherence are thrown away; that was 5 of the 31 pairs in 2025. Areas that look vegetated in optical images, or very dark in radar (ponds, radar shadow), are excluded too, because there low coherence means something else.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_17_active_inactive.webp"
            animated=true
            class="img-fluid rounded" 
            alt="Monthly animation for 2025 of the mine split into active front in vermilion and inactive front in brown, with water in blue and built-up in dark gray on a pale green background. Active patches move around the pits from month to month; a haul road stays active."
        %}
    </div>
</div>
<div class="caption">
    Figure 6. Active (vermilion) and inactive (brown) parts of the mine, month by month in 2025.
</div>

Only **12 to 29% of the mine is active in any given month** (Figure 7), between about 160 ha in January and 460 ha in October. The active patches move around from month to month, which is exactly what you would expect from a mine moving its working faces. A nice sanity check: the main haul road connecting the pits is active in every single month of the year.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_17_active_inactive_chart.webp"
            class="img-fluid rounded" 
            alt="Stacked bar chart per month of 2025: active front in vermilion at the bottom and inactive front in brown on top. The total mine grows from 1,322 to 1,618 ha; the active share ranges from 12% in January to 29% in October."
        %}
    </div>
</div>
<div class="caption">
    Figure 7. Active and inactive front per month. The label is the share of the mine that is active.
</div>

I have not validated this layer against ground data yet, so take the exact numbers with a pinch of salt. The patterns, though, look very plausible.

## 4. Ground Movement: Is the Idle Ground Stable?

This is the part I'm most excited about. The same radar pairs carry another piece of information: the *phase* of the signal. The phase difference between two passes measures the change in distance between the ground and the satellite, and one full color cycle in an interferogram is only 2.8 cm. In principle, this lets us measure ground movement of a few centimeters from a satellite almost 900 km away.

In practice, it only works where the ground keeps its fingerprint, so I only used the part of the mine that was **never active in 2025** (about 520 ha). The steps are:

1. *Throw away the rainy pairs* (the same 5 as before).

2. *Remove the atmosphere, as far as possible*: humidity also delays the radar signal, differently on every date. For each pair, a plane and the median over the area are removed, so all values are relative to the idle mine as a whole.

3. *Average all 26 remaining pairs* into one rate per pixel, in cm/month, together with its uncertainty (typically about 0.3 cm/month).

4. *Keep only what is clearly real*: a movement is significant when it is at least twice its own uncertainty and at least 0.5 cm/month.

But is it real, or just the weather? Real movement keeps its direction, while weather changes from date to date. So I split the year in two halves and computed the movement from January–June and July–December separately: the same spots move the same way in both halves (correlation of 0.69). Weather alone would give a correlation close to zero.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_17_ground_movement_map.webp" 
            class="img-fluid rounded" 
            alt="Map of the average ground movement in 2025 in centimeters per month, on the parts of the mine that were never active. Red areas move away from the satellite (settling), blue areas move towards it. Significant areas are outlined. The parts of the mine that were active at some point in the year are shown in light gray."
        %}
    </div>
</div>
<div class="caption">
    Figure 8. Average ground movement in 2025 in the never-active part of the mine. Red: away from the satellite (settling). Blue: towards the satellite. Outlined: significant movement. Gray: parts of the mine that were active at some point in the year (not measured).
</div>

More than half of the idle mine is stable within ±0.5 cm/month. But there are two clear groups of movement (Figure 9):

* **About 84 ha are settling** at around 1 cm/month, about 11 cm over the year. And they are slowing down: around 1.4 cm/month from January to March, down to about 0.5 cm/month at the end of the year. That is the typical behavior of waste dumps or backfill compacting after they were placed. A few hectares settle faster than 2 cm/month; those are the spots I would ask a geotechnical engineer to look at.

* **About 51 ha move towards the satellite** at a similar pace. This one needs careful interpretation, because "towards the satellite" does *not* necessarily mean the ground is rising. Sentinel-1 on this track looks westward and down, so ground sliding eastward, for example down an east-facing dump slope, also moves towards the satellite. It could also be the floor of a recently excavated pit rebounding after the weight above it was removed. Interestingly, 70% of these areas were first mined in 2022–2024, so this is young ground.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid 
            path="assets/img/post_17_ground_movement_series.webp" 
            class="img-fluid rounded" 
            alt="Line chart of cumulative ground movement through 2025: the settling areas reach about -11 cm and the towards areas about +10 cm by the end of the year, both curving slightly flatter over time; the rest of the never-active mine stays near 0."
        %}
    </div>
</div>
<div class="caption">
    Figure 9. Cumulative movement through 2025 for the significant settling areas, the significant "towards" areas, and the rest of the never-active mine. Dotted lines cross the pairs lost to rain.
</div>

There are important limitations here. With only one viewing direction, I cannot separate vertical from horizontal movement. All values are relative to the idle mine, so if the whole area is settling slowly, that part is invisible. And without ground survey data (prisms or GPS), this remains a well-supported hypothesis rather than a measurement. Adding the ascending Sentinel-1 orbit, which looks eastward, would separate vertical from east–west movement, and that is probably the next step.

## Closing Thoughts

What I like about this exercise is how much more a mine "says" once you look at it with different sensors and at different time scales. The annual map shows how big it is. The monthly update shows what is new. Coherence shows where the activity actually is. And the phase shows whether the ground that is left alone is really stable. Each layer answers a question the previous one cannot.

All of this runs on free and open data, on a normal workstation. Ten years ago, centimeter-scale ground movement monitoring of a mine was something you would buy from a specialized company, if you could afford it at all. Today, the main bottleneck is no longer data or computing power, but careful interpretation: knowing what the signal can and cannot tell you, and being honest about it.
