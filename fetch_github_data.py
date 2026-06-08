#!/usr/bin/env python3
"""
Fetch GitHub contribution data using REST API
"""

import json
import os
from datetime import datetime
import subprocess
from collections import defaultdict
import sys

def gh_api(path, max_items=100):
    """Execute GitHub API call using gh CLI with pagination"""
    all_data = []
    page = 1
    
    while True:
        try:
            full_path = f"{path}&per_page=100&page={page}" if "?" in path else f"{path}?per_page=100&page={page}"
            result = subprocess.run(
                ["gh", "api", full_path],
                capture_output=True, text=True, check=True, timeout=15
            )
            data = json.loads(result.stdout)
            
            if not data or isinstance(data, dict) and "message" in data:
                break
            
            all_data.extend(data)
            
            if len(data) < 100 or len(all_data) >= max_items:
                break
            page += 1
            
        except subprocess.TimeoutExpired:
            print(f"  Timeout on page {page}")
            break
        except subprocess.CalledProcessError as e:
            print(f"  API error on page {page}: {e}")
            break
    
    return all_data[:max_items]

def fetch_user_repos(username):
    """Fetch all repositories for a user"""
    return gh_api(f"users/{username}/repos?type=owner", max_items=50)

def get_repo_commits(repo_owner, repo_name, max_commits=50):
    """Fetch recent commits from a repository"""
    return gh_api(f"repos/{repo_owner}/{repo_name}/commits", max_items=max_commits)

def get_repo_pull_requests(repo_owner, repo_name, max_prs=50):
    """Fetch pull requests from a repository"""
    return gh_api(f"repos/{repo_owner}/{repo_name}/pulls?state=all", max_items=max_prs)

def get_repo_issues(repo_owner, repo_name, max_issues=50):
    """Fetch issues from a repository"""
    issues = gh_api(f"repos/{repo_owner}/{repo_name}/issues?state=all", max_items=max_issues)
    return [i for i in issues if "pull_request" not in i]

def get_user_events(username):
    """Fetch public events for a user"""
    return gh_api(f"users/{username}/events/public", max_items=500)

def aggregate_by_month(events, date_field="created_at"):
    """Aggregate events by month"""
    monthly = defaultdict(int)
    
    for event in events:
        date_str = event.get(date_field)
        if not date_str:
            continue
        
        try:
            date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
            month_key = date.strftime("%Y-%m")
            monthly[month_key] += 1
        except:
            continue
    
    return dict(sorted(monthly.items()))

def main():
    username = "winmutt"
    output_dir = "/opt/opencode/src/self-2026"
    
    print(f"Fetching GitHub data for user: {username}")
    print("=" * 60)
    
    # Fetch user's repositories
    print("\n1. Fetching repositories...")
    repos = fetch_user_repos(username)
    print(f"   Found {len(repos)} repositories")
    
    # Fetch public events
    print("\n2. Fetching public events...")
    events = get_user_events(username)
    print(f"   Found {len(events)} public events")
    
    # Filter events by type
    push_events = [e for e in events if e.get("type") == "PushEvent"]
    pr_events = [e for e in events if e.get("type") == "PullRequestEvent"]
    issue_events = [e for e in events if e.get("type") == "IssuesEvent"]
    pr_review_events = [e for e in events if e.get("type") == "PullRequestReviewEvent"]
    comment_events = [e for e in events if "CommentEvent" in e.get("type", "")]
    
    print(f"   - Push events: {len(push_events)}")
    print(f"   - PR events: {len(pr_events)}")
    print(f"   - Issue events: {len(issue_events)}")
    print(f"   - PR review events: {len(pr_review_events)}")
    print(f"   - Comment events: {len(comment_events)}")
    
    # Aggregate events by month
    print("\n3. Aggregating by month...")
    
    commits_by_month = defaultdict(int)
    for event in push_events:
        date_str = event.get("created_at")
        if date_str:
            try:
                date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
                month_key = date.strftime("%Y-%m")
                commits_by_month[month_key] += event.get("size", len(event.get("payload", {}).get("commits", [])))
            except:
                continue
    
    pr_by_month = aggregate_by_month(pr_events)
    issue_by_month = aggregate_by_month(issue_events)
    all_events_by_month = aggregate_by_month(events)
    
    # Fetch detailed data from repos
    all_commits = []
    all_prs = []
    all_issues = []
    
    print("\n4. Fetching detailed data from repositories...")
    for i, repo in enumerate(repos):
        repo_name = repo["name"]
        repo_owner = repo["owner"]["login"]
        
        print(f"   [{i+1}/{len(repos)}] {repo_name}...", end=" ")
        sys.stdout.flush()
        
        commits = get_repo_commits(repo_owner, repo_name, max_commits=50)
        all_commits.extend(commits)
        
        prs = get_repo_pull_requests(repo_owner, repo_name, max_prs=50)
        all_prs.extend(prs)
        
        issues = get_repo_issues(repo_owner, repo_name, max_issues=50)
        all_issues.extend(issues)
        
        print(f"commits={len(commits)} prs={len(prs)} issues={len(issues)}")
    
    # Combine all activities
    all_activity = {}
    for month, count in commits_by_month.items():
        all_activity[month] = all_activity.get(month, 0) + count
    for month, count in pr_by_month.items():
        all_activity[month] = all_activity.get(month, 0) + count
    for month, count in issue_by_month.items():
        all_activity[month] = all_activity.get(month, 0) + count
    
    # Save results
    output_file = os.path.join(output_dir, "github_real_data.json")
    data = {
        "username": username,
        "fetched_at": datetime.now().isoformat(),
        "repos": [{"name": r["name"], "owner": r["owner"]["login"], "updated_at": r.get("updated_at")} for r in repos],
        "events": {
            "total": len(events),
            "push": len(push_events),
            "pr": len(pr_events),
            "issues": len(issue_events),
            "pr_reviews": len(pr_review_events),
            "comments": len(comment_events)
        },
        "commits_by_month": dict(sorted(commits_by_month.items())),
        "pr_by_month": pr_by_month,
        "issue_by_month": issue_by_month,
        "all_events_by_month": all_events_by_month,
        "all_activity_by_month": dict(sorted(all_activity.items())),
        "detailed": {
            "commits": len(all_commits),
            "prs": len(all_prs),
            "issues": len(all_issues)
        }
    }
    
    with open(output_file, "w") as f:
        json.dump(data, f, indent=2)
    
    print(f"\n5. Saved to: {output_file}")
    print(f"\nSummary:")
    print(f"   Total events: {len(events)}")
    print(f"   Total commits: {len(all_commits)}")
    print(f"   Total PRs: {len(all_prs)}")
    print(f"   Total issues: {len(all_issues)}")
    print(f"   Activity months: {len(all_activity)}")
    
    if all_activity:
        print(f"\nMonthly activity (last 24 months):")
        for month, count in list(all_activity.items())[-24:]:
            print(f"   {month}: {count}")

if __name__ == "__main__":
    main()
