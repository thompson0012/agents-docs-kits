---
name: media
description: Use when generating or transcribing media with the harness CLI commands documented here, including images, video, speech, and audio transcription.
---

# Media

Use this skill when the active harness exposes the media CLI commands documented below. Run one media command per bash call, pass JSON parameters as a single argument, and avoid chaining multiple media commands in one call.

If the current harness does not expose these commands, stop and use the available media tooling instead of inventing a wrapper.
## asi-generate-image

Generate images from text prompts. Supports img2img with reference images.

```
asi-generate-image '{"prompt": "A sunset over mountains", "filename": "sunset", "aspect_ratio": "16:9"}'
```

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `prompt` | yes | — | Detailed description of the image |
| `filename` | yes | — | Output filename without extension (adds .png) |
| `aspect_ratio` | no | `"1:1"` | `"1:1"`, `"3:4"`, `"4:3"`, `"9:16"`, `"16:9"` |
| `model` | no | harness default | Harness-supported image model identifier when you need non-default behavior |
| `images` | no | — | List of absolute image paths for img2img (max 10, PNG/JPEG/WebP) |
| `background` | no | — | Background handling mode when the selected image backend supports it |

Good for: photos, illustrations, artistic images, decorative graphics, AI-powered edits.
Bad for: charts, graphs, timelines, infographics — AI hallucinates text/numbers. Use Python scripts for programmatic visuals.

## asi-generate-video

Generate short video clips from text prompts. Optionally animate from a starting frame. For complex video productions (storyboarding, frame chaining, multi-scene), read `video-production/guide.md` in this skill's workspace directory.

```
asi-generate-video '{"prompt": "A wave crashing on shore at sunset", "filename": "wave", "duration": 8}'
```

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `prompt` | yes | — | Scene description including action, camera movement, style |
| `filename` | yes | — | Output filename without extension (adds .mp4) |
| `aspect_ratio` | no | `"16:9"` | `"16:9"` (landscape) or `"9:16"` (portrait) |
| `duration` | no | `8` | Supported values depend on the installed backend; check the command help when you need a non-default duration |
| `model` | no | harness default | Harness-supported video model identifier when you need non-default behavior |
| `image_path` | no | — | Absolute path to starting frame image |

## asi-text-to-speech

Convert text to speech audio. Read `speech/guide.md` for voices, delivery control tags, and multi-speaker dialogue format.

```bash
asi-text-to-speech '{"file_path": "/home/user/workspace/script.txt", "voice": "charon"}'
```

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `file_path` | yes | — | Absolute path to .txt (single speaker) or .json (multi-speaker dialogue) |
| `voice` | no | `"kore"` | Voice name for single-speaker .txt files. Ignored for .json dialogue |
| `model` | no | harness default | Harness-supported text-to-speech model identifier when you need non-default behavior |

## asi-transcribe-audio

Transcribe audio/video files to text with optional speaker diarization and timestamps.

```bash
asi-transcribe-audio '{"file_path": "/home/user/workspace/meeting.mp3"}'
asi-transcribe-audio '{"file_path": "/home/user/workspace/meeting.mp3", "diarize": true}'
```

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `file_path` | yes | — | Absolute path to audio/video file |
| `diarize` | no | `false` | Identify speakers (up to 32) |
| `num_speakers` | no | — | Hint for expected number of speakers (1-32) |
| `timestamps` | no | `"none"` | `"none"` (plain txt), `"word"`, `"character"` (json with timing) |
| `language_code` | no | — | ISO 639-1 code (e.g. `"en"`, `"es"`). Auto-detected if omitted |

Supported formats: mp3, wav, m4a, ogg, flac, mp4, webm. Max 3 GB.