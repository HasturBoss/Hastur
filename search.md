---
layout: page
title: Search
tagline: Yor's Secret Box
ref: search
order: 1
---

[![png](/images/search/google.png)](https://www.google.com)

This site blog content search engine:

<!-- HTML elements for search -->
<input type="text" id="search-input" placeholder="Search Blog - Enter Title/Related Content/Date/Tags.." style="width:450px;"/>
<ul id="results-container"></ul>

<!-- script pointing to jekyll-search.js -->
<script src="/script/simple-jekyll-search.min.js"></script>

<script>
SimpleJekyllSearch({
    searchInput: document.getElementById('search-input'),
    resultsContainer: document.getElementById('results-container'),
    json: '/script/search.json',
    searchResultTemplate: '<li><a href="{url}" title="{desc}">{title}</a></li>',
    noResultsText: 'No article found',
    limit: 20,
    fuzzy: false
  })
</script>

Yor's YouTube URL: [Yor's Video](https://www.youtube.com/@user-yor/featured)

Yor's Gmail URL: [Yor's Gmail](https://mail.google.com/mail)

[Home Page]({{ '/' | absolute_url }})
