# -*- coding: utf-8 -*-
"""
Static builder for the portfolio.

Everything the site says about a project lives in PROJECTS / PROTOTYPES below,
so copy edits happen in one place. Run `python build.py` to regenerate the
three HTML pages. Image orientation is measured from the files themselves.
"""

import html
import json
import os
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))

SITE = "https://jotunlegion.github.io"
NAME = "Dmytro Bondar"
TITLE = "Senior Game Designer - AI-first Prototyping & LiveOps"
EMAIL = "dimabondar2812@gmail.com"
PHONE = "+380 66 074 1499"
LINKEDIN = "https://www.linkedin.com/in/dmytro-bondar-63a94a144/"
GITHUB = "https://github.com/jotunlegion"

# ---------------------------------------------------------------- shipped work

PROJECTS = [
    {
        "slug": "rainbow-high",
        "name": "Rainbow High: Coloring Games",
        "studio": "Bini Games / TEACH & DRAW LTD",
        "year": "2025",
        "role": "zero",
        "platforms": ["iOS", "Android"],
        "tags": ["zero", "kids", "mobile"],
        "url": "https://apps.apple.com/us/app/id6740995343",
        "rating": (4.6, "559"),
        "blurb": (
            "The title I am proudest of, and the one I owned end to end: concept, core loop, "
            "progression, monetisation and the GDD that the team built from. It landed in the "
            "Top 50 new kids' releases and pulled hundreds of thousands of downloads across iOS "
            "and Android almost entirely on organic traffic. With no meaningful UA budget behind "
            "it, the store page and the first ninety seconds of play had to do the marketing "
            "themselves, so most of my design effort went into making the very first colouring "
            "session feel generous and instantly readable to a child who cannot yet read."
        ),
    },
    {
        "slug": "cats-care",
        "name": "Cats Care! Pet Games for Kids",
        "studio": "Bini Games / TEACH & DRAW LTD",
        "year": "2024",
        "role": "zero",
        "platforms": ["iOS"],
        "tags": ["zero", "kids", "mobile"],
        "url": "https://apps.apple.com/us/app/id6476145721",
        "rating": (4.4, "94"),
        "blurb": (
            "A kitten daycare built from an empty document. Children feed, bathe, treat and tuck "
            "in a room full of restless cats, and every one of those verbs had to survive the "
            "hardest usability audience there is: a four-year-old with no reading ability and no "
            "patience for a tutorial. The design work was mostly subtraction - cutting states, "
            "widening hit areas, and letting animation carry the instructions that text normally "
            "would."
        ),
    },
    {
        "slug": "jigsaw-travel",
        "name": "Jigsaw Travel: Cards Match",
        "studio": "VGam.es",
        "year": "2023",
        "role": "zero",
        "platforms": ["Android"],
        "tags": ["zero", "puzzle", "mobile"],
        "url": "https://play.google.com/store/apps/details?id=com.vgames.solipic&hl=en",
        "rating": None,
        "blurb": (
            "A puzzle hybrid I took from pitch to store: each level is a photograph cut into cards "
            "and shuffled across a board, and the player slides and swaps tiles to bring the "
            "picture back. The interesting design tension was pacing - a jigsaw is calm and a "
            "sliding puzzle is fiddly, so the difficulty curve had to add board size and card "
            "count slowly enough that the restoration always felt like a reward rather than a "
            "chore."
        ),
    },
    {
        "slug": "todli",
        "name": "Todli: Drawing Games for Kids",
        "studio": "Bini Games / TEACH & DRAW LTD",
        "year": "2023-2025",
        "role": "ops",
        "platforms": ["iOS"],
        "tags": ["ops", "kids", "mobile"],
        "url": "https://apps.apple.com/us/app/id908698556",
        "rating": (4.5, "38,160"),
        "blurb": (
            "A long-running title with a large installed base and more than thirty-eight thousand "
            "ratings behind it - the kind of product where you inherit someone else's decisions "
            "and have to improve the numbers without breaking what already works. My work here was "
            "live operations: reading the funnel, forming hypotheses about where sessions were "
            "leaking, writing feature GDDs aimed at specific metrics, and shipping them in a "
            "cadence the team could actually sustain."
        ),
    },
    {
        "slug": "pinksy",
        "name": "Pinksy: Drawing Games for Kids",
        "studio": "Bini Games / TEACH & DRAW LTD",
        "year": "2023-2025",
        "role": "ops",
        "platforms": ["iOS"],
        "tags": ["ops", "kids", "mobile"],
        "url": "https://apps.apple.com/us/app/id1260895318",
        "rating": (4.6, "36,574"),
        "blurb": (
            "The sister product to Todli, and the same discipline applied: analyse the current "
            "metrics, build a hypothesis, write the feature document, ship, measure, repeat. "
            "Working across two mature drawing apps at once was useful precisely because it "
            "exposed which retention effects were real and which were just noise in a single "
            "product's data."
        ),
    },
    {
        "slug": "bini-mega-world",
        "name": "Bini Mega World: Games for Kids",
        "studio": "Bini Games",
        "year": "2023-2025",
        "role": "ops",
        "platforms": ["Android"],
        "tags": ["ops", "kids", "mobile"],
        "url": "https://play.google.com/store/apps/details?id=com.games.bini.world.life.kids.open.town.animal&hl=en",
        "rating": None,
        "blurb": (
            "An open-town sandbox for children stuffed with mini-games, animals and small stories. "
            "As a live-ops product its problem is breadth: there is always somewhere new to add "
            "content, and almost never a clear signal about which corner of the town deserves it. "
            "Most of my contribution was deciding what not to build, and directing feature work at "
            "the specific sessions that the metrics said were ending too early."
        ),
    },
    {
        "slug": "ws-purrfect-horror",
        "name": "Whispered Secrets: Purrfect Horror CE",
        "studio": "GrandMA Studios",
        "year": "2022",
        "role": "zero",
        "platforms": ["PC", "Mac"],
        "tags": ["zero", "hopa", "pc"],
        "url": "https://www.bigfishgames.com/whispered-secrets-purrfect-horror-ce-f18731t1l1.html",
        "rating": (4.2, "24"),
        "blurb": (
            "A hidden-object puzzle adventure built from idea to release: a stolen Egyptian "
            "artefact, a rising tide of missing-person cases, and a great many stray cats. The "
            "craft in a HOPA is almost entirely in pacing - a scene has to alternate between "
            "search, puzzle and story beat often enough that the player never notices they have "
            "been clicking on the same screen for four minutes."
        ),
    },
    {
        "slug": "ws-tying-the-knot",
        "name": "Whispered Secrets: Tying the Knot",
        "studio": "GrandMA Studios",
        "year": "2021",
        "role": "zero",
        "platforms": ["PC", "Mac"],
        "tags": ["zero", "hopa", "pc"],
        "url": "https://www.bigfishgames.com/whispered-secrets-tying-the-knot-f15640t1l1.html",
        "rating": (3.9, "8"),
        "blurb": (
            "Another entry in the Whispered Secrets series, taken from concept through to a "
            "shipped build. Working inside an established series is its own constraint: returning "
            "players arrive with firm expectations about tone and puzzle vocabulary, so novelty "
            "has to be introduced in the story and the set pieces rather than in the controls."
        ),
    },
    {
        "slug": "ws-ripple-of-the-heart",
        "name": "Whispered Secrets: Ripple of the Heart",
        "studio": "GrandMA Studios",
        "year": "2022",
        "role": "zero",
        "platforms": ["PC", "Mac"],
        "tags": ["zero", "hopa", "pc"],
        "url": "https://www.bigfishgames.com/whispered-secrets-ripple-of-the-heart-f18539t1l1.html",
        "rating": (3.5, "2"),
        "blurb": (
            "A further Whispered Secrets case designed and documented from scratch. By this point "
            "the series pipeline was something I had helped rebuild, so the design work and the "
            "production work were inseparable - deciding a puzzle's shape also meant knowing "
            "which art and scripting milestones it would land on."
        ),
    },
    {
        "slug": "mcf-last-resort",
        "name": "Mystery Case Files: The Last Resort CE",
        "studio": "GrandMA Studios",
        "year": "2021",
        "role": "zero",
        "platforms": ["PC", "Mac"],
        "tags": ["zero", "hopa", "pc"],
        "url": "https://www.bigfishgames.com/mystery-case-files-the-last-resort-ce-f15755t1l1.html",
        "rating": (3.0, "94"),
        "blurb": (
            "An entry in one of the longest-running and most scrutinised franchises in the casual "
            "PC market - Mystery Case Files players have been comparing releases for well over a "
            "decade and are extremely vocal about it. Designing into that legacy meant treating "
            "the series bible as a hard constraint and finding room for new ideas in the "
            "investigation structure rather than in the fundamentals."
        ),
    },
    {
        "slug": "city-of-stories",
        "name": "City of Stories: Stephan's Journey",
        "studio": "GrandMA Studios",
        "year": "2021",
        "role": "zero",
        "platforms": ["PC", "Mac"],
        "tags": ["zero", "hopa", "pc"],
        "url": "https://www.bigfishgames.com/city-of-stories-stephans-journey-f16144t2l1.html",
        "rating": (4.0, "4"),
        "blurb": (
            "A new IP rather than a series entry, which meant the design had to establish its own "
            "world, cast and visual grammar with none of the shorthand a sequel inherits. Built "
            "from the first idea through to release alongside the team I was leading at the time."
        ),
    },
    {
        "slug": "point-of-no-return",
        "name": "The Point of no Return",
        "studio": "Treehouse Dreams",
        "year": "2020-2021",
        "role": "zero",
        "platforms": ["PC", "UE4"],
        "tags": ["zero", "narrative", "pc"],
        "url": "https://treehouse-dreams.itch.io/the-point-of-no-return",
        "rating": None,
        "blurb": (
            "A walking simulator on UE4 about a Ukrainian veteran - from the decision to serve, to "
            "coming home with a physical injury and an unsteady mind. I worked as game designer "
            "and, as a former serviceman myself, as military consultant: writing documentation, "
            "reviewing the script and level design, and pushing back whenever a detail rang false. "
            "It was a social project supported by the Ukrainian Cultural Foundation, and easily "
            "the most personal thing on this page."
        ),
    },
]

# ------------------------------------------------------------------ prototypes

PROTOTYPES = [
    {
        "slug": "they-will-make-more",
        "name": "They Will Make More",
        "kicker": "Idle strategy / political satire",
        "url": "https://they-will-make-more.dimabondar2812.workers.dev",
        "stack": ["React", "Cloudflare Workers", "vinext"],
        "blurb": (
            "A state simulator for the accounting of human material - a bleak satire in which you "
            "run an endless offensive from a ministry dashboard. Underneath the joke is a real "
            "economy: 420 fortifications across three fronts, 2,118 kilometres of front line, and "
            "conscription, food, disease, budget and public discontent all feeding one another. "
            "A fortification only falls when every defensive object on it is destroyed, so the "
            "campaign cannot be won by waiting - it has to be supplied. Balanced to roughly ten "
            "hours of real playtime, and deliberately designed so that a player who neglects the "
            "systems fails from a shortage of people rather than from the clock."
        ),
    },
    {
        "slug": "warmatch",
        "name": "WarMatch",
        "kicker": "Base builder + match-3",
        "url": "https://warmatch.pages.dev",
        "stack": ["HTML5 Canvas", "Vanilla JS"],
        "blurb": (
            "A zombie-apocalypse base builder wrapped around a match-3 mini-game, where the "
            "matched pallets are the ammunition and supply that keep your camp alive. Panda "
            "soldiers hold the line, a squad of cheerfully awful sergeants narrate it, and the "
            "two layers are tuned so that a good match-3 run is immediately visible on the base "
            "screen. Fully playable in the browser with a Ukrainian and English interface."
        ),
    },
    {
        "slug": "pixeldron",
        "name": "PixelDron",
        "kicker": "FPV drone deathmatch",
        "url": "https://pixeldron.pages.dev",
        "stack": ["Three.js", "Vite", "Capacitor"],
        "blurb": (
            "An FPV drone deathmatch rendered in deliberately coarse voxels, built in two phases: "
            "first you build a shelter, then you fly. Before a match the pilot picks camouflage, "
            "flag, map and time of day, which gives the arena a surprising amount of variety for "
            "how small the asset set actually is. The flight model is the whole design - it has to "
            "feel twitchy enough to read as FPV without becoming unusable in the first thirty "
            "seconds."
        ),
    },
    {
        "slug": "gravity-bridge",
        "name": "Gravity Bridge",
        "kicker": "3D puzzle runner",
        "url": "https://gravity-bridge.dimabondar2812.workers.dev",
        "stack": ["Three.js", "React", "Cloudflare Workers"],
        "blurb": (
            "A jelly character eats coloured blocks, swells up, and spits them back out to build "
            "bridges across gaps - then walks up the vertical surfaces it has just created. "
            "Stepping on someone else's stair costs a block to repaint, which turns a simple "
            "collect-and-place loop into a small resource decision on every gap. Multiplier gates, "
            "a level map, a shop and a daily gift are all wired in, so the prototype demonstrates "
            "the meta layer and not just the core mechanic."
        ),
    },
    {
        "slug": "binitown",
        "name": "BiniTown",
        "kicker": "Family game hub",
        "url": "https://binitown.pages.dev/",
        "stack": ["Vite", "Phaser", "Three.js"],
        "blurb": (
            "An educational hub pitched as the first game for the whole family: a bright little "
            "town where a farm, a cafe, a fishing spot and a lighthouse each open into their own "
            "mini-game, tied together by a match-3 progression layer. The prototype exists to test "
            "one specific question - whether a parent and a small child can share the same session "
            "without either of them being bored, which mostly comes down to how the difficulty of "
            "each mini-game is split between them."
        ),
    },
    {
        "slug": "floramenta",
        "name": "Floramenta",
        "kicker": "Cognitive training companion",
        "url": "https://floramenta.pages.dev/",
        "stack": ["Vanilla JS", "PWA", "Capacitor"],
        "blurb": (
            "Casual cognitive games and a memory companion aimed at older players, built around "
            "the observation that memory and fine motor skill fade like a garden left untended. "
            "The onboarding asks who the app is for - yourself, a parent, a grandparent - and "
            "shapes the questions and the daily plan accordingly. It is explicitly not a medical "
            "product, and the interface is deliberately quiet: short, bounded sessions, generous "
            "type, and no attempt to keep anyone in the app longer than the exercise needs."
        ),
    },
]

# --------------------------------------------------------------------- helpers

def esc(s):
    return html.escape(str(s), quote=True)


def shots_for(folder, slug):
    """Return web paths for a project's screenshots, sorted, plus orientation."""
    d = os.path.join(ROOT, "assets", "img", folder, slug)
    if not os.path.isdir(d):
        return [], False
    names = sorted(
        f for f in os.listdir(d)
        if f.lower().startswith("shot") and f.lower().endswith((".webp", ".jpg", ".png"))
    )
    # Drop byte-identical duplicates (some capture runs produced the same frame).
    seen, files = set(), []
    for n in names:
        key = os.path.getsize(os.path.join(d, n))
        if key in seen:
            continue
        seen.add(key)
        files.append(n)
    if not files:
        return [], False
    with Image.open(os.path.join(d, files[0])) as im:
        portrait = im.height > im.width
    return ["assets/img/%s/%s/%s" % (folder, slug, f) for f in files], portrait


def icon_for(slug):
    d = os.path.join(ROOT, "assets", "img", "projects", slug)
    for ext in ("webp", "jpg", "png"):
        p = os.path.join(d, "icon." + ext)
        if os.path.exists(p):
            return "assets/img/projects/%s/icon.%s" % (slug, ext)
    return None


def head(title, desc, page):
    return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="{name}">
<link rel="canonical" href="{site}/{page}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{site}/{page}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#08090c">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='15' fill='%23ff7a45'/%3E%3Ctext x='32' y='44' font-family='monospace' font-size='34' font-weight='bold' text-anchor='middle' fill='%2314100d'%3EDB%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
""".format(title=esc(title), desc=esc(desc), name=esc(NAME), site=SITE, page=page)


def nav(active):
    items = [("index.html", "Home"), ("work.html", "Shipped work"), ("lab.html", "Prototypes")]
    links = "".join(
        '<a href="{h}"{c}>{t}</a>'.format(h=h, t=t, c=' class="active" aria-current="page"' if h == active else "")
        for h, t in items
    )
    return """<header class="nav">
  <div class="nav-inner">
    <a class="brand" href="index.html">
      <span class="mark" aria-hidden="true">DB</span>
      <span>{name}<small>SENIOR GAME DESIGNER</small></span>
    </a>
    <nav class="nav-links" aria-label="Main">{links}</nav>
    <a class="btn nav-cta" href="mailto:{email}">Get in touch <span class="arrow" aria-hidden="true">&rarr;</span></a>
    <button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
</header>
""".format(name=esc(NAME), links=links, email=EMAIL)


def footer():
    return """<footer class="footer">
  <div class="shell">
    <p class="big-cta" data-reveal>Have a game that needs a designer?<br><a href="mailto:{email}">{email}</a></p>
    <div class="footer-grid" style="margin-top:3.2rem">
      <div>
        <h4>About this site</h4>
        <p style="font-size:.93rem;max-width:38ch">Hand-built, no framework, no tracking. Every screenshot is pulled from the live store page or captured from the running prototype.</p>
      </div>
      <div>
        <h4>Pages</h4>
        <div class="footer-list">
          <a href="index.html">Home</a>
          <a href="work.html">Shipped work</a>
          <a href="lab.html">Prototypes</a>
        </div>
      </div>
      <div>
        <h4>Elsewhere</h4>
        <div class="footer-list">
          <a href="mailto:{email}">Email</a>
          <a href="{linkedin}" target="_blank" rel="noopener">LinkedIn</a>
          <a href="{github}" target="_blank" rel="noopener">GitHub</a>
          <a href="tel:{phoneraw}">{phone}</a>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span id="year">2026</span> {name}</span>
      <span>Kyiv, Ukraine</span>
    </div>
  </div>
</footer>

<div class="lb" id="lightbox" role="dialog" aria-modal="true" aria-label="Screenshot viewer">
  <button class="lb-close" aria-label="Close">&times;</button>
  <button class="lb-nav prev" aria-label="Previous">&#8249;</button>
  <button class="lb-nav next" aria-label="Next">&#8250;</button>
  <figure><img alt=""><figcaption></figcaption></figure>
</div>

<script src="assets/js/main.js"></script>
</body>
</html>
""".format(email=EMAIL, linkedin=LINKEDIN, github=GITHUB, phone=PHONE,
           phoneraw=PHONE.replace(" ", ""), name=esc(NAME))


def project_card(p, folder, group):
    shots, portrait = shots_for(folder, p["slug"])
    icon = icon_for(p["slug"]) if folder == "projects" else None

    if shots:
        thumbs = "".join(
            '<button type="button" data-src="{s}" data-index="{i}" data-alt="{a}"{cur}>'
            '<img src="{s}" alt="" loading="lazy" decoding="async"></button>'.format(
                s=s, i=i, a=esc(p["name"] + " screenshot " + str(i + 1)),
                cur=' aria-current="true"' if i == 0 else "")
            for i, s in enumerate(shots)
        )
        strip = '<div class="proj-strip">%s</div>' % thumbs if len(shots) > 1 else ""
        shot_html = (
            '<div class="proj-shot{pc}" data-index="0" aria-label="Open screenshots for {n}">'
            '<img src="{first}" alt="{n} screenshot" loading="lazy" decoding="async">{badge}</div>'
        ).format(pc=" portrait" if portrait else "", first=shots[0], n=esc(p["name"]),
                 badge=badge_html(p))
    else:
        strip, shot_html = "", ""

    if folder == "projects":
        meta = '<span class="by">{studio} &middot; {year}</span>'.format(
            studio=esc(p["studio"]), year=esc(p["year"]))
        tags = "".join('<span class="tag">%s</span>' % esc(t) for t in p["platforms"])
        rating = ""
        if p.get("rating"):
            rating = '<span class="proj-rating"><b>{r}</b>&#9733; &middot; {n} ratings</span>'.format(
                r=p["rating"][0], n=p["rating"][1])
        link_text = "View on store"
        data_tags = ' data-tags="%s"' % " ".join(p["tags"])
    else:
        meta = '<span class="by">%s</span>' % esc(p["kicker"])
        tags = "".join('<span class="tag cool">%s</span>' % esc(t) for t in p["stack"])
        rating = '<span class="proj-rating">Playable in browser</span>'
        link_text = "Play it"
        data_tags = ""

    icon_html = ('<img class="proj-icon" src="{i}" alt="" loading="lazy">'.format(i=icon)) if icon else ""

    return """
<article class="proj"{data_tags} data-reveal data-reveal-group="{group}">
  {shot}
  {strip}
  <div class="proj-body">
    <div class="proj-top">
      {icon}
      <div class="proj-title"><h3>{name}</h3>{meta}</div>
    </div>
    <p>{blurb}</p>
    <div class="proj-tags">{tags}</div>
    <div class="proj-foot">
      <a class="proj-link" href="{url}" target="_blank" rel="noopener">{link_text} <span aria-hidden="true">&rarr;</span></a>
      {rating}
    </div>
  </div>
</article>""".format(data_tags=data_tags, group=group, shot=shot_html, strip=strip,
                     icon=icon_html, name=esc(p["name"]), meta=meta, blurb=esc(p["blurb"]),
                     tags=tags, url=p["url"], link_text=link_text, rating=rating)


def badge_html(p):
    if p.get("role") == "zero":
        return '<span class="proj-badge zero">Built 0 &rarr; 1</span>'
    if p.get("role") == "ops":
        return '<span class="proj-badge ops">LiveOps</span>'
    return ""


# ----------------------------------------------------------------------- pages

def build_index():
    studios = ["Eventyr", "Bini Games", "GrandMA Studios", "TEACH & DRAW LTD", "Treehouse Dreams",
               "Big Fish Games", "VGam.es"]
    marquee = "".join("<span>%s</span>" % esc(s) for s in studios * 2)

    experience = [
        {
            "when": "2026 - present &middot; part-time / freelance",
            "role": "AI-first Senior Game Designer",
            "co": "Eventyr",
            "text": "Mobile casual puzzle and brain-teaser games, with the emphasis on how fast an "
                    "idea can be made playable. I build a web prototype with Claude, generate and "
                    "integrate the art with AI tooling, then write the GDD around the thing that "
                    "already runs - documentation that describes a validated build rather than a "
                    "hopeful one.",
            "bullets": [
                "Web prototypes built with Claude, from idea to playable in days",
                "AI-generated graphics produced and integrated into the build",
                "GDDs written from the working prototype, not ahead of it",
                "Testing, bug fixing and playable ad concepts",
            ],
        },
        {
            "when": "2023 - present",
            "role": "Senior Game Designer / Product Owner",
            "co": "Bini Games",
            "text": "Hypercasual and educational games for children, with live operations as the "
                    "main focus. The work runs in a loop: read the current product's metrics, form "
                    "a hypothesis about what is actually limiting them, write the GDD for the "
                    "feature that tests it, ship, and measure. Alongside that I have taken several "
                    "products from the first idea all the way to release.",
            "bullets": [
                "Analysis of live product metrics and hypothesis building",
                "Feature GDDs written against specific metric goals",
                "Full product GDDs from idea to implementation",
                "Feature prototyping with Claude and graphical AI",
            ],
        },
        {
            "when": "2020 - 2023",
            "role": "Head of Game Design",
            "co": "GrandMA Studios",
            "text": "I managed a team of five game designers while running my own project. The "
                    "production pipeline was rebuilt from scratch during my time there, and "
                    "on-time milestone delivery moved from under 10% to roughly 99% - not through "
                    "pressure, but by making workload visible and by fixing the handoffs between "
                    "departments that were quietly eating the schedule.",
            "bullets": [
                "Direct work on new games, from idea through to release",
                "Gantt planning and workload metrics for the whole team",
                "An individual development plan for each designer",
                "Communication set up and maintained between departments",
            ],
        },
        {
            "when": "2020 - 2021",
            "role": "Junior Game Designer &amp; Military Consultant",
            "co": "The Point of no Return / Json",
            "text": "A walking simulator on UE4 about the difficulty Ukrainian soldiers face "
                    "adapting to life in the rear. I wrote documentation and gave feedback at every "
                    "stage; as a former serviceman I also reviewed the script and level design for "
                    "anything that did not ring true. A social project rather than a commercial "
                    "one, supported by the Ukrainian Cultural Foundation.",
            "bullets": [],
            "past": True,
        },
    ]

    tl = ""
    for i, e in enumerate(experience):
        bullets = ""
        if e["bullets"]:
            bullets = "<ul>%s</ul>" % "".join("<li>%s</li>" % b for b in e["bullets"])
        tl += """
    <div class="tl-item{past}" data-reveal data-reveal-group="tl">
      <div class="tl-when">{when}</div>
      <div class="tl-where"><h3>{role}</h3><span class="co">{co}</span></div>
      <p>{text}</p>
      {bullets}
    </div>""".format(past=" past" if e.get("past") else "", when=e["when"],
                     role=e["role"], co=esc(e["co"]), text=esc(e["text"]), bullets=bullets)

    skills = [
        ("Design", ["Core loop &amp; progression design", "Prototype-first GDDs", "LiveOps feature design",
                    "Metrics-driven hypotheses", "Playable ad concepts", "Kids &amp; casual UX"]),
        ("Tools", ["Unity", "Unreal Engine", "Figma", "Miro", "Power BI", "Jira &amp; Confluence"]),
        ("AI", ["Claude for prototyping", "LLM-assisted documentation", "Midjourney &amp; image models",
                "AI asset pipelines"]),
        ("Leading", ["Team of 5 designers", "Gantt &amp; workload planning", "Cross-department comms",
                     "Individual growth plans"]),
    ]
    skill_cards = ""
    for title, items in skills:
        lis = "".join('<span class="tag">%s</span>' % i for i in items)
        skill_cards += """
      <div class="card" data-reveal data-reveal-group="sk">
        <h3>{t}</h3>
        <div class="proj-tags" style="margin-top:1rem">{lis}</div>
      </div>""".format(t=title, lis=lis)

    featured = "".join(project_card(p, "projects", "feat")
                       for p in PROJECTS if p["slug"] in ("rainbow-high", "cats-care", "ws-purrfect-horror"))

    body = """<main id="main">

<section class="hero">
  <div class="shell hero-grid">
    <div>
      <div class="hero-role" data-reveal>
        <span class="dot" aria-hidden="true"></span> Open to senior design roles
        <span aria-hidden="true">&middot;</span> Kyiv, Ukraine
      </div>
      <h1 data-reveal style="--d:60ms">I design games that <span class="grad">reach the store</span>, then keep improving them.</h1>
      <p class="lead" data-reveal style="--d:130ms">
        I am a senior game designer working across casual, kids and puzzle genres, in Unity, Unreal
        and increasingly in the browser. Twelve shipped titles, most of them carried from a blank
        page to release; three years leading a design team; and a current practice built around
        AI-first prototyping - getting an idea playable fast enough that the design document can
        describe something real instead of something hoped for.
      </p>
      <div class="hero-actions" data-reveal style="--d:200ms">
        <a class="btn" href="work.html">See the shipped work <span class="arrow" aria-hidden="true">&rarr;</span></a>
        <a class="btn ghost" href="lab.html">Play the prototypes</a>
      </div>
    </div>
    <aside class="hero-card" data-reveal style="--d:260ms">
      <h4>By the numbers</h4>
      <div class="stat-row"><span class="k">Titles shipped</span><span class="v"><span data-count="12">0</span></span></div>
      <div class="stat-row"><span class="k">Years in game design</span><span class="v"><span data-count="6">0</span><em>+</em></span></div>
      <div class="stat-row"><span class="k">Designers led</span><span class="v"><span data-count="5">0</span></span></div>
      <div class="stat-row"><span class="k">On-time milestones</span><span class="v"><span data-count="99">0</span><em>%</em></span></div>
      <div class="stat-row"><span class="k">Playable prototypes</span><span class="v"><span data-count="6">0</span></span></div>
    </aside>
  </div>
</section>

<div class="marquee" aria-hidden="true"><div class="marquee-track">{marquee}</div></div>

<section class="section">
  <div class="shell">
    <div class="section-head">
      <span class="eyebrow" data-reveal>How I work</span>
      <h2 data-reveal>Prototype first. Document what actually runs.</h2>
      <p class="lead" data-reveal>
        Most design documents are written before anyone knows whether the thing is fun, which is why
        so many of them are quietly abandoned two sprints in. I work the other way round: build the
        smallest playable version first - these days with Claude and AI-generated art, which
        compresses that step from weeks to days - and only then write the GDD, describing the build
        the team can already open. The document becomes a record of decisions that survived contact
        with a real player, and production stops arguing about hypotheticals.
      </p>
    </div>
    <div class="grid four">{skills}</div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="shell">
    <div class="section-head">
      <span class="eyebrow" data-reveal>Experience</span>
      <h2 data-reveal>Six years, four studios, one habit: ship it.</h2>
    </div>
    <div class="tl">{tl}</div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="shell">
    <div class="section-head">
      <span class="eyebrow" data-reveal>Selected work</span>
      <h2 data-reveal>Three of twelve</h2>
      <p data-reveal>A colouring game that found its audience organically, a kids' pet sim, and a
      hidden-object adventure for the PC casual market. The rest are on the shipped work page.</p>
    </div>
    <div class="grid three">{featured}</div>
    <div style="margin-top:2.4rem" data-reveal>
      <a class="btn ghost" href="work.html">All twelve shipped titles <span class="arrow" aria-hidden="true">&rarr;</span></a>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="shell">
    <div class="section-head">
      <span class="eyebrow" data-reveal>Education</span>
      <h2 data-reveal>Not a games degree - and that turned out fine.</h2>
    </div>
    <div class="grid two">
      <div class="card" data-reveal data-reveal-group="edu">
        <h3>Public Administration, MA</h3>
        <p style="margin-top:.5rem">National Pedagogical Dragomanov University &middot; 2018</p>
      </div>
      <div class="card" data-reveal data-reveal-group="edu">
        <h3>Teacher of Italian and English languages and world literature, BA</h3>
        <p style="margin-top:.5rem">National Pedagogical Dragomanov University &middot; 2016</p>
      </div>
    </div>
    <p class="lead" style="margin-top:2rem" data-reveal>
      A teaching background is unusually useful when your players are four years old, and
      administration turned out to be exactly the training a Head of Game Design needs when the real
      problem is not the design at all but the schedule around it. Languages: Ukrainian and Russian
      as native, English at B2.
    </p>
  </div>
</section>

</main>
""".format(marquee=marquee, skills=skill_cards, tl=tl, featured=featured)

    return (head("{n} - {t}".format(n=NAME, t=TITLE),
                 "Senior game designer with 12 shipped titles across casual, kids and puzzle genres. "
                 "AI-first prototyping, LiveOps and design team leadership.",
                 "index.html")
            + nav("index.html") + body + footer())


def build_work():
    counts = {"all": len(PROJECTS)}
    for p in PROJECTS:
        for t in p["tags"]:
            counts[t] = counts.get(t, 0) + 1

    order = [("all", "Everything"), ("zero", "Built 0 &rarr; 1"), ("ops", "LiveOps"),
             ("kids", "Kids"), ("hopa", "Hidden object"), ("puzzle", "Puzzle"),
             ("mobile", "Mobile"), ("pc", "PC")]
    chips = "".join(
        '<button type="button" data-filter="{k}" aria-pressed="{p}">{l}<span class="n">{n}</span></button>'.format(
            k=k, l=l, n=counts.get(k, 0), p="true" if k == "all" else "false")
        for k, l in order if counts.get(k)
    )
    cards = "".join(project_card(p, "projects", "work") for p in PROJECTS)

    body = """<main id="main">
<section class="section" style="padding-bottom:3rem">
  <div class="shell">
    <div class="section-head">
      <span class="eyebrow" data-reveal>Shipped work</span>
      <h2 data-reveal>Twelve titles that made it out the door.</h2>
      <p class="lead" data-reveal>
        Nine of these I carried from the first idea through to release; three were mature products
        where my job was live operations - reading the metrics, forming a hypothesis and shipping
        the feature that tested it. They span mobile kids' games, casual puzzles, hidden-object
        adventures for the PC market and one narrative project on UE4. Every screenshot below comes
        straight from the live store page, and every card links to it.
      </p>
    </div>
    <div class="filters" role="group" aria-label="Filter projects">{chips}</div>
    <div class="grid three">{cards}</div>
  </div>
</section>
</main>
""".format(chips=chips, cards=cards)

    return (head("Shipped work - " + NAME,
                 "Twelve shipped games: kids' mobile titles, casual puzzles, hidden-object "
                 "adventures and a UE4 narrative project.",
                 "work.html")
            + nav("work.html") + body + footer())


def build_lab():
    cards = "".join(project_card(p, "prototypes", "lab") for p in PROTOTYPES)
    body = """<main id="main">
<section class="section" style="padding-bottom:3rem">
  <div class="shell">
    <div class="section-head">
      <span class="eyebrow" data-reveal>Prototypes</span>
      <h2 data-reveal>Six things you can play right now.</h2>
      <p class="lead" data-reveal>
        This is where the prototype-first habit actually lives. Each of these was built to answer one
        specific design question - does this loop hold up, does this mechanic read, can two people of
        very different ages share a session - and each is a real build you can open in a browser
        rather than a mockup. They run on Cloudflare, most were assembled with AI assistance, and
        every screenshot here was captured from the live version. Click any image to page through
        the shots.
      </p>
    </div>
    <div class="grid three">{cards}</div>
  </div>
</section>
</main>
""".format(cards=cards)

    return (head("Prototypes - " + NAME,
                 "Six playable game prototypes built with AI-assisted development and hosted on "
                 "Cloudflare - idle strategy, match-3, FPV drone combat and more.",
                 "lab.html")
            + nav("lab.html") + body + footer())


# ------------------------------------------------------------------------ main

if __name__ == "__main__":
    pages = {"index.html": build_index(), "work.html": build_work(), "lab.html": build_lab()}
    for fname, content in pages.items():
        with open(os.path.join(ROOT, fname), "w", encoding="utf-8") as f:
            f.write(content)
        print("wrote %-12s %6d bytes" % (fname, len(content.encode("utf-8"))))

    # sitemap + robots so the pages are indexable
    urls = "".join("  <url><loc>%s/%s</loc></url>\n" % (SITE, p) for p in pages)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % urls)
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % SITE)
    print("wrote sitemap.xml, robots.txt")
