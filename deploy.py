# -*- coding: utf-8 -*-
"""
Publish the built site to Cloudflare Pages.

`wrangler pages deploy .` would upload build.py, the README and the git dir along
with the site, so this stages only the public files first. Run build.py before
this (or just use `python deploy.py --build`).
"""
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
STAGE = os.path.join(ROOT, ".deploy")
PROJECT = "dmytrobondar"
WRANGLER = r"E:/GravityBridge/game/node_modules/.bin/wrangler.cmd"

PAGES = ["index.html", "lab.html", "work.html", "about.html", "404.html",
         "sitemap.xml", "robots.txt",
         "favicon-32.png", "favicon-192.png", "apple-touch-icon.png"]
DIRS = ["assets"]

if "--build" in sys.argv:
    subprocess.run([sys.executable, os.path.join(ROOT, "build.py")], check=True, cwd=ROOT)

if os.path.isdir(STAGE):
    shutil.rmtree(STAGE)
os.makedirs(STAGE)

n = 0
for f in PAGES:
    src = os.path.join(ROOT, f)
    if os.path.exists(src):
        shutil.copy2(src, os.path.join(STAGE, f))
        n += 1
    else:
        print("  !! missing", f)
for d in DIRS:
    src = os.path.join(ROOT, d)
    if os.path.isdir(src):
        shutil.copytree(src, os.path.join(STAGE, d))
        n += sum(len(files) for _, _, files in os.walk(src))

size = sum(os.path.getsize(os.path.join(dp, f))
           for dp, _, fs in os.walk(STAGE) for f in fs) // 1024
print(f"staged {n} files, {size} KB -> {STAGE}")

env = dict(os.environ, CI="1")
r = subprocess.run([WRANGLER, "pages", "deploy", STAGE,
                    "--project-name", PROJECT, "--branch", "main",
                    "--commit-dirty=true"], env=env, cwd=ROOT)
sys.exit(r.returncode)
