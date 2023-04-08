<div align="center">
  <p><em><strong>Disclaimer:</strong> The information here may vary depending on the version you're using.<br/>
  Please refer to the <code>README.md</code> bundled within the theme-gem for information specific to your version or by pointing
  your browser to the Git tag corresponding to your version. e.g. https://github.com/HasturBoss/Hastur/blob/main/README.md.<br/>
  Running <code>bundle show minima</code> will provide you with the local path to your current theme version.</em></p>
  <img src="/README.svg"/>
  <p>It's Jekyll's default (and first) theme. It's what you get when you run <code>jekyll new</code>.</p>
  <p><a href="https://hasturboss.github.io/Hastur/">Theme preview</a></p>
</div>

## Installation

Add this line to your Jekyll site's Gemfile:

```ruby
gem "minima"
```

And then execute:

    $ bundle


## Contents At-A-Glance

Minima has been scaffolded by the `jekyll new-theme` command and therefore has all the necessary files and directories to have a new Jekyll site up and running with zero-configuration.

### Layouts

Refers to files within the `_layouts` directory, that define the markup for your theme.

  - `default.html` &mdash; The base layout that lays the foundation for subsequent layouts. The derived layouts inject their
    contents into this file at the line that says ` {{ content }} ` and are linked to this file via
    [FrontMatter](https://jekyllrb.com/docs/frontmatter/) declaration `layout: base`.
  - `home.html` &mdash; The layout for your landing-page / home-page / index-page. [[More Info.](#home-layout)]
  - `page.html` &mdash; The layout for your documents that contain FrontMatter, but are not posts.
  - `post.html` &mdash; The layout for your posts.

#### Base Layout

From Minima v3 onwards, the base layout is named **`default.html`**, whichever route being the easiest:

```
---
# new `_layouts/default.html` for backwards-compatibility when multiple
# layouts have been customized.

layout: default
---

{{ content }}
```

#### Home Layout

`home.html` is a flexible HTML layout for the site's landing-page / home-page / index-page. <br/>

##### *Main Heading and Content-injection*

From Minima v2.2 onwards, the *home* layout will inject all content from your `index.md` / `index.html` **before** the **`Posts`** heading. This will allow you to include non-posts related content to be published on the landing page under a dedicated heading. *We recommended that you title this section with a Heading2 (`##`)*.

Usually the `site.title` itself would suffice as the implicit 'main-title' for a landing-page. But, if your landing-page would like a heading to be explicitly displayed, then simply define a `title` variable in the document's front matter and it will be rendered with an `<h1>` tag.

##### *Post Listing*

This section is optional from Minima v2.2 onwards.<br/>
It will be automatically included only when your site contains one or more valid posts or drafts (if the site is configured to `show_drafts`).

The title for this section is `Posts` by default and rendered with an `<h2>` tag. You can customize this heading by defining a `list_title` variable in the document's front matter.


### Includes

Refers to snippets of code within the `_includes` directory that can be inserted in multiple layouts (and another include-file as well) within the same theme-gem.

  - `disqus_comments.html` &mdash; Code to markup disqus comment box.
  - `footer.html` &mdash; Defines the site's footer section.
  - `google-analytics.html` &mdash; Inserts Google Analytics module (active only in production environment).
  - `head.html` &mdash; Code-block that defines the `<head></head>` in *default* layout.
  - `header.html` &mdash; Defines the site's main header section. By default, pages with a defined `title` attribute will have links displayed here.
  - `social.html` &mdash; Renders social-media icons based on the `minima:social_links` data in the config file.
  - `social-links/*.svg` &mdash; SVG markup components of supported social-icons.


### Sass

Refers to `.scss` files within the `_sass` directory that define the theme's styles.

  - `custom/default.scss` &mdash; The "white" skin of the theme. *Used by default.*
  - `minima.scss` &mdash; A component that defines the theme's *skin-agnostic* variable defaults and sass partials.
    It imports the following components (in the following order):
    - `minima/_base.scss` &mdash; Sass partial for resets and defines base styles for various HTML elements.
    - `minima/_layout.scss` &mdash; Sass partial that defines the visual style for various layouts.
    - `minima/_syntax-highlighting.scss` &mdash; A hook that allows overriding styles defined above. (*Note: Cannot override variables*)

Refer the [skins](#skins) section for more details.


### Assets

Refers to various asset files within the `assets` directory.

  - `assets/themes/style.scss` &mdash; Imports sass files from within the `_sass` directory and gets processed into the theme's
    stylesheet: `assets/themes/styles.css`.
  - `assets/themes/icons.liquid` &mdash; Imports enabled social-media icon graphic and gets processed into a composite SVG file.
    Refer [section on social networks](#social-networks) for its usage.


### Plugins

Minima comes with [`jekyll-seo-tag`](https://github.com/jekyll/jekyll-seo-tag) plugin preinstalled to make sure your website gets the most useful meta tags. See [usage](https://github.com/jekyll/jekyll-seo-tag#usage) to know how to set it up.

A JavaScript library to add search functionality to any Jekyll blog.
Place the following code in a file called `search.json` in the **root** of your Jekyll blog. See [usage](https://github.com/christian-fei/Simple-Jekyll-Search#usage) to know how to set it up. (You can also get a copy [from here](/assets/jscripts/search.json))

This file will be used as a small data source to perform the searches on the client side:

```yaml
---
layout: none
---
[
  {% for post in site.posts %}
    {
      "title"    : "{{ post.title | escape }}",
      "category" : "{{ post.category }}",
      "tags"     : "{{ post.tags | join: ', ' }}",
      "url"      : "{{ site.baseurl }}{{ post.url }}",
      "date"     : "{{ post.date }}"
    } {% unless forloop.last %},{% endunless %}
  {% endfor %}
]
```


## Usage

Have the following line in your config file:

```yaml
theme: minima
```


### Customizing templates

To override the default structure and style of minima, simply create the concerned directory at the root of your site, copy the file you wish to customize to that directory, and then edit the file.
e.g., to override the [`_includes/head.html `](_includes/head.html) file to specify a custom style path, create an `_includes` directory, copy `_includes/head.html` from minima gem folder to `<yoursite>/_includes` and start editing that file.

The site's default CSS has now moved to a new place within the gem itself, [`assets/themes/styles.css`](assets/css/style.scss).

You need not maintain entire partial(s) at the site's source just to override a few styles. However, your stylesheet's primary
source (`assets/themes/styles.css`) should contain the following:

  - Front matter dashes at the very beginning (can be empty).
  - Directive to import a skin.
  - Directive to import the base styles (automatically loads overrides when available).

Therefore, your `assets/themes/styles.css` should contain the following at minimum:

```sass
---
---

@import
  "custom/{{ site.minima.skin | default: 'default' }}",
  "minima";
```

#### Skins

Minima 3.0 supports defining and switching between multiple color-palettes (or *skins*).

```
.
├── minima.scss
└── minima
    └── _syntax-highlighting.scss
```


A skin is a Sass file placed in the directory `_sass/custom` and it defines the variable defaults related to the "color"
aspect of the theme. It also embeds the Sass rules related to syntax-highlighting since that is primarily related to color and
has to be adjusted in harmony with the current skin.

The default color palette for Minima is defined within `_sass/custom/white.scss`. To switch to another available skin,
simply declare it in the site's config file. For example, to activate `_sass/custom/black.scss` as the skin, the setting
would be:

```yaml
minima:
  skin: default
```

As part of the migration to support skins, some existing Sass variables have been retired and some **have been redefined** as
summarized in the following table:

Minima 2.0      | Minima 3.0
--------------- | ----------
`$brand-color`  | `$link-base-color`
`$grey-*`       | `$brand-*`
`$orange-color` | *has been removed*

##### Available skins

Skin setting    | Description
--------------- | -----------
classic(white)  | Default, light color scheme.
dark(black)     | Dark variant of the classic skin.
default         | *Adaptive skin* based on the default classic and dark skins.

*:bulb: Adaptive skins switch between the "light" and "dark" variants based on the user's operating system setting or browser setting
(via CSS Media Query [prefers-color-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme)).*

### Customize navigation links

This allows you to set which pages you want to appear in the navigation area and configure order of the links.

For instance, to only link to the `about` page, add the following to your `_config.yml`:

```yaml
header_pages:
  - about.md
```


### Change default date format

You can change the default date format by specifying `site.minima.date_format`
in `_config.yml`.

```
# Minima date format
# refer to http://shopify.github.io/liquid/filters/date/ if you want to customize this
minima:
  date_format: "%b %-d, %Y"
```


### Extending the `<head />`

You can *add* custom metadata to the `<head />` of your layouts by creating a file `_includes/head.html` in your source directory. For example, to add favicons:

1. Head over to [https://realfavicongenerator.net/](https://realfavicongenerator.net/) to add your own favicons.
2. [Customize](#customization) default `_includes/head.html` in your source directory and insert the given code snippet.


### Enabling comments (via Disqus)

Optionally, if you have a Disqus account, you can tell Jekyll to use it to show a comments section below each post.

:warning: `url`, e.g. `https://example.com`, must be set in you config file for Disqus to work.

To enable it, after setting the url field, you also need to add the following lines to your Jekyll site:

```yaml
  disqus:
    shortname: my_disqus_shortname
```

You can find out more about Disqus' shortnames [here](https://help.disqus.com/installation/whats-a-shortname).

Comments are enabled by default and will only appear in production, i.e., `JEKYLL_ENV=production`

If you don't want to display comments for a particular post you can disable them by adding `comments: false` to that post's YAML Front Matter.

### Author Metadata

From `Minima-3.0` onwards, `site.author` is expected to be a mapping of attributes instead of a simple scalar value:

```yaml
author:
  name: Hastur Boss
  email: "hasturboss@qq.com"
```

To migrate existing metadata, update your config file and any reference to the object in your layouts and includes as summarized below:

Minima 2.x    | Minima 3.0
------------- | -------------------
`site.author` | `site.author.name`
`site.email`  | `site.author.email`


### Social networks

You can add links to the accounts you have on other sites, with respective icon as an SVG graphic, via the config file.
From `Minima-3.0` onwards, the social media data is sourced from config key `minima.social_links`. It is a list of key-value pairs, each entry
corresponding to a link rendered in the footer. For example, to render links to Jekyll GitHub repository and twitter account, one should have:

```yaml
minima:
  social_links:
    - { platform: github,  user_url: "https://github.com/HasturBoss/Hastur" }
    - { platform: youtube,  user_url: "https://www.youtube.com/@user-yor" }
    - { platform: facebook,  user_url: "https://www.facebook.com/profile.php?id=100051853814324" }
```

Apart from the necessary keys illustrated above, `title` may also be defined to render a custom link-title. By default, the title is the same
as `platform`. The `platform` key corresponds to the SVG id of the sprite in the composite file at URL `/assets/minima-social-icons.svg`.

The theme ships with an icon for `rss` and icons of select social-media platforms:

- `devto`
- `dribbble`
- `facebook`
- `flickr`
- `github`
- `google`
- `instagram`
- `keybase`
- `linkedin`
- `microdotblog`
- `pinterest`
- `stackoverflow`
- `telegram`
- `twitter`
- `youtube`

To render a link to a platform not listed above, one should first create a file at path `_includes/icons/<PLATFORM>.svg` comprised of
graphic markup **without the top-level `<svg></svg>`**. The icon is expected to be centered within a viewbox of `"0 0 16 16"`. Then, make an
entry under key `minima.social_links`.

For example, to render a link to an account of user `john.doe` at platform `deviantart.com`, the steps to follow would be:
  - Get DeviantArt logo in SVG format.
  - Using a text-editor, open the downloaded file to inspect if the `viewBox` attribute is defined on the `<svg>` element and is set
    as `"0 0 16 16" (or similar "square" dimension)`.
  - If the `viewBox` attribute is non-square or undefined, the graphic *may optionally need* to be edited in a vector graphic editor such as
    *Inkscape* or *Adobe Illustrator* for properly aligned render on page.
  - Edit the SVG file in text-editor to delete everything **except** what is contained between `<svg></svg>` and save it into the Jekyll
    project at path `_includes/icons/deviantart.svg`.
  - Finally, edit the Jekyll config file to enable loading of new icon graphic with:
    ```yaml
    minima:
      social_links:
        - platform: deviantart  # same as SVG filename.
          user_url: "https://www.deviantart.com/john.doe"  # URL of profile page.
          title:  My profile at DeviantArt.com  # Optional. Text displayed on hovering over link.
    ```

**Notes:**
- The list of social-links is declarative. List-items are rendered in the order declared in the downstream configuration file and not merged
  with entries from upstream config file(s) such as theme-config-file or prior local config files.
- The `user_url` is rendered as given without handling any special characters within.


### Enabling Google Analytics

To enable Google Analytics, add the following lines to your Jekyll site:

```yaml
  google_analytics: UA-NNNNNNNN-N
```

Google Analytics will only appear in production, i.e., `JEKYLL_ENV=production`

### Enabling Excerpts on the Home Page

To display post-excerpts on the Home Page, simply add the following to your `_config.yml`:

```yaml
show_excerpts: true
```


## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/jekyll/minima. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## Development

To test your theme, run `bundle exec jekyll serve` and open your browser at `http://localhost:4000/Hastur/`. This starts a Jekyll server using your theme and the contents. As you make modifications, your site will regenerate and you should see the changes in the browser after a refresh.

## License

The theme is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
