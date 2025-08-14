# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the nixfred.com personal website hosted on GitHub Pages. It's a static website with no build process required - just pure HTML/CSS/JavaScript that automatically deploys when changes are pushed to the main branch.

## Key Commands

### Publishing Website Updates
- `webpush` or `pushweb`: Update the live website at nixfred.com
  1. Commit all changes to GitHub (including any new files)
  2. Push to main branch for automatic GitHub Pages deployment
  3. Update README.md and CLAUDE.md if needed

### Git Operations
- `COMMIT`: Full commit of all files in the directory to GitHub
- `COMMITALL`: Ensure every file in the entire directory is committed, including all subfolders

### Testing and Verification
- Open files locally in Brave browser to preview changes before pushing
- No build process or npm commands needed - this is pure HTML/CSS/JS
- Changes go live on nixfred.com within minutes of pushing to GitHub

## Project Structure

- `index.html` - Main homepage with personal content and "I'm Still Standing" theme
- `network.html` - Network-related content page  
- `old.html` - Previous version of the website
- `profile.jpg` - Profile image used for favicons and content
- `favicon-*.png`, `favicon.ico` - Site icons in various sizes

## Development Workflow

1. Make changes directly to HTML/CSS/JavaScript files
2. Preview locally in browser
3. Use `webpush` to deploy:
   - Commits all changes
   - Pushes to GitHub main branch
   - GitHub Pages automatically deploys to nixfred.com

## Important Notes

- This is a completely self-contained website with no external dependencies
- No build tools, frameworks, or npm packages required
- All code stays within this repository
- GitHub Pages handles hosting and SSL
- Domain nixfred.com is managed through Cloudflare DNS with CNAME to nixfred.github.io

## Journal Entries

When adding journal entries:
- Use provided text word-for-word without changes
- Format nicely but preserve original wording
- Use today's date if none provided
- Add to appropriate section in index.html

## Website Updates

When updating content:
- Always preview changes locally first
- Maintain the existing dark theme and typography style
- Keep the personal, reflective tone of the content
- Ensure all changes are pushed to the live site with `webpush`