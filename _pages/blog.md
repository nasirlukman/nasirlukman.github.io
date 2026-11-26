---
layout: default
permalink: /post/
title: post
description: Blog posts on remote sensing, hyperspectral imaging, radar, GIS, and geospatial data science for mining, forest, and environmental monitoring.
nav: true
nav_order: 1
pagination:
  enabled: false
  collection: posts
  permalink: /page/:num/
  per_page: 10
  sort_field: date
  sort_reverse: true
  trail:
    before: 1 # The number of links before the current page
    after: 3 # The number of links after the current page
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

{% assign featured_posts = site.posts | where: "featured", "true" %}
{% if featured_posts.size > 0 %}
<br>

<div class="container featured-posts">
{% assign is_even = featured_posts.size | modulo: 2 %}
<div class="row row-cols-{% if featured_posts.size <= 2 or is_even == 0 %}2{% else %}3{% endif %}">
{% for post in featured_posts %}
<div class="col mb-4">
<a href="{{ post.url | relative_url }}">
<div class="card hoverable">
<div class="row g-0">
<div class="col-md-12">
<div class="card-body">
<div class="float-right">
<i class="fa-solid fa-thumbtack fa-xs"></i>
</div>
<h3 class="card-title text-lowercase">{{ post.title }}</h3>
<p class="card-text">{{ post.description }}</p>

                    {% if post.external_source == blank %}
                      {% assign read_time = post.content | number_of_words | divided_by: 180 | plus: 1 %}
                    {% else %}
                      {% assign read_time = post.feed_content | strip_html | number_of_words | divided_by: 180 | plus: 1 %}
                    {% endif %}
                    {% assign year = post.date | date: "%Y" %}

                    <p class="post-meta">
                      {{ read_time }} min read &nbsp; &middot; &nbsp;
                      <a href="{{ year | prepend: '/blog/' | prepend: site.baseurl}}">
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </a>
        </div>
      {% endfor %}
      </div>
    </div>
    <hr>

{% endif %}

  <ul class="post-list">

    {% if page.pagination.enabled %}
      {% assign postlist = paginator.posts %}
    {% else %}
      {% assign postlist = site.posts %}
    {% endif %}

    {% for post in postlist %}

    {% if post.external_source == blank %}
      {% assign read_time = post.content | number_of_words | divided_by: 180 | plus: 1 %}
    {% else %}
      {% assign read_time = post.feed_content | strip_html | number_of_words | divided_by: 180 | plus: 1 %}
    {% endif %}
    {% assign tags = post.tags | join: "" %}
    {% assign categories = post.categories | join: "" %}

    <li data-categories="{% for c in post.categories %}{{ c | slugify }} {% endfor %}">

{% if post.thumbnail %}

<div class="row">
          <div class="col-sm-9">
{% endif %}
        <h3>
        {% if post.redirect == blank %}
          <a class="post-title" href="{{ post.url | relative_url }}">{{ post.title }}</a>
        {% elsif post.redirect contains '://' %}
          <a class="post-title" href="{{ post.redirect }}" target="_blank">{{ post.title }}</a>
          <svg width="2rem" height="2rem" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
            <path d="M17 13.5v6H5v-12h6m3-3h6v6m0-6-9 9" class="icon_svg-stroke" stroke="#999" stroke-width="1.5" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"></path>
          </svg>
        {% else %}
          <a class="post-title" href="{{ post.redirect | relative_url }}">{{ post.title }}</a>
        {% endif %}
      </h3>
      <p>{{ post.description }}</p>
      <p class="post-meta">
        {{ read_time }} min read &nbsp; &middot; &nbsp;
        {{ post.date | date: '%B %d, %Y' }}
        {% if post.external_source %}
        &nbsp; &middot; &nbsp; {{ post.external_source }}
        {% endif %}
      </p>

{% if post.thumbnail %}

</div>

  <div class="col-sm-3">
    <img class="card-img" src="{{ post.thumbnail | relative_url }}" style="object-fit: cover; height: 90%" alt="image">
  </div>
</div>
{% endif %}
    </li>

    {% endfor %}

  </ul>

{% if page.pagination.enabled %}
{% include pagination.liquid %}
{% endif %}

</div>
