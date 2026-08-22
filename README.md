# Contributing Guide (Read this before touching anything)

## Getting access
1. Send [repo owner] your GitHub username → they'll add you as a Collaborator
2. Accept the invite via the email/notification GitHub sends you
3. You now have push access to the repo

## One-time setup (do this once)

### A. Create your own GitHub Personal Access Token (PAT)
Don't ask for or use anyone else's token — each person needs their own.
1. GitHub → Settings → Developer settings → Personal access tokens → 
   Tokens (classic) → Generate new token
2. Check the `repo` scope box, set expiry (30-90 days), generate
3. **Copy the token immediately** — GitHub only shows it once

### B. Clone the repo into YOUR OWN Colab
1. Open a new Colab notebook (colab.research.google.com)
2. Store your token safely using Colab Secrets (left sidebar → key icon 🔑):
   - Add a secret named `GITHUB_TOKEN`, paste your token as the value
3. Run this in a cell to clone the repo:

```python
from google.colab import userdata
token = userdata.get('GITHUB_TOKEN')
username = "YOUR_GITHUB_USERNAME"
repo_url = f"https://{username}:{token}@github.com/ssrthakkumar/Vision_Based_BrainTumor_Classification_using_DeepLearning.git"
!git clone {repo_url}
%cd Vision_Based_BrainTumor_Classification_using_DeepLearning
!git config user.name "YOUR_GITHUB_USERNAME"
!git config user.email "YOUR_GITHUB_EMAIL"
```

**Never** hardcode your token directly in a cell without Secrets — if you 
accidentally push that cell, your token leaks publicly.

## Daily workflow

### 1. Create your own branch (do this once per feature you're working on)
```bash
!git checkout -b your-name-feature-name
# example: git checkout -b priya-model-training
```
**Do not work directly on `main`.** Your branch = your safe workspace.

### 2. Before starting work each day, sync with main
```bash
!git checkout main
!git pull origin main
!git checkout your-branch-name
!git merge main
```
This pulls in anything teammates already added, so you're not working on 
outdated code.

### 3. Do your work
- Code, experiment, whatever your task is

### 4. Push your progress
```bash
!git add .
!git commit -m "clear message about what you did"
!git push origin your-branch-name
```

### 5. When your feature is done and tested
Tell [repo owner] — they'll review and merge your branch into `main` via a 
Pull Request on GitHub (Compare & pull request button appears automatically 
after you push a new branch).

## Notebook collaboration (important!)

`.ipynb` files cause messy git conflicts when multiple people edit the same 
one simultaneously. So:

- **For live/simultaneous work**: use the shared Google Drive notebook link 
  [paste link here] — this works like Google Docs, real-time, no git needed
- **For git**: only push a notebook once it's in a stable, working state 
  (end of your work session, feature complete) — not mid-edit

## Journal
Each person adds their own daily log under `journal/` (e.g., `journal/day1_priya.md`) 
documenting what you did, what you learned, and problems you hit. Use the 
same format as existing entries.
