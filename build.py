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

# Canonical home. The GitHub Pages URL (jotunlegion.github.io) still serves the
# same build as a mirror, but the name people should see is this one.
SITE = "https://dmytrobondar.pages.dev"
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

# Prototypes lead the site, so their order is deliberate: the two most
# finished builds first, the deepest systems piece last.
_PROTO_ORDER = ["warmatch", "gravity-bridge", "floramenta",
                "binitown", "pixeldron", "they-will-make-more"]
PROTOTYPES.sort(key=lambda p: _PROTO_ORDER.index(p["slug"]))

# --------------------------------------------------------------------- helpers

def clean_url(page):
    """Cloudflare Pages serves /about, not /about.html, and 308s the .html form.
    Canonical links and the sitemap use the clean path so neither is a redirect;
    the in-page links stay as .html so the GitHub Pages mirror keeps working."""
    if page == "index.html":
        return ""
    return page[:-5] if page.endswith(".html") else page


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
<link rel="canonical" href="{site}/{clean}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{site}/{clean}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#08090c">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="favicon-192.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta property="og:image" content="{site}/assets/img/life/avatar.webp">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
""".format(title=esc(title), desc=esc(desc), name=esc(NAME), site=SITE,
           page=page, clean=clean_url(page))


def nav(active):
    items = [("index.html", "Home"), ("lab.html", "Prototypes"),
             ("work.html", "Shipped work"), ("about.html", "About me")]
    links = "".join(
        '<a href="{h}"{c}>{t}</a>'.format(h=h, t=t, c=' class="active" aria-current="page"' if h == active else "")
        for h, t in items
    )
    return """<header class="nav">
  <div class="nav-inner">
    <a class="brand" href="index.html">
      <img class="mark" src="assets/img/life/avatar.webp" alt="" width="30" height="30">
      <span>{name}<small>SENIOR GAME DESIGNER</small></span>
    </a>
    <nav class="nav-links" aria-label="Main">{links}<a class="nav-contact-m" href="#" data-contact>Get in touch &rarr;</a></nav>
    <button class="btn nav-cta" type="button" data-contact>Get in touch <span class="arrow" aria-hidden="true">&rarr;</span></button>
    <button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
</header>
""".format(name=esc(NAME), links=links)


def footer():
    return """<footer class="footer">
  <div class="shell">
    <p class="big-cta" data-reveal>Have a game that needs a designer?<br><a href="#" data-contact>Write me a message &rarr;</a></p>
    <div class="footer-grid" style="margin-top:3.2rem">
      <div>
        <h4>About this site</h4>
        <p style="font-size:.93rem;max-width:38ch">Hand-built, no framework, no tracking. Every screenshot is pulled from the live store page or captured from the running prototype.</p>
      </div>
      <div>
        <h4>Pages</h4>
        <div class="footer-list">
          <a href="index.html">Home</a>
          <a href="lab.html">Prototypes</a>
          <a href="work.html">Shipped work</a>
          <a href="about.html">About me</a>
        </div>
      </div>
      <div>
        <h4>Elsewhere</h4>
        <div class="footer-list">
          <a href="#" data-contact>Send a message</a>
          <a href="mailto:{email}">{email}</a>
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

<div class="modal" id="contact" role="dialog" aria-modal="true" aria-labelledby="contact-title">
  <div class="modal-card">
    <button class="modal-close" type="button" aria-label="Close">&times;</button>
    <h3 id="contact-title">Say hello</h3>
    <p>A role, a project, a question about something on this site &mdash; all welcome. Write below and it lands straight in my inbox.</p>
    <form action="https://formsubmit.co/ajax/{email}" method="post" data-mailto="{email}" novalidate>
      <div class="field">
        <label for="cf-name">Your name</label>
        <input id="cf-name" name="name" type="text" autocomplete="name" placeholder="Jane Doe" required>
      </div>
      <div class="field">
        <label for="cf-email">Your email</label>
        <input id="cf-email" name="email" type="email" autocomplete="email" placeholder="jane@studio.com" required>
      </div>
      <div class="field">
        <label for="cf-subject">Subject</label>
        <input id="cf-subject" name="subject" type="text" placeholder="Senior game designer role">
      </div>
      <div class="field">
        <label for="cf-message">Message</label>
        <textarea id="cf-message" name="message" placeholder="Tell me what you are building." required></textarea>
      </div>
      <div class="modal-actions">
        <button class="btn" type="submit">Send message <span class="arrow" aria-hidden="true">&rarr;</span></button>
        <a class="btn ghost" href="mailto:{email}">Use my mail app instead</a>
      </div>
      <p class="form-status" role="status" aria-live="polite"></p>
      <p class="form-note">Or reach me directly: <a href="mailto:{email}">{email}</a> &middot; <a href="tel:{phoneraw}">{phone}</a></p>
    </form>
  </div>
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
        data_tags = ' data-tags="%s"' % " ".join(p["tags"])
        # Shipped titles keep the quiet footer: a store link plus the rating.
        foot = """<div class="proj-foot">
      <a class="proj-link" href="{url}" target="_blank" rel="noopener">View on store <span aria-hidden="true">&rarr;</span></a>
      {rating}
    </div>""".format(url=p["url"], rating=rating)
    else:
        meta = '<span class="by">%s</span>' % esc(p["kicker"])
        tags = "".join('<span class="tag cool">%s</span>' % esc(t) for t in p["stack"])
        data_tags = ""
        # A prototype's whole footer is the play button - full width, bright,
        # and the tap target is the entire bar rather than a line of small text.
        foot = """<a class="proj-play" href="{url}" target="_blank" rel="noopener"
       aria-label="Play {name} in your browser">
      <span class="proj-play-word">PLAY</span>
      <span class="proj-play-sub">Opens in your browser <span aria-hidden="true">&rarr;</span></span>
    </a>""".format(url=p["url"], name=esc(p["name"]))

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
    {foot}
  </div>
</article>""".format(data_tags=data_tags, group=group, shot=shot_html, strip=strip,
                     icon=icon_html, name=esc(p["name"]), meta=meta, blurb=esc(p["blurb"]),
                     tags=tags, foot=foot)


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

    featured_proto = "".join(project_card(p, "prototypes", "hp")
                             for p in PROTOTYPES[:3])
    featured_work = "".join(
        project_card(p, "projects", "feat")
        for p in PROJECTS if p["slug"] in ("rainbow-high", "cats-care", "ws-purrfect-horror"))

    body = """<main id="main">

<section class="hero">
  <div class="shell hero-grid">
    <div>
      <div class="hero-role" data-reveal>
        <span class="dot" aria-hidden="true"></span> Open to senior design roles
        <span aria-hidden="true">&middot;</span> Kyiv, Ukraine
      </div>
      <h1 data-reveal style="--d:60ms">I build <span class="grad">playable prototypes</span>, then design around what works.</h1>
      <p class="lead" data-reveal style="--d:130ms">
        I am a game designer with experience across casual genres, puzzle games, indie projects,
        Unity and UE4, focused these days on AI-driven prototyping, LiveOps, team organisation and
        metrics-based product improvement. At Bini Games I have worked on a run of kids' titles,
        including Rainbow High Colouring, which entered the Top 50 new successful kids' games and
        reached hundreds of thousands of downloads across Android and iOS with a strong focus on
        organic traffic. As Head of Game Designers at GrandMA Studios I managed a team of five
        designers and rebuilt the production pipeline from scratch, improving on-time milestone
        delivery from under 10% to roughly 99%. I work prototype-first: the GDD is built around a
        validated prototype, which is what makes documentation practical and production-ready
        rather than aspirational.
      </p>
      <div class="hero-actions" data-reveal style="--d:200ms">
        <a class="btn btn-xl" href="lab.html">Play the prototypes <span class="arrow" aria-hidden="true">&rarr;</span></a>
        <a class="btn ghost" href="work.html">See the shipped work</a>
      </div>
    </div>
    <div class="hero-side">
    <figure class="hero-photo" data-reveal style="--d:200ms">
      <img src="assets/img/life/portrait.webp" alt="Dmytro Bondar" width="600" height="750" loading="eager" decoding="async">
      <figcaption>Dmytro Bondar &middot; Kyiv</figcaption>
    </figure>
    <aside class="hero-card" data-reveal style="--d:300ms">
      <h4>By the numbers</h4>
      <div class="stat-row"><span class="k">Titles shipped</span><span class="v"><span data-count="12">0</span></span></div>
      <div class="stat-row"><span class="k">Playable prototypes</span><span class="v"><span data-count="{proto_n}">0</span></span></div>
      <div class="stat-row"><span class="k">Years in game design</span><span class="v"><span data-count="6">0</span><em>+</em></span></div>
      <div class="stat-row"><span class="k">Designers led</span><span class="v"><span data-count="5">0</span></span></div>
      <div class="stat-row"><span class="k">On-time milestones</span><span class="v"><span data-count="99">0</span><em>%</em></span></div>
    </aside>
    </div>
  </div>
</section>

<div class="marquee" aria-hidden="true"><div class="marquee-track">{marquee}</div></div>

<section class="section" style="padding-bottom:0">
  <div class="shell">
    <a class="play-band" href="lab.html" data-reveal>
      <div class="play-band-inner">
        <div class="play-band-text">
          <span class="play-band-eyebrow">Playable right now &mdash; no install, no sign-up</span>
          <h2>Prototypes you can play in your browser, right now</h2>
          <p>
            Every one runs on a real URL, and every one exists to answer a specific design question.
            This is the fastest way to see how I actually work.
          </p>
        </div>
        <span class="play-band-cta">
          <span class="play-word">PLAY</span>
          <span class="play-sub">Tap anywhere on this panel <span aria-hidden="true">&rarr;</span></span>
        </span>
      </div>
    </a>
  </div>
</section>

<section class="section">
  <div class="shell">
    <div class="section-head">
      <span class="eyebrow" data-reveal>The lab</span>
      <h2 data-reveal>A few of them &mdash; open one in a tab</h2>
      <p data-reveal>
        A zombie-apocalypse base builder wrapped around a match-3, a 3D bridge-building puzzle
        runner, and a cognitive-training companion for older players. Each was assembled quickly
        with AI assistance, then tuned by hand until the loop actually held up.
      </p>
    </div>
    <div class="grid three">{featured_proto}</div>
    <div style="margin-top:2.4rem" data-reveal>
      <a class="btn" href="lab.html">See every prototype <span class="arrow" aria-hidden="true">&rarr;</span></a>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="shell">
    <div class="section-head">
      <span class="eyebrow" data-reveal>How I work</span>
      <h2 data-reveal>Prototype first. Document what actually runs.</h2>
      <p class="lead" data-reveal>
        Most design documents are written before anyone knows whether the thing is fun, which is why
        so many of them are quietly abandoned two sprints in. I work the other way round: build the
        smallest playable version first &mdash; these days with Claude and AI-generated art, which
        compresses that step from weeks to days &mdash; and only then write the GDD, describing the
        build the team can already open. The document becomes a record of decisions that survived
        contact with a real player, and production stops arguing about hypotheticals.
      </p>
    </div>
    <div class="grid four">{skills}</div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="shell">
    <div class="section-head">
      <span class="eyebrow" data-reveal>Shipped work</span>
      <h2 data-reveal>Twelve titles that made it to a store</h2>
      <p data-reveal>A colouring game that found its audience organically, a kids' pet sim, and a
      hidden-object adventure for the PC casual market. The other nine are one click away.</p>
    </div>
    <div class="grid three">{featured_work}</div>
    <div style="margin-top:2.4rem" data-reveal>
      <a class="btn ghost" href="work.html">All twelve shipped titles <span class="arrow" aria-hidden="true">&rarr;</span></a>
    </div>
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
      <span class="eyebrow" data-reveal>Education</span>
      <h2 data-reveal>Not a games degree &mdash; and that turned out fine.</h2>
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
      A teaching background is unusually useful when your players are four years old, and public
      administration turned out to be exactly the training a Head of Game Design needs when the real
      problem is not the design at all but the schedule around it. Languages: Ukrainian and Russian
      as native, English at B2. There is a life outside all of this too &mdash;
      <a href="about.html" style="color:var(--accent)">it has its own page</a>.
    </p>
  </div>
</section>

</main>
""".format(marquee=marquee, skills=skill_cards, tl=tl, proto_n=len(PROTOTYPES),
           featured_proto=featured_proto, featured_work=featured_work)

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
      <h2 data-reveal>Things you can play right now.</h2>
      <p class="lead" data-reveal>
        This is where the prototype-first habit actually lives. Each of these was built to answer one
        specific design question - does this loop hold up, does this mechanic read, can two people of
        very different ages share a session - and each is a real build you can open in a browser
        rather than a mockup. They run on Cloudflare, most were assembled with AI assistance, and
        every screenshot on this page was captured from the live version by walking through the
        build: menus, meta screens, mid-run gameplay. Hover the thumbnails under a card to page
        through them, or click any image to open it full size.
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



# ------------------------------------------------------------------ about page

# Each block is one part of the story, with the photos that belong to it.
# `tall` flags portrait-shaped shots so the grid frames them properly.
LIFE = [
    {
        "kicker": "Where it starts",
        "title": "A village on a river bend",
        "shots": ["village-1.webp", "village-2.webp", "village-3.webp",
                  "village-4.webp", "village-5.webp", "village-6.webp"],
        "text": [
            "I grew up in Pechera, a village in the Vinnytsia region that sits on a bend of the "
            "Southern Bug, with a ruined Potocki palace, an old mill, church domes over the cliff "
            "and a river you can swim across if you are stubborn about it. It is genuinely "
            "beautiful, and growing up somewhere beautiful does something to your eye.",
            "I still think that is where my taste came from. Long before I knew what a level was, "
            "I was learning what it feels like to walk through a place that has been arranged well "
            "- where the path takes you, what the landmark on the hill is doing, why you keep "
            "looking back over your shoulder. Every environment I have designed since is a little "
            "bit that riverbank."
        ],
    },
    {
        "kicker": "The soft part",
        "title": "Nature, and a weakness for animals",
        "shots": ["animals-1.webp", "animals-2.webp"],
        "tall": True,
        "text": [
            "I love being outdoors and I have never once managed to walk past a cat. This is not a "
            "hobby so much as a permanent condition - if there is a kitten in the yard, that is "
            "where I will be for the next twenty minutes.",
            "It is not unrelated to the work, either. Designing a kitten daycare for four-year-olds "
            "is much easier when you actually like the animal you are asking a child to look after, "
            "and when you already know exactly how a cat behaves when it does not want to be picked "
            "up."
        ],
    },
    {
        "kicker": "Being useful",
        "title": "Two years on the water as a rescuer",
        "shots": ["rescue-1.webp", "rescue-2.webp"],
        "text": [
            "It mattered to me to do something with an obvious point to it, so I worked as a "
            "lifeguard and rescuer. It is a strange job: long stretches of watching nothing happen, "
            "punctuated by minutes where everything depends on whether you noticed early enough and "
            "whether the drill is in your hands rather than your head.",
            "I was recognised for it more than once, including a commendation from the Mayor of "
            "Kyiv. What I actually took from it is less presentable than a certificate: how a team "
            "behaves under pressure, why procedure exists, and how much of a good outcome is "
            "decided long before the emergency, in the boring preparation nobody photographs."
        ],
    },
    {
        "kicker": "Service",
        "title": "Lieutenant, infantry platoon commander",
        "shots": ["army-1.webp", "army-2.webp"],
        "text": [
            "I served as an officer in the Ukrainian infantry, a platoon commander with the rank of "
            "lieutenant, and took part directly in combat operations - both as a soldier and "
            "responsible for the people under my command. That second part is the one that changed "
            "me. Being answerable for other people's lives rearranges your sense of what a "
            "difficult decision actually is.",
            "It also permanently altered how I read a plan. I am the person on the team who asks "
            "what happens when this goes wrong, who is responsible when it does, and whether the "
            "instruction still makes sense to someone tired and under pressure. Deadlines are not "
            "nothing, but I have a fairly calibrated idea of where they sit."
        ],
    },
    {
        "kicker": "Off the clock",
        "title": "Trips that ask something of you",
        "shots": ["travel-1.webp", "travel-2.webp"],
        "video": "travel.mp4",
        "text": [
            "My preferred holiday is the kind you have to earn: mountains, a heavy pack, weather "
            "that does not care about your plans, and a view at the top that only exists for people "
            "who walked up. The Carpathians get most of my free weekends.",
            "I like the shape of it - a clear goal, a real cost, and a payoff you cannot buy. That "
            "is also, more or less, the shape of a well-designed game level."
        ],
    },
    {
        "kicker": "The real passion",
        "title": "I play everything that comes out",
        "shots": [],
        "text": [
            "Video games are the thing I would be doing anyway. I play new releases as they land, "
            "across every genre, partly out of professional curiosity and mostly because I cannot "
            "help myself. Being current is not research to me, it is just Tuesday.",
            "The one that rearranged my world as a child was "
            "<a href=\"https://store.steampowered.com/app/32370/STAR_WARS_Knights_of_the_Old_Republic/\" "
            "target=\"_blank\" rel=\"noopener\">Star Wars: Knights of the Old Republic</a>. It was "
            "the first time a game made me feel that my choices were mine, that a story could turn "
            "on something I decided, and that a world could be big enough to have opinions about. "
            "Everything I have tried to build since has been chasing some version of that feeling."
        ],
    },
    {
        "kicker": "Around a table",
        "title": "Board games, which are just design with the lid off",
        "shots": ["tabletop.webp"],
        "tall": True,
        "text": [
            "I collect and play board games obsessively - Scythe, Arkham Horror, Terraforming Mars, "
            "Fallout, Ticket to Ride and a shelf that has stopped pretending it has room.",
            "They are the most honest design school there is. Every rule is visible, every economy "
            "is on the table, and when something is unbalanced you find out within one evening "
            "because four people tell you to your face. A lot of what I know about pacing and "
            "player turns came from being beaten at cardboard."
        ],
    },
    {
        "kicker": "Reading",
        "title": "Anime, manga, and a shelf of gothic horror",
        "shots": ["books-1.webp", "books-2.webp", "books-3.webp"],
        "text": [
            "I read constantly, and I have a specific weakness: gothic and horror literature. Poe, "
            "Lovecraft, Merritt, Bierce, Crowley - the shelf is almost uniformly black-spined and I "
            "am not sorry about it. Alongside that, plenty of anime and manga, Hannibal and "
            "Fullmetal Alchemist among the volumes that get re-read.",
            "Horror is a genuinely useful genre to study, because it lives or dies on pacing and on "
            "what you withhold. That is exactly the same problem as designing a hidden-object "
            "adventure or the first minute of a kids' game: knowing precisely how much to show, and "
            "when."
        ],
    },
]


def life_shots(block):
    shots = block.get("shots", [])
    if not shots and not block.get("video"):
        return ""
    figs = ""
    for s in shots:
        path = "assets/img/life/" + s
        if not os.path.exists(os.path.join(ROOT, path)):
            continue
        figs += ('<figure><img src="{p}" alt="{a}" loading="lazy" decoding="async"></figure>'
                 .format(p=path, a=esc(block["title"])))
    if block.get("video"):
        vp = "assets/img/life/" + block["video"]
        if os.path.exists(os.path.join(ROOT, vp)):
            figs += ('<figure><video src="{v}" muted loop playsinline controls preload="metadata" '
                     'aria-label="{a}"></video></figure>').format(v=vp, a=esc(block["title"]))
    if not figs:
        return ""
    cls = "shots"
    if block.get("tall"):
        cls += " tall"
    if figs.count("<figure>") == 1:
        cls += " one"
    return '<div class="{c}">{f}</div>'.format(c=cls, f=figs)


def build_about():
    blocks = ""
    for i, blk in enumerate(LIFE, 1):
        media = life_shots(blk)
        paras = "".join("<p>%s</p>" % t for t in blk["text"])
        if media:
            blocks += """
  <div class="story-item" data-reveal>
    <div class="story-text">
      <span class="story-kicker"><span class="num">{n:02d}</span> {k}</span>
      <h3>{t}</h3>
      {p}
    </div>
    {m}
  </div>""".format(n=i, k=esc(blk["kicker"]), t=esc(blk["title"]), p=paras, m=media)
        else:
            blocks += """
  <div class="story-item" data-reveal style="grid-template-columns:1fr">
    <div class="story-text">
      <span class="story-kicker"><span class="num">{n:02d}</span> {k}</span>
      <h3>{t}</h3>
      {p}
    </div>
  </div>""".format(n=i, k=esc(blk["kicker"]), t=esc(blk["title"]), p=paras)

    facts = [
        ("From", "Pechera, Vinnytsia region"),
        ("Based in", "Kyiv, Ukraine"),
        ("Previously", "Rescuer &middot; Infantry officer"),
        ("The game that did it", "KOTOR, age eleven"),
    ]
    fact_html = "".join(
        '<div class="fact" data-reveal data-reveal-group="fx"><span class="k">{k}</span>'
        '<span class="v">{v}</span></div>'.format(k=k, v=v) for k, v in facts)

    body = """<main id="main">

<section class="section" style="padding-bottom:clamp(3rem,6vw,5rem)">
  <div class="shell">
    <div class="section-head" style="max-width:none;margin-bottom:clamp(2rem,4vw,3rem)">
      <span class="eyebrow" data-reveal>About me</span>
      <h2 data-reveal>The parts that are not on the CV.</h2>
    </div>
    <div class="about-hero">
      <div class="about-portrait" data-reveal>
        <img src="assets/img/life/portrait.webp" alt="Dmytro Bondar" loading="eager" decoding="async">
      </div>
      <div data-reveal style="--d:120ms">
        <p class="lead">
          Everything else on this site is about work. This page is about the person doing it, which
          in my case means a village on a river, two years pulling people out of the water, a
          lieutenant's shoulder boards, a great many mountains, and a shelf of gothic horror that
          has quietly taken over one wall.
        </p>
        <p class="lead" style="margin-top:1.1rem">
          None of it is decoration. Design is a job about people - what they will understand, what
          they will feel, what they will do when something goes wrong - and most of what I know
          about people I did not learn at a desk.
        </p>
        <div class="fact-strip">{facts}</div>
      </div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="shell">
    <div class="story">{blocks}</div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="shell">
    <p class="quote" data-reveal>
      If there is a thread running through all of it, it is probably this: I like being useful, I
      like things that are made well, and I have never been able to leave a good system alone
      without taking it apart to see how it works.
    </p>
    <div style="margin-top:2.4rem" data-reveal>
      <a class="btn" href="lab.html">Now go play something <span class="arrow" aria-hidden="true">&rarr;</span></a>
    </div>
  </div>
</section>

</main>
""".format(facts=fact_html, blocks=blocks)

    return (head("About me - " + NAME,
                 "The parts that are not on the CV: a village in Vinnytsia region, two years as a "
                 "rescuer, service as an infantry officer, mountains, board games and gothic horror.",
                 "about.html")
            + nav("about.html") + body + footer())



def build_404():
    body = """<main id="main">
<section class="section">
  <div class="shell" style="max-width:60ch">
    <span class="eyebrow" data-reveal>Error 404</span>
    <h2 data-reveal>This page does not exist.</h2>
    <p class="lead" style="margin-top:1.2rem" data-reveal>
      Which is a shame, because most of the pages here do. Try the prototypes &mdash; that is where
      the interesting things live &mdash; or head back to the start.
    </p>
    <div class="hero-actions" data-reveal>
      <a class="btn btn-xl" href="lab.html">Play the prototypes <span class="arrow" aria-hidden="true">&rarr;</span></a>
      <a class="btn ghost" href="index.html">Back to the home page</a>
    </div>
  </div>
</section>
</main>
"""
    return (head("Page not found - " + NAME,
                 "That page does not exist. Try the prototypes or the home page.",
                 "404.html")
            + nav("") + body + footer())


# ------------------------------------------------------------------------ main

if __name__ == "__main__":
    pages = {"index.html": build_index(), "lab.html": build_lab(),
             "work.html": build_work(), "about.html": build_about(),
             "404.html": build_404()}
    for fname, content in pages.items():
        with open(os.path.join(ROOT, fname), "w", encoding="utf-8") as f:
            f.write(content)
        print("wrote %-12s %6d bytes" % (fname, len(content.encode("utf-8"))))

    # sitemap + robots so the pages are indexable
    urls = "".join("  <url><loc>%s/%s</loc></url>\n" % (SITE, clean_url(p))
                   for p in pages if p.endswith(".html") and p != "404.html")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % urls)
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % SITE)
    print("wrote sitemap.xml, robots.txt")
