---
layout: default
permalink: /post/
title: post
description: Blog posts on remote sensing, hyperspectral imaging, radar, GIS, and geospatial data science for mining, forest, and environmental monitoring.
nav: true
nav_order: 1
---
{% if site.display_categories and site.display_categories.size > 0 %}
<div class="category-filter" role="group" aria-label="Filter posts by category">
  <button type="button" class="filter-btn active" data-filter="all">All</button>
  {% for category in site.display_categories %}
  <button type="button" class="filter-btn" data-filter="{{ category | slugify }}">{{ category }}</button>
  {% endfor %}
</div>

<style>
  .category-filter { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 0.5rem 0 1.5rem; }
  .category-filter .filter-btn {
    border: 1px solid var(--global-theme-color); background: transparent; color: var(--global-theme-color);
    border-radius: 999px; padding: 0.25rem 0.9rem; font-size: 0.9rem; cursor: pointer; transition: all 0.15s ease;
  }
  .category-filter .filter-btn:hover, .category-filter .filter-btn.active { background: var(--global-theme-color); color: #fff; }
  .post-list li.is-hidden { display: none; }
</style>

<script>
  document.addEventListener('DOMContentLoaded', function () {
    var buttons = document.querySelectorAll('.category-filter .filter-btn');
    var posts = document.querySelectorAll('.post-list > li');
    function apply(filter) {
      buttons.forEach(function (b) { b.classList.toggle('active', b.dataset.filter === filter); });
      posts.forEach(function (li) {
        var cats = (li.dataset.categories || '').split(' ');
        li.classList.toggle('is-hidden', filter !== 'all' && cats.indexOf(filter) === -1);
      });
    }
    buttons.forEach(function (b) {
      b.addEventListener('click', function () {
        apply(b.dataset.filter);
        history.replaceState(null, '', b.dataset.filter === 'all' ? location.pathname : '#' + b.dataset.filter);
      });
    });
    var hash = location.hash.replace('#', '');
    if (hash && document.querySelector('.filter-btn[data-filter="' + hash + '"]')) apply(hash);
  });
</script>
{% endif %}

<div class="post">
  <ul class="post-list">
    {% for post in site.posts %}
      {% assign read_time = post.content | number_of_words | divided_by: 180 | plus: 1 %}
      <li data-categories="{% for c in post.categories %}{{ c | slugify }} {% endfor %}">
        <h3>
          <a class="post-title" href="{{ post.url | relative_url }}">{{ post.title }}</a>
        </h3>
        <p>{{ post.description }}</p>
        <p class="post-meta">
          {{ read_time }} min read &nbsp; &middot; &nbsp;
          {{ post.date | date: '%B %d, %Y' }}
        </p>
      </li>
    {% endfor %}
  </ul>
</div>
