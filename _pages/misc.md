---
layout: page
title: Misc
permalink: /misc/
description: A few moments I captured that have great energy ☀️
nav: true
nav_order: 7
_styles: |
  .misc-collage {
    width: 100%;
    max-width: 100%;
  }
  .misc-collage .misc-lead {
    font-size: 0.85rem;
    line-height: 1.5;
    opacity: 0.88;
    margin-bottom: 1.25rem;
    letter-spacing: 0.02em;
  }
  /* Manual: add misc-tile--landscape (2 per row) or misc-tile--portrait (3 per row) on each <figure> */
  .misc-collage__grid {
    display: grid;
    grid-template-columns: repeat(6, minmax(0, 1fr));
    gap: 8px;
    align-items: start;
  }
  @media (min-width: 768px) {
    .misc-collage__grid {
      gap: 10px;
    }
  }
  .misc-collage__grid figure {
    margin: 0;
    min-width: 0;
    grid-column: span 6;
  }
  .misc-collage__grid figure.misc-tile--landscape {
    grid-column: span 3;
  }
  .misc-collage__grid figure.misc-tile--portrait {
    grid-column: span 2;
  }
  @media (max-width: 767px) {
    .misc-collage__grid figure.misc-tile--landscape,
    .misc-collage__grid figure.misc-tile--portrait {
      grid-column: span 6;
    }
  }
  .misc-collage__grid img {
    width: 100%;
    height: auto;
    display: block;
    border-radius: 0;
  }
  /* h-* pairs: left column = all (a), right column = all (b), stacked top→bottom */
  .misc-collage__pairs {
    display: grid;
    grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
    gap: 8px 10px;
    align-items: start;
    margin-bottom: 0.5rem;
  }
  .misc-collage__pairs-col {
    display: flex;
    flex-direction: column;
    gap: 8px;
    min-width: 0;
  }
  .misc-collage__pairs-col figure {
    margin: 0;
  }
  .misc-collage__pairs-col img {
    width: 100%;
    height: auto;
    display: block;
    border-radius: 0;
  }
  /* v-* triplets: three columns (a / b / c), stacked top→bottom */
  .misc-collage__triples {
    display: grid;
    grid-template-columns: minmax(0, 1fr) minmax(0, 1fr) minmax(0, 1fr);
    gap: 8px 10px;
    align-items: start;
    margin-bottom: 0.5rem;
  }
  .misc-collage__triples-col {
    display: flex;
    flex-direction: column;
    gap: 8px;
    min-width: 0;
  }
  .misc-collage__triples-col figure {
    margin: 0;
  }
  .misc-collage__triples-col img {
    width: 100%;
    height: auto;
    display: block;
    border-radius: 0;
  }
---

<div class="misc-collage" markdown="0">

<div class="misc-collage__pairs" aria-label="Matched h pairs">

<div class="misc-collage__pairs-col misc-collage__pairs-col--a">
<figure><img src="{{ '/assets/img/misc/h-3a.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure><img src="{{ '/assets/img/misc/h-4a.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure><img src="{{ '/assets/img/misc/h-5a.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure><img src="{{ '/assets/img/misc/h-6a.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure><img src="{{ '/assets/img/misc/h-7a.jpg' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure><img src="{{ '/assets/img/misc/h-8a.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure><img src="{{ '/assets/img/misc/h-9a.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure><img src="{{ '/assets/img/misc/h-1a.jpg' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure><img src="{{ '/assets/img/misc/h-2a.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
</div>

<div class="misc-collage__pairs-col misc-collage__pairs-col--b">
<figure><img src="{{ '/assets/img/misc/h-3b.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure><img src="{{ '/assets/img/misc/h-4b.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure><img src="{{ '/assets/img/misc/h-5b.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure><img src="{{ '/assets/img/misc/h-6b.jpg' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure><img src="{{ '/assets/img/misc/h-7b.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure><img src="{{ '/assets/img/misc/h-8b.jpg' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure><img src="{{ '/assets/img/misc/h-9b.jpg' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure><img src="{{ '/assets/img/misc/h-1b.jpg' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure><img src="{{ '/assets/img/misc/h-2b.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
</div>

</div>

<div class="misc-collage__triples" aria-label="Matched v triplets">

<div class="misc-collage__triples-col misc-collage__triples-col--a">
<figure><img src="{{ '/assets/img/misc/v-1a.jpg' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure><img src="{{ '/assets/img/misc/v-2a.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure><img src="{{ '/assets/img/misc/v-3a.jpg' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure><img src="{{ '/assets/img/misc/v-4a.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
</div>

<div class="misc-collage__triples-col misc-collage__triples-col--b">
<figure><img src="{{ '/assets/img/misc/v-1b.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure><img src="{{ '/assets/img/misc/v-2b.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure><img src="{{ '/assets/img/misc/v-3b.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure><img src="{{ '/assets/img/misc/v-4b.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
</div>

<div class="misc-collage__triples-col misc-collage__triples-col--c">
<figure><img src="{{ '/assets/img/misc/v-1c.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure><img src="{{ '/assets/img/misc/v-2c.jpg' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure><img src="{{ '/assets/img/misc/v-3c.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
</div>

</div>

<div class="misc-collage__grid" aria-label="More images">

<!-- 其余：横图 misc-tile--landscape（一排 2）｜竖图 misc-tile--portrait（一排 3） -->

<figure class="misc-tile--landscape"><img src="{{ '/assets/img/misc/IMG_3797.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure class="misc-tile--landscape"><img src="{{ '/assets/img/misc/IMG_4861.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure class="misc-tile--landscape"><img src="{{ '/assets/img/misc/IMG_6649.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure class="misc-tile--landscape"><img src="{{ '/assets/img/misc/IMG_3288.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure class="misc-tile--landscape"><img src="{{ '/assets/img/misc/IMG_4866.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure class="misc-tile--landscape"><img src="{{ '/assets/img/misc/IMG_7308.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure class="misc-tile--landscape"><img src="{{ '/assets/img/misc/DSCF7727.jpg' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure class="misc-tile--landscape"><img src="{{ '/assets/img/misc/DSCF3136.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure class="misc-tile--landscape"><img src="{{ '/assets/img/misc/IMG_8677.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure class="misc-tile--landscape"><img src="{{ '/assets/img/misc/IMG_6377.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure class="misc-tile--landscape"><img src="{{ '/assets/img/misc/IMG_6739.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure class="misc-tile--landscape"><img src="{{ '/assets/img/misc/ad8b92661qab607639f02b98487ba4f5.jpg' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure class="misc-tile--landscape"><img src="{{ '/assets/img/misc/ee341ecc1g7e9637d72e22ce388e1775.jpg' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure class="misc-tile--landscape"><img src="{{ '/assets/img/misc/522daa4fbf4130f3f581db6f2064ec1c.jpg' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure class="misc-tile--landscape"><img src="{{ '/assets/img/misc/IMG_8475.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure class="misc-tile--landscape"><img src="{{ '/assets/img/misc/IMG_8643.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure class="misc-tile--landscape"><img src="{{ '/assets/img/misc/IMG_1776.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure class="misc-tile--landscape"><img src="{{ '/assets/img/misc/IMG_6660.JPG' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure class="misc-tile--landscape"><img src="{{ '/assets/img/misc/IMG_8725.jpg' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>
<figure class="misc-tile--landscape"><img src="{{ '/assets/img/misc/IMG_9890.jpg' | relative_url }}" alt="" loading="lazy" data-zoomable></figure>

</div>

</div>
