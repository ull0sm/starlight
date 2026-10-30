# Talking points if your teacher asks "how is this different?"

**One-line answer:** Most GitHub drowsiness projects check one thing (eye closure) against one fixed number and play a beep. DriveGuard calibrates to each driver, combines five signals, adapts to lighting, escalates all the way to an emergency contact, and keeps a record of every trip.

| Question | Answer | Where in the code |
|---|---|---|
| Isn't EAR just the standard method? | Yes, EAR is from Soukupová & Čech (CVWW 2016). We use it as one input, not the whole system. | `detectors/face_detectors.py` |
| Why calibrate? | Eye shapes differ, so a fixed 0.25 gives false alarms. We measure the driver's open-eye EAR for 5 s and use 75% of it. | `detectors/calibrator.py` |
| How is the score computed? | Weighted: EAR 0–30, sustained drowsy 25, yawn 20, head off-road 15, phone 10. Tiers are LOW/MODERATE/HIGH/CRITICAL. | `detectors/fatigue_score.py` |
| What happens at night? | Brightness is checked every 15 frames and the thresholds relax (EAR 0.25 → 0.22 → 0.20). | `detectors/night_enhancer.py` |
| What does it do in an emergency? | Drowsy + head tilt for 20 s, or score 75+ for 10 s → stop alert, rest places within 5 km (OpenStreetMap), Gmail + Telegram with location. | `safety/critical_state_monitor.py`, `emergency/emergency_alert.py` |
| Evidence? | 10 s dashcam clip per alert, per-frame CSV, A+–F trip grade. | `safety/incident_recorder.py`, `reports/` |
| Limitations? | No IR camera; IP location is only accurate to ~1–5 km. | README |

**Sources:** NHTSA drowsy driving page (nhtsa.gov/risky-driving/drowsy-driving); AAA Foundation, "Drowsy Driving in Fatal Crashes, United States, 2017–2021"; Soukupová & Čech, "Real-Time Eye Blink Detection using Facial Landmarks", CVWW 2016.
