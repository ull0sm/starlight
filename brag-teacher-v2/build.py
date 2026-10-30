"""Builds composition/index.html, timing every scene to its voiceover clip."""
import json
import pathlib
import subprocess

HERE = pathlib.Path(__file__).parent
COMP = HERE / "composition"
LEAD, TAIL = 0.3, 0.6


def dur(p):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", str(p)], capture_output=True, text=True).stdout
    return float(out)


vo = [dur(COMP / f"assets/vo/s{i}.wav") for i in range(12)]
starts, t = [], 0.0
for d in vo:
    starts.append(round(t, 2))
    t += LEAD + d + TAIL
total = round(t + 0.6, 2)

audio = []
for i, s in enumerate(starts):
    audio.append(f'<audio id="vo{i}" data-start="{s + LEAD:.2f}" data-volume="1" src="assets/vo/s{i}.wav"></audio>')
audio.append(f'<audio id="mus1" data-start="0" data-duration="116" data-volume="0.10" data-fade-in="1" data-fade-out="3" src="assets/music/happy-beats-business-moves-vol-12-by-ende-dot-app.mp3"></audio>')
audio.append(f'<audio id="mus2" data-start="114" data-duration="{min(60, total - 114):.2f}" data-volume="0.10" data-fade-in="2" data-fade-out="3" src="assets/music/happy-beats-business-moves-vol-10-by-ende-dot-app.mp3"></audio>')
sfx = [("bong_001", 2, .25), ("card-slide-1", 3, .3), ("error_006", 6, .3), ("card-slide-1", 9, .3), ("impactBell_heavy_000", 11, .35)]
for j, (name, sc, v) in enumerate(sfx):
    audio.append(f'<audio id="sfx{j}" data-start="{starts[sc]:.2f}" data-volume="{v}" src="assets/sfx/{name}.ogg"></audio>')

scenes_attr = []
for i, s in enumerate(starts):
    d = (starts[i + 1] if i + 1 < len(starts) else total) - s
    scenes_attr.append((i, s, round(d, 2)))

tpl = (HERE / "template.html").read_text()
html = (tpl.replace("{{TOTAL}}", str(total))
           .replace("{{AUDIO}}", "\n  ".join(audio))
           .replace("{{STARTS}}", json.dumps(starts))
           .replace("{{VO}}", json.dumps([round(v, 2) for v in vo])))
for i, s, d in scenes_attr:
    html = html.replace(f'data-scene="{i}"', f'data-start="{s}" data-duration="{d}"')
(COMP / "index.html").write_text(html)
print("total", total, "starts", starts)
