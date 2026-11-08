# LAZYMETA BRAND DNA & POSITIONING ENGINE (v1.0)
## Client Metadata Intake, Voice Elevation & `brand.json` Architecture

---

## 1. PURPOSE & VALUE
Before writing 90 posts or crafting visual prompts, the **Brand DNA Engine** intakes raw client information (Facebook Page URL, about page, website, rough founder notes, or competitor examples) and transforms it into an elevated **Brand Bible (`brand_bible.md`)** and machine-readable **`brand.json`**.

This ensures every single post and visual prompt generated across a 30-day campaign sounds like it was written by an insider who understands the brand's customer psychology better than they understand themselves.

---

## 2. THE 6 PILLARS OF BRAND FORENSIC ELEVATION

1. **The Value Transformation Equation:**
   From [Current Painful State] $\rightarrow$ [Desired Dream Outcome] without [Common Friction].
2. **The "Common Enemy" (Antagonist):**
   The broken industry status quo or myth that the brand rallies against.
3. **Audience Psychographics (The 2:00 AM Problem):**
   Deep emotional pain points, hidden fears, and secret ambitions.
4. **Brand Archetype & Personality Matrix:**
   Contrarian Challenger, Elite Technical Mentor, Empathetic War Veteran, or Witty Cultural Disruptor.
5. **The Vocabulary Lexicon:**
   Curated power words vs. banned corporate clichés.
6. **Visual Identity & Color Anchors:**
   Signature color palette, lighting mood, and mapped Google AI Flow preset (Realistic, Vector, or Personal Brand).

---

## 3. FILE ARTIFACT: `campaigns/<niche>/brand.json`

Every campaign folder stores its Brand DNA in `brand.json`:

```json
{
  "brand_name": "Daily Cat Blogs",
  "handle": "@dailycatblogs",
  "website": "r1fat.pages.dev",
  "industry": "Pet Lifestyle & Feline Psychology",
  "mission_statement": "Demystifying cat behavior through aesthetic visual storytelling, warm Scandinavian minimalism, and humorous, science-backed feline body language insights.",
  "target_audience": {
    "persona": "Millennial and Gen-Z cat parents and feline enthusiasts",
    "core_frustrations": [
      "Misinterpreting sudden cat aggression or tail twitches",
      "Wasting money on expensive cat beds their cat completely ignores",
      "Feeling anxious over late-night 3 AM zoomies"
    ],
    "desires": [
      "Building deep, unbreakable trust and affection with their cats",
      "Validating the hilarious, bizarre quirks of daily cat ownership",
      "Decorating with cozy, aesthetic, non-tacky pet accessories"
    ]
  },
  "brand_voice": {
    "archetype": "The Witty Feline Insider",
    "tone": "Warm, cozy, playfully sarcastic, empathetic, authoritative",
    "language": "English (optional creator-grade Bengali)",
    "power_words": ["vulnerability", "feline bear trap", "interdimensional ghosts", "the cat loaf", "trust token"],
    "banned_phrases": ["In this article", "Cats are popular pets", "Did you know that"]
  },
  "the_enemy": "Sterile veterinary manuals and outdated myths claiming cats are cold, unloving, or aloof.",
  "visual_identity": {
    "primary_preset": "hyper_realistic",
    "color_palette": {
      "backdrop": "#0B0F17",
      "primary_accent": "#F59E0B",
      "secondary_rim": "#38BDF8"
    },
    "aesthetic_keywords": "warm Scandinavian interior, light oak wood, golden hour sunbeams, cozy hygge, sharp focus"
  },
  "viral_bucket_angles": {
    "the_contrarian": "Why spending $85 on memory foam cat beds is an evolutionary mistake.",
    "the_epiphany": "The single secret slow blink that signals your cat trusts you with their life.",
    "the_war_story": "The legendary 3:14 AM hallway zoomie incident and the physics behind it.",
    "the_cheat_sheet": "The complete cat tail decoding dictionary for instant mood reading.",
    "the_relatable_mirror": "The Universal Law of Feline Paralysis: why you can never move when a cat sleeps on your lap."
  }
}
```

---

## 4. INTEGRATION INTO LAZYMETA TOOLS

* **`01_text_engine.md` & `lazymeta-caption-generator`**: Reads `brand.json` to immediately craft high-retention hooks and 90 post captions in the elevated brand tone.
* **`02_image_engine.md` & `lazymeta-vector-prompt-engine`**: Adopts the `visual_identity` from `brand.json` to tune color palettes, backgrounds, and presets for Google AI Flow.
* **`LazyMeta Studio`**: Displays the active brand badge in the floating navigation header with quick access to the brand profile.

