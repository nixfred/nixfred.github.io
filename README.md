# nixfred.com Website

**This repository IS the live website** - [nixfred.com](https://nixfred.com) is served directly from these files via GitHub Pages.

## Overview

This repository is the actual nixfred.com website:
- **These HTML files ARE the website** - no separate codebase or build process
- Hosted directly from this repo via GitHub Pages at nixfred.github.io
- Domain nixfred.com configured in Cloudflare to point to GitHub Pages
- Edited and managed through Claude Code for instant updates
- Changes pushed to main branch go live automatically within minutes

## How It Works

1. **Direct GitHub Pages Hosting**: These HTML/CSS/JS files are served AS-IS from this repository
2. **Cloudflare DNS**: nixfred.com domain has CNAME record pointing to nixfred.github.io
3. **Claude Code Editing**: Connected directly to this repo for live website editing
4. **Instant Deployment**: Push to main = live on nixfred.com (no build, no deploy, just git push)

## Updating the Website

### With Claude Code (Primary Method)
Claude Code is connected to this repository and directly edits the live website:
- Edit any HTML/CSS/JavaScript file = editing the actual website
- Use `webpush` or `pushweb` command to publish changes
- Claude commits and pushes all changes to GitHub
- Website updates live on nixfred.com within 2-3 minutes

### Manual Updates
1. Clone this repository (you're cloning the actual website)
2. Edit the HTML/CSS/JavaScript files (you're editing the website directly)
3. Commit and push to main branch
4. That's it - your changes are live on nixfred.com

## Website Files (These ARE the Website)

- `index.html` - The actual homepage you see at nixfred.com
- `network.html` - Network page at nixfred.com/network.html
- `profile.jpg` - Profile image used on the site
- `favicon.ico`, `favicon-16.png`, `favicon-32.png` - Site icons
- `CLAUDE.md` - Instructions for Claude Code when editing this website

## Tech Stack

- **Pure HTML/CSS/JavaScript** - No frameworks, no build tools
- **GitHub Pages** - Serves these files directly as the website
- **Cloudflare DNS** - Points nixfred.com to GitHub Pages
- **Claude Code** - Primary editing interface for the website

## Domain Configuration

How nixfred.com serves this repository:
- Cloudflare DNS has CNAME record: nixfred.com → nixfred.github.io
- GitHub Pages serves this repository at nixfred.github.io
- SSL certificate automatically provided by GitHub Pages
- Result: These files = Live website at nixfred.com

## Quick Deploy

**With Claude Code:** Just say `webpush` or `pushweb`

**Manually:**
```bash
git add .
git commit -m "Update website"
git push origin main
```

Changes go live at [nixfred.com](https://nixfred.com) in ~2 minutes. No build, no CI/CD, just git push = website updated.