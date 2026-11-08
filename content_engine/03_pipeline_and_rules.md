# LAZYMETA PIPELINE & SYSTEM RULES (v4.0)
## Campaign Folders, Multi-Preset Prompts, Studio Workflow & Scheduler

---

## 1. 🚫 STRICT AGENT RESTRICTION: ZERO IMAGE GENERATION TOOLS
* **NO Image Generation Tools:** The AI agent must **NEVER** attempt to generate, download, or create image files directly. Do not invoke `image-generator` or background subagents for images.
* **The Manual Workflow:** The agent provides **ultra-specific, copy-paste-ready prompts** mapped 1-to-1 to each post. The operator pastes them into **Google AI Flow**, downloads the files, and drops them into **LazyMeta Studio** (`python run.py studio`), which handles C2PA stripping, iPhone EXIF stamping, and auto-renaming.

---

## 2. CAMPAIGN FOLDER STRUCTURE

Organizing by campaign folder keeps each niche cleanly isolated and portable:

```text
lazymeta/
├── campaigns/                   # Store all your 30-day niche campaigns here
│   ├── webdev_mastery/          # Niche A
│   │   ├── captions.json        # Structured post data, copy & multi-preset prompts
│   │   ├── prompts.md           # Visual prompt book (all 3 presets per post)
│   │   └── images/              # 01.jpg, 02.jpg ... 90.jpg (auto-sorted via Studio)
│   └── ecommerce_growth/        # Niche B
│       ├── captions.json
│       ├── prompts.md
│       └── images/
├── content_engine/              # Content generation prompts & guides
├── .env                         # Meta API credentials (strictly gitignored)
└── run.py                       # CLI entry point
```

---

## 3. `captions.json` FORMAT (WITH EMBEDDED PROMPTS & PRESETS)

Using `captions.json` embeds visual prompt metadata right alongside the post copy for instant 1-click copying in LazyMeta Studio:

```json
[
  {
    "id": 1,
    "day": 1,
    "slot": "morning",
    "bucket": "The Contrarian",
    "images": ["01.jpg"],
    "caption": "অধিকাংশ ফ্রিল্যান্সার ভাবে তাদের কাজ না পাওয়ার কারণ 'কমিউনিকেশন স্কিল'। ⚡\nকিন্তু বাস্তব সত্যিটা শুনলে আপনার চোখ কপালে উঠবে...\n\n#FreelanceStrategy #ClientAcquisition",
    "prompt": "High-end editorial vector illustration, modern 2.5D tech graphic with dramatic cinematic lighting, 1:1 aspect ratio. A stylized silhouette developer standing at the edge of an immense floating dark-slate server monolith... Avoid plastic 3D clay, blurry lines, flat white background.",
    "prompt_presets": {
      "hyper_realistic": "Editorial photography, candid shot, 1:1 aspect ratio. A tired but deeply focused young developer sitting by a rain-streaked window at 2:00 AM... Avoid airbrushed plastic skin, cartoon rendering.",
      "tech_vector": "High-end editorial vector illustration, modern 2.5D tech graphic, 1:1 aspect ratio. A stylized silhouette developer standing at the edge of an immense dark-slate server monolith... Avoid cheesy 3D, white cutouts.",
      "face_personal_brand": "High-end commercial personal branding portrait, 1:1 aspect ratio. [CREATOR_FACE: Charismatic founder/creator], sitting confidently in a dark-wood acoustic podcast studio... Avoid plastic skin, fake teeth."
    }
  }
]
```

### Key Fields:
* `"id"`: Sequential post number from 1 to 90.
* `"images"`: Associated filename(s) in `images/` (e.g. `["01.jpg"]`).
* `"caption"`: Full post text with pre-fold hooks, staccato body, takeaway, and hashtags.
* `"prompt"`: The primary prompt that renders in LazyMeta Studio with a 1-click `[ 📋 Copy Prompt for AI Flow ]` button.
* `"prompt_presets"`: The 3 tailored presets (`hyper_realistic`, `tech_vector`, `face_personal_brand`) giving the operator complete creative freedom.

---

## 4. `prompts.md` COMPANION PROMPT BOOK

Alongside `captions.json`, the agent produces `campaigns/<niche>/prompts.md` for easy reading and bulk prompt copying:

```markdown
# [Campaign Name] - Visual Prompt Catalog (01.jpg - 90.jpg)

### Image 01: [Post Title / Hook]
* **Target File**: `images/01.jpg`
* **Day & Slot**: Day 01 - Morning (09:00 AM)
* **Bucket**: The Contrarian
* **Visual Hook Concept**: A lone developer challenging a colossal monolith of legacy code.

#### Preset 1: Hyper-Realistic Editorial Photo
> Editorial photography, candid 85mm portrait, 1:1 square aspect ratio...

#### Preset 2: 2.5D Tech Editorial Vector (Recommended)
> High-end editorial vector illustration, modern 2.5D tech graphic, 1:1 square aspect ratio...

#### Preset 3: Face-Copy / Personal Brand Hero
> High-end commercial personal branding portrait, 1:1 square aspect ratio. [CREATOR_FACE: Founder]...
```

---

## 5. LAZYMETA STUDIO WORKFLOW

```powershell
python run.py studio -f campaigns/<niche_name>
```

1. **Launch Studio**: Starts local Apple VisionOS glassmorphism UI at `http://localhost:5000`.
2. **1-Click Copy**: Click `[ 📋 Copy Prompt for AI Flow ]` on any post card.
3. **Generate in Google AI Flow**: Paste into Google AI Flow and download the result.
4. **Drag & Drop**: Drop the downloaded image right onto the post's dropzone.
5. **Auto-Sort & Anti-AI Sanitization**:
   - Auto-renames to `<id:02d>.jpg`.
   - Strips Google C2PA & SynthID markers.
   - Injects authentic iPhone 15 Pro EXIF + `r1fat.pages.dev` metadata stamp.
   - Updates `captions.json` in real time.
6. **Dispatch Queue**: Once images are ready, click `[ Launch Queue ]` to schedule directly to Meta via Graph API v22.0.
