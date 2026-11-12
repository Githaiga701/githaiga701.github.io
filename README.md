# Gideon Githaiga: portfolio

Source for https://githaiga701.github.io

A single static page: no framework and no build step on GitHub's side.

## Editing

- Projects, experience and skills live as plain lists at the top of `build.py`.
- Page layout, styles and the fixed text live in `template.html`.
- After editing either file, run `python3 build.py` to regenerate `index.html`, then commit and push.

## Photo

Save a portrait as `assets/gideon.jpg` (4:5, about 800 x 1000 px). Until that file exists the page shows a monogram.

## Files

- `index.html`: the generated page that GitHub Pages serves
- `assets/`: fonts (self-hosted, open licences), favicon, social preview image, CV
- `404.html`: shown for unknown addresses
