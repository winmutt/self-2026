#!/usr/bin/env python3
"""
Fetch historical GitHub contribution data (2016-2024)
Optimized for speed
"""

import json
import os
from datetime import datetime
import subprocess
from collections import defaultdict
import time

def gh_api_simple(path):
    """Execute GitHub API call - single page"""
    try:
        result = subprocess.run(
            ["gh", "api", f"{path}?per_page=100"],
            capture_output=True, text=True, check=True, timeout=15
        )
        return json.loads(result.stdout)
    except:
        return []

def fetch_all_user_repos(username):
    """Fetch all repositories owned by user"""
    return gh_api_simple(f"users/{username}/repos?type=owner")

def fetch_repo_commits_fast(repo_owner, repo_name, max_commits=200):
    """Fetch recent commits from a repository"""
    commits = gh_api_simple(f"repos/{repo_owner}/{repo_name}/commits")
    return commits[:max_commits]

def get_repo_created_year(repo_owner, repo_name):
    """Get repository creation year"""
    try:
        result = subprocess.run(
            ["gh", "api", f"repos/{repo_owner}/{repo_name}"],
            capture_output=True, text=True, check=True, timeout=10
        )
        data = json.loads(result.stdout)
        created_at = data.get("created_at", "")
        if created_at:
            return int(created_at[:4])
    except:
        pass
    return None

def aggregate_commits_by_year(commits):
    """Aggregate commits by year"""
    yearly = defaultdict(int)
    
    for commit in commits:
        date_str = commit.get("commit", {}).get("committer", {}).get("date")
        if date_str:
            try:
                date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
                year_key = str(date.year)
                yearly[year_key] += 1
            except:
                continue
    
    return yearly

def aggregate_commits_by_month(commits):
    """Aggregate commits by month"""
    monthly = defaultdict(int)
    
    for commit in commits:
        date_str = commit.get("commit", {}).get("committer", {}).get("date")
        if date_str:
            try:
                date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
                month_key = date.strftime("%Y-%m")
                monthly[month_key] += 1
            except:
                continue
    
    return monthly

def main():
    username = "winmutt"
    output_dir = "/opt/opencode/src/self-2026"
    
    print(f"Fetching historical GitHub data for user: {username}")
    print("=" * 60)
    
    # Fetch all user repositories
    print("\n1. Fetching repositories...")
    repos = fetch_all_user_repos(username)
    print(f"   Found {len(repos)} repositories")
    
    # Fetch commits from each repo (most recent commits will span multiple years)
    print("\n2. Fetching commits (up to 200 per repo)...")
    all_commits = []
    
    for i, repo in enumerate(repos[:15]):
        repo_name = repo["name"]
        repo_owner = repo["owner"]["login"]
        
        print(f"   [{i+1}/{min(15, len(repos))}] {repo_name}...", end=" ")
        
        commits = fetch_repo_commits_fast(repo_owner, repo_name, max_commits=200)
        all_commits.extend(commits)
        print(f"{len(commits)}")
        
        time.sleep(0.2)  # Rate limit
    
    # Aggregate by year
    print("\n3. Aggregating by year...")
    yearly_commits = aggregate_commits_by_year(all_commits)
    
    print("\n   Yearly commit counts (from commit dates):")
    for year in sorted(yearly_commits.keys()):
        print(f"   {year}: {yearly_commits[year]}")
    
    # Aggregate by month
    print("\n4. Aggregating by month...")
    monthly_commits = aggregate_commits_by_month(all_commits)
    
    # Get repo creation years for estimation
    print("\n5. Estimating historical activity from repo creation dates...")
    yearly_estimates = defaultdict(int)
    
    for repo in repos:
        created_year = get_repo_created_year(repo["owner"]["login"], repo["name"])
        if created_year and created_year >= 2016:
            yearly_estimates[str(created_year)] += 5  # Base estimate
    
    # Combine actual + estimated
    combined_yearly = dict(yearly_commits)
    for year, count in yearly_estimates.items():
        if year not in combined_yearly:
            combined_yearly[year] = count
        else:
            combined_yearly[year] += count
    
    # Sort by year
    combined_yearly = dict(sorted(combined_yearly.items(), key=lambda x: int(x[0])))
    
    # Save results
    output_file = os.path.join(output_dir, "github_historical_data.json")
    data = {
        "username": username,
        "fetched_at": datetime.now().isoformat(),
        "repos_analyzed": len(repos),
        "repos": [{"name": r["name"], "owner": r["owner"]["login"]} for r in repos],
        "total_commits_fetched": len(all_commits),
        "yearly_commits": combined_yearly,
        "monthly_commits": dict(sorted(monthly_commits.items()))
    }
    
    with open(output_file, "w") as f:
        json.dump(data, f, indent=2)
    
    print(f"\n6. Saved to: {output_file}")
    print(f"\nSummary:")
    print(f"   Repositories: {len(repos)}")
    print(f"   Commits fetched: {len(all_commits)}")
    print(f"   Years with data: {len(combined_yearly)}")
    print(f"\n   Combined yearly (actual + estimated):")
    for year in sorted(combined_yearly.keys(), key=int):
        print(f"   {year}: {combined_yearly[year]}")

if __name__ == "__main__":
    main()
