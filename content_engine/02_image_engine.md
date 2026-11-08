# LAZYMETA GOOGLE AI FLOW PROMPT ENGINE (v4.0)
## Multi-Preset Visual Architecture · Zero Tool Overhead · Direct Studio Pipeline

---

## 1. 🚫 STRICT OPERATIONAL RULE: NO DIRECT IMAGE GENERATION

> **CRITICAL AGENT RESTRICTION:**  
> **DO NOT CALL ANY IMAGE GENERATION TOOLS, APIS, OR SUBAGENTS.**  
> Never invoke `image-generator`, never execute image creation scripts, and never attempt to produce image files.  
> The operator manually generates every photo using **Google AI Flow** (powered by Google Imagen 3).  
>
> **Your sole responsibility:** Engineer **ultra-specific, highly detailed, production-ready prompt recipes** optimized specifically for Google AI Flow, combining positive art direction, camera parameters, and negative anti-AI exclusions into unified copy-paste blocks.

---

## 2. GOOGLE AI FLOW PROMPT ENGINEERING FORMULA

Google AI Flow delivers peak visual fidelity when the prompt combines **Scene Drama + Physical Camera/Art Medium + Lighting Geometry + Embedded Anti-AI Exclusions** in a continuous, high-weight semantic structure.

### The Unified Master Prompt Syntax:
```text
[STYLE & MEDIUM: e.g. High-end editorial photography / 2.5D tech vector illustration], [COMPOSITION & ASPECT RATIO: 1:1 square / 4:5 mobile portrait]. [CENTRAL SUBJECT & ACTION: Visual tension, emotional expression, dynamic posture]. [ENVIRONMENT & BACKGROUND: Depth, textures, color palette]. [LIGHTING & ATMOSPHERE: Volumetric rim lighting, catchlights, color temperature]. [TECHNICAL RENDERING: 85mm f/1.4 lens, natural skin pores / razor-sharp vector contours]. [EMBEDDED NEGATIVE EXCLUSIONS: Avoid plastic skin, distorted hands, blurry lines, cheesy 3D, CGI gloss, chaotic background, unreadable text walls].
```

---

## 3. THE 3 OFFICIAL PROMPT PRESETS (PER POST)

For **every single post** in the campaign, you must engineer **3 distinct prompt presets** so the operator can pick the exact visual aesthetic they want in Google AI Flow:

---

### 📸 Preset 1: Hyper-Realistic Editorial Photography (People / Realism / Storytelling)
* **Best Used For:** The War Story, The Relatable Mirror, founder confessions, real-world case studies, and emotional hooks.
* **Core Style:** High-end 35mm or 85mm f/1.4 editorial portrait, cinematic photojournalism, National Geographic / Vanity Fair tech editorial grade.
* **Key Visual Elements:** Authentic human skin textures (micro-pores, natural peach fuzz, subtle freckles), genuine emotional tension, volumetric natural lighting (window daylight or dramatic moody rim light), real physical fabric folds.
* **Negative Exclusions (Inlined):** Suppresses plastic airbrushed skin, wax-figure looks, uncanny valley eyes, distorted extra fingers, and glossy CGI rendering.
* **Blueprint:**
  > Editorial photography, cinematic candid shot, [1:1 square / 4:5 portrait] aspect ratio. [SUBJECT & METAPHOR: e.g. A tired but deeply focused young male developer in a dark hoodie sitting by a rain-streaked window at 2:00 AM, looking at a laptop glowing softly with code, holding a lukewarm mug of coffee with a thoughtful expression]. Authentic natural skin texture with visible micro-pores, natural subtle facial asymmetry, lifelike eyes with realistic window light reflections. Shallow depth of field, shot on 85mm f/1.4 lens, soft creamy bokeh background showing a cozy minimalist modern apartment. Atmospheric moody lighting with warm amber desk lamp and cool blue moonlight edge light. Ultra-sharp focus on face, 8k resolution, authentic color grading. Avoid plastic skin, airbrushing, oversaturated colors, distorted hands, cartoon rendering, CGI gloss, flat flash photography.

---

### 🎨 Preset 2: Modern 2.5D Tech Editorial Vector (Obsidian & Glassmorphism)
* **Best Used For:** The Cheat Sheet, The Epiphany, architecture breakdowns, algorithms, coding tips, and SaaS frameworks.
* **Core Style:** Sleek 2.5D vector tech graphic, dark-mode glassmorphic isometric digital art, Stripe Press / Linear.app / Kurzgesagt editorial aesthetic.
* **Key Visual Elements:** Deep obsidian `#0B0F17` dark slate backdrop, translucent frosted-glass floating panels, blueprint coordinate grids, glowing neon circuit nodes, sharp geometric silhouettes.
* **Micro Tech Badges:** Exactly 1 laser-etched status pill (e.g. `STATUS: 200`, `v2.4`, `LEVERAGE: 10X`, `CORE_ENGINE`).
* **Negative Exclusions (Inlined):** Suppresses photorealistic faces, messy sketch lines, cheap clipart, white cutouts, 3D clay plastic, and unreadable text walls.
* **Blueprint:**
  > High-end editorial vector illustration, modern 2.5D tech graphic with dramatic cinematic lighting, [1:1 square / 4:5 portrait] aspect ratio. [METAPHOR & ACTION: e.g. A sleek stylized silhouette professional in side profile standing on a floating dark-graphite platform, turning a single glowing neon-emerald circuit switch on an immense server monolith]. Clean geometric silhouettes, rich color depth, razor-sharp vector boundaries with translucent frosted-glass floating UI cards. Minimal sharp UI badge reading '[BADGE: e.g. STATUS: 200]'. Atmospheric deep obsidian navy background (#0B0F17) with faint subtle blueprint grid lines and glowing vector particles. High-contrast dual-tone volumetric rim lighting in electric cyan and warm amber accentuating subject contours. Masterpiece digital art, sleek Linear and Stripe editorial tech design aesthetic, hyper-clean vector shapes, zero noise, high visual hook retention. Avoid photorealistic human skin, plastic 3D clay, blurry lines, cluttered background, unreadable messy text walls, cheesy cartoon, flat boring white background.

---

### 👤 Preset 3: Face-Copy / Personal Brand Authority Hero (Creator Self-Promotion)
* **Best Used For:** Personal branding, The Contrarian, authority building, product launches, client acquisition, and founder thought leadership.
* **Core Style:** High-status personal branding portrait, TED Talk / Keynote speaker / executive studio aesthetic, optimized for Google AI Flow face-swapping or reference image uploads.
* **Key Visual Elements:** Placeholder tag `[CREATOR_FACE: Reference photo or upload]`, high-authority posture (confident eye contact, open body language, sharp blazer or signature streetwear), premium minimalist architectural background (sound-treated podcast studio, executive glass boardroom, or dark aesthetic loft).
* **Negative Exclusions (Inlined):** Suppresses stiff unnatural mannequin smiles, distorted collar/clothing, awkward hand poses, cartoon smoothing, and cheap studio backdrops.
* **Blueprint:**
  > High-end commercial personal branding portrait, executive keynote authority aesthetic, [1:1 square / 4:5 portrait] aspect ratio. [CREATOR_FACE: Stylized charismatic founder/creator], sitting forward confidently in an ergonomic dark leather chair, making direct engaging eye contact, dressed in a tailored minimalist charcoal blazer over a black crewneck. Modern high-end podcast studio setting in the background with dark wood acoustic slat panels, warm amber ambient backlighting, and a subtle high-end broadcast microphone slightly out of focus. Crisp commercial lighting with soft beauty dish key light and cool cyan edge rim light carving out shoulders. Shot on Hasselblad 100MP, 85mm lens at f/2.0, razor-sharp eye catchlights, lifelike natural skin tone and texture, premium editorial magazine cover quality. Avoid plastic skin smoothing, fake teeth, uncanny valley stare, awkward fingers, distorted logo badges, harsh flash shadows, cheesy stock photo smile.

---

## 4. STANDARD OUTPUT SCHEMA (FOR BATCHES & CAMPAIGNS)

Whenever you generate content for a post, output the visual prompt section in this exact format:

```markdown
### 🖼️ Visual Prompt Engine -> Post #[ID] (`images: [ID:02d].jpg`)
**Visual Hook Concept:** [1-sentence explanation of the visual dilemma or scroll-stopping tension]

* **Preset 1 [Realistic Photography]:**
  > [Copy-Paste Ready Unified Master Prompt for Google AI Flow]

* **Preset 2 [2.5D Tech Vector]:**
  > [Copy-Paste Ready Unified Master Prompt for Google AI Flow]

* **Preset 3 [Personal Brand Hero / Face-Swap]:**
  > [Copy-Paste Ready Unified Master Prompt for Google AI Flow]

* **Primary Recommended for LazyMeta Studio (JSON `"prompt"`):**
  > [The single best preset chosen for this specific post, ready for 1-click clipboard copying]
```

---

## 5. LAZYMETA STUDIO INTEGRATION

In `campaigns/<niche>/captions.json`, the `"prompt"` field stores the **Primary Recommended Prompt** so that when you run `python run.py studio`:
1. The 1-Click `[ 📋 Copy Prompt for AI Flow ]` button immediately copies the complete engineered master string.
2. The operator pastes it into Google AI Flow, downloads the image, and drops it into the card's dropzone.
3. LazyMeta Studio auto-sanitizes C2PA, stamps `r1fat.pages.dev` + iPhone EXIF, and renames the file to `<id:02d>.jpg`.
