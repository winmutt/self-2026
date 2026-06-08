#!/usr/bin/env python3
"""
Fetch GitHub contribution history using GraphQL API
"""

import json
import os
from datetime import datetime
import subprocess
from collections import defaultdict

def fetch_contribution_calendar(username):
    """Fetch contribution calendar data using GraphQL"""
    query = f'''
    {{
        user(login: "{username}") {{
            contributionsCollection {{
                contributionCalendar {{
                    totalContributions
                    weeks {{
                        contributionDays {{
                            weekday
                            contributionCount
                            date
                        }}
                    }}
                }}
            }}
            repositoriesContributedTo(first: 100, contributionTypes: [COMMIT, ISSUE, PULL_REQUEST, REPOSITORY]) {{
                nodes {{
                    name
                    owner {{ login }}
                }}
            }}
            pullRequests(first: 100) {{
                totalCount
            }}
            issues(first: 100) {{
                totalCount
            }}
        }}
    }}
    '''
    
    result = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={query}"],
        capture_output=True, text=True
    )
    
    if result.returncode != 0:
        print(f"GraphQL error: {result.stderr}")
        return None
    
    return json.loads(result.stdout)

def main():
    username = "winmutt"
    
    print(f"Fetching GitHub contribution calendar for: {username}")
    
    result = fetch_contribution_calendar(username)
    
    if not result or "errors" in result:
        print("Error fetching data")
        if result:
            print(result.get("errors"))
        return
    
    user = result.get("data", {}).get("user", {})
    collection = user.get("contributionsCollection", {})
    
    calendar = collection.get("contributionCalendar", {})
    print(f"\nCalendar data:")
    print(f"  Total contributions: {calendar.get('totalContributions', 'N/A')}")
    print(f"  Weeks: {len(calendar.get('weeks', []))}")
    
    # Aggregate by month
    monthly = defaultdict(int)
    for week in calendar.get("weeks", []):
        for day in week.get("contributionDays", []):
            date_str = day.get("date")
            count = day.get("contributionCount", 0)
            if date_str:
                month_key = date_str[:7]  # YYYY-MM
                monthly[month_key] += count
    
    print(f"\nMonthly contributions (from calendar):")
    for month, count in sorted(monthly.items()):
        print(f"  {month}: {count}")
    
    # Save data
    output_file = "/opt/opencode/src/self-2026/github_graphql_data.json"
    data = {
        "username": username,
        "fetched_at": datetime.now().isoformat(),
        "total_contributions": calendar.get("totalContributions"),
        "monthly_contributions": dict(sorted(monthly.items())),
        "repos_contributed": user.get("repositoriesContributedTo", {}).get("nodes", []),
        "prs_count": user.get("pullRequests", {}).get("totalCount"),
        "issues_count": user.get("issues", {}).get("totalCount")
    }
    
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"\nSaved to: {output_file}")

if __name__ == "__main__":
    main()
