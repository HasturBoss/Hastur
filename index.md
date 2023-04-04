---
layout: default
---

[![png]({{site.baseurl}}/assets/images/search/google.png)](https://www.google.com)

<div class="home">

  <h1 class="page-heading">Posts</h1>

  <ul class="post-list">
    {% for post in site.posts %}
      <li>
        <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>

        <h2>
          <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
        </h2>
      </li>
    {% endfor %}
  </ul>

  <p class="rss-subscribe"><a href="{{ "/feed.xml" | prepend: site.baseurl }}"><img src="{{site.baseurl}}/assets/images/home/rss.png"></a></p>

</div>