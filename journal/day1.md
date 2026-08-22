# Day 1 — Project Setup, Dataset Exploration & Tooling

**Date:** 21 August 2026

---

## 📌 What I Did

- Selected the **Brain Tumor MRI Dataset** (Kaggle, by Masoud Nickparvar) —  
  4 classes: `glioma`, `meningioma`, `notumor`, `pituitary`

- Downloaded it into Colab via the `kagglehub` library and explored its  
  structure (`Training`/`Testing` folders, image counts, sample visuals)

- Set up Kaggle and GitHub authentication using **Colab Secrets** instead of 
  hardcoding credentials — secrets stay encrypted and never appear in notebook 
  outputs, which matters the moment a notebook is shared or pushed publicly

- Cloned the project repo into Colab using a GitHub **Personal Access Token 
  (PAT)** with `repo` scope, since GitHub deprecated plain password auth for 
  git operations over HTTPS

- Added a `.gitignore` to exclude the dataset, checkpoints, and model weight 
  files (`.h5`, `.pth`) — large binary files bloat git history and datasets 
  often carry redistribution restrictions, so only the download *script* 
  belongs in the repo, not the data itself

---

## 📊 Dataset Findings

### ⚖️ Perfectly Balanced

- **1,400 training / 400 testing images per class**
- **5,600 training images total**
- **1,600 testing images total**

This matters because an imbalanced dataset can make a model look accurate overall while quietly failing on underrepresented classes — balance here means I can skip that fix.

---

### 📐 Inconsistent Image Sizes

Most classes are **512×512**, but `notumor` is **Inconsistent**.

A CNN requires a fixed input shape, so resizing every image to a common size is a **mandatory preprocessing step**, not optional cleanup.

---

## 🔑 Key Technical Lesson

### ☁️ Colab Sessions Are Temporary

Colab sessions are temporary — variables and file paths don't persist reliably across reconnects, and `kagglehub`'s cache path can change between sessions.

**Fix:** Always use the path returned at download time rather than hardcoding one, and re-run notebook cells top-to-bottom after any reconnect.

---

## Why PAT instead of password (GitHub git auth)

- **Password = full account access** (settings, billing, everything). Risky to 
  use in scripts/terminals where it could leak.
- **Git operations = frequent, scriptable HTTPS requests** → easy target for 
  automated password-guessing attacks. GitHub removed password auth for git 
  in Aug 2021 because of this.
- **Password auth can't handle 2FA** — no way to prompt for a 2FA code during 
  a git push/pull, so it was a security gap even before removal.
- **PAT fixes all three**:
  - Scoped (e.g. only `repo` access, not full account)
  - Revocable anytime without changing your actual password
  - Can set an expiry date, so forgotten tokens auto-die

**Analogy**: PAT = valet key (starts the car, opens the trunk) vs password = 
master house key. Same convenience, much smaller risk if lost.

---

## 🚀 Plan for Day 2

Preprocess the dataset:

1. Resize all images to a uniform size
2. Normalize pixel values
3. Split `Training` into train/validation
4. Apply data augmentation

> The reasoning behind each step will be documented as I go.
