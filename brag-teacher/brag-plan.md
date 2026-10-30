# Brag plan: DriveGuard technical showcase (for teacher)
Tone: polished, explanatory. 61.2s. This runs past brag's 25s window on purpose: the user asked for technical depth. Voice: Kokoro af_heart. Music: happy-beats vol 10 at 0.12.

## Storyboard + Voiceover script
1. Title (0–5.8s): "This is DriveGuard, a real-time driver safety system we built in Python."
2. Pipeline (5.8–23.3s): the real architecture diagram, with each stage highlighted as the VO names it. "Each webcam frame passes through a night vision enhancer, then MediaPipe Face Mesh with 478 landmarks. From those we compute eye aspect ratio, mouth aspect ratio, and head pose with solvePnP, while YOLOv8 looks for a phone."
3. Night mode (23.3–30.5s): DAY/DUSK/NIGHT threshold cards. "Every fifteen frames it measures brightness, and switches between day, dusk, and night thresholds automatically."
4. Fatigue score (30.5–37s): weight bars 30/25/20/15/10 + risk tiers. "All signals combine into a weighted fatigue score from zero to one hundred, with four risk tiers."
5. Critical monitor (37–51.8s): conditions A/B + actions. "A critical state monitor has two triggers… sends Gmail and Telegram alerts."
6. Dashboard (51.8–58.6s): real screenshot + Flask/SSE, CSV, history. "A Flask dashboard streams everything live, and each session is saved to CSV for history and graphs."
7. Outro: "That's DriveGuard. Thank you."
