#!/usr/bin/env python3
import os
import random
import subprocess
from datetime import datetime, timedelta

LOG_FILE = "logs/activity.log"
MESSAGES = [
    "fix: resolve edge case in logic",
    "refactor: improve code clarity",
    "docs: update configuration notes",
    "perf: optimize routine",
    "feat: add minor improvement",
    "chore: update dependencies",
    "fix: handle null pointer exception",
    "test: add validation",
    "style: format code",
    "docs: clarify usage",
]

def skip_day():
    """Decide if we should skip today (30% chance)"""
    return random.random() < 0.3

def num_commits():
    """Random number of commits (1-8)"""
    # Bias towards smaller numbers (more realistic)
    if random.random() < 0.5:
        return random.randint(1, 3)
    return random.randint(1, 8)

def generate_log_entry():
    """Generate a realistic log entry"""
    timestamp = datetime.now().isoformat()
    actions = [
        "task completed",
        "process started",
        "operation successful",
        "check passed",
        "sync completed",
        "scan finished",
        "validation ok",
        "update applied"
    ]
    return f"[{timestamp}] {random.choice(actions)}"

def make_commits():
    """Make random number of commits with log modifications"""
    os.makedirs("logs", exist_ok=True)

    commits_count = num_commits()

    for i in range(commits_count):
        # Append to log file
        with open(LOG_FILE, "a") as f:
            f.write(generate_log_entry() + "\n")

        # Stage and commit
        subprocess.run(["git", "add", LOG_FILE], check=True)
        message = random.choice(MESSAGES)
        subprocess.run(["git", "commit", "-m", message], check=True)

        # Small random delay between commits (0-3 seconds)
        if i < commits_count - 1:
            import time
            time.sleep(random.uniform(0, 3))

def main():
    # Configure git user
    subprocess.run(["git", "config", "user.email", "qfedericoba@gmail.com"], check=True)
    subprocess.run(["git", "config", "user.name", "FedericoQuinones"], check=True)

    try:
        make_commits()
        print(f"✓ Made commits successfully")
    except subprocess.CalledProcessError as e:
        print(f"✗ Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
