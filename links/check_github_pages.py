#!/usr/bin/env python3
"""
Automatically discovers and checks GitHub Pages for nixfred repos
"""

import subprocess
import json
import urllib.request
import urllib.error
from typing import List, Dict

def get_all_repos() -> List[Dict]:
    """Get all repositories for nixfred"""
    cmd = [
        "gh", "api", "users/nixfred/repos", "--paginate",
        "--jq", ".[] | {name: .name, has_pages: .has_pages, description: .description, html_url: .html_url}"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    # Parse the JSON lines output
    repos = []
    for line in result.stdout.strip().split('\n'):
        if line:
            repos.append(json.loads(line))
    return repos

def check_github_pages_url(username: str, repo_name: str) -> bool:
    """Check if a GitHub Pages URL is accessible"""
    if repo_name == f"{username}.github.io":
        url = f"https://{username}.github.io"
    else:
        url = f"https://{username}.github.io/{repo_name}"
    
    try:
        req = urllib.request.Request(url, method='HEAD')
        with urllib.request.urlopen(req, timeout=5) as response:
            return response.status == 200
    except:
        return False

def discover_pages():
    """Main function to discover all active GitHub Pages"""
    print("Discovering GitHub Pages for nixfred...\n")
    
    repos = get_all_repos()
    active_pages = []
    potential_pages = []
    
    for repo in repos:
        repo_name = repo['name']
        
        # Check if Pages is enabled in repo settings
        if repo.get('has_pages'):
            active_pages.append(repo)
            print(f"✓ {repo_name} - Pages ENABLED in settings")
        else:
            # Check if the URL works anyway (sometimes Pages is active but not reflected in API)
            if check_github_pages_url('nixfred', repo_name):
                potential_pages.append(repo)
                print(f"? {repo_name} - Pages URL accessible but not enabled in settings")
    
    print("\n=== ACTIVE GITHUB PAGES ===")
    for repo in active_pages:
        if repo['name'] == 'nixfred.github.io':
            url = "https://nixfred.github.io"
        else:
            url = f"https://nixfred.github.io/{repo['name']}"
        print(f"• {repo['name']}")
        print(f"  URL: {url}")
        if repo.get('description'):
            print(f"  Description: {repo['description']}")
        print()
    
    if potential_pages:
        print("\n=== POTENTIAL PAGES (URL works but not enabled) ===")
        for repo in potential_pages:
            url = f"https://nixfred.github.io/{repo['name']}"
            print(f"• {repo['name']}: {url}")
    
    return active_pages, potential_pages

if __name__ == "__main__":
    active, potential = discover_pages()
    
    # Generate JSON output for the website
    output = {
        "active_pages": active,
        "potential_pages": potential
    }
    
    with open("github_pages.json", "w") as f:
        json.dump(output, f, indent=2)
    
    print(f"\nResults saved to github_pages.json")
    print(f"Found {len(active)} active pages and {len(potential)} potential pages")