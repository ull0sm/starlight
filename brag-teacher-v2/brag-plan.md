# DriveGuard: "How are we different?" (teacher video)

**Goal:** answer the objection "this is a generic GitHub project" with evidence from our own code, plus outside sources.
**Length:** 2:44, landscape 1920x1080. Voice: Kokoro af_heart. Music: happy-beats vol 12 → vol 10 at 0.10 under the voice.
**Animated driver:** a generic driver drawn in SVG (no real person) acts out each detection: blinking, nodding off, yawning, head turn, phone pickup, night mode.

## Argument
1. **Problem.** NHTSA: ~91,000 police-reported drowsy-driving crashes (2017). AAA Foundation: 17.6% of fatal crashes 2017–2021 involved a drowsy driver.
2. **The typical project.** dlib 68 landmarks → EAR (Soukupová & Čech, CVWW 2016) → fixed 0.25 threshold for 20 frames → `alarm.wav`. Examples: byteB8/drowsiness-detection, akash151101/Drowsiness-Detection.
3. **What we do differently** (each backed by a file in this repo):
   1. Per-driver calibration: baseline EAR × 0.75, clamped to [0.18, 0.32], plus head-pose offsets (`detectors/calibrator.py`)
   2. Signal fusion: EAR 30 + drowsy 25 + yawn 20 + head 15 + phone 10 → 0–100 score (`detectors/fatigue_score.py`), with iris gaze as a separate alert (`detectors/gaze_detector.py`)
   3. Light adaptation: DAY/DUSK/NIGHT every 15 frames (`detectors/night_enhancer.py`)
   4. Escalation: voice → critical (20s / 10s) → STOP → OSM rest places → Gmail/Telegram → 10s dashcam clip (`safety/`, `emergency/`)
   5. Memory: per-frame CSV, A+–F scorecard, 2-hour break advisor (EU 561/2006), `--evaluate` offline mode
   6. Hardening: 2-pass YOLO, driver-missing alarm, fail-safe if YOLO can't load (`FIXES.md`)
4. **Side-by-side table**
5. **Honest limits:** no IR camera, IP location ~1–5 km

## Voiceover script
See `build.py` / `composition/assets/vo/s*.wav`; the full text is in `talking-points.md`.
