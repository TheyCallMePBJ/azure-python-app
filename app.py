from flask import Flask, render_template_string

app = Flask(__name__)


PAGE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ name }} | Resume</title>
    <style>
        :root { --navy: #1a1a2e; --blue: #1a56a0; --muted: #6b7280; --text: #374151; }
        * { box-sizing: border-box; }
        body { margin: 0; background: #f3f4f6; color: var(--text); font: 10.5pt Arial, sans-serif; line-height: 1.35; }
        .resume { max-width: 860px; margin: 24px auto; padding: 34px 48px; background: #fff; box-shadow: 0 4px 20px #00000012; }
        header { text-align: center; border-bottom: 2px solid var(--blue); padding-bottom: 10px; }
        h1 { margin: 0 0 4px; color: var(--navy); font-size: 29px; letter-spacing: .5px; }
        .contact { color: var(--muted); font-size: 10px; }
        a { color: var(--blue); text-decoration: none; }
        section { margin-top: 13px; }
        h2 { margin: 0 0 8px; padding-bottom: 3px; border-bottom: 1px solid var(--blue); color: var(--blue); font-size: 12px; letter-spacing: .35px; }
        p { margin: 0 0 8px; }
        .row, .project-head { display: flex; justify-content: space-between; gap: 16px; }
        .row strong, .project-head strong { color: var(--navy); }
        .date { color: var(--muted); white-space: nowrap; }
        .entry { margin-bottom: 9px; }
        .skills { display: grid; grid-template-columns: 115px 1fr; gap: 3px 12px; }
        .skills strong { color: var(--navy); }
        .project-head { margin-bottom: 3px; }
        .project-head span, .stack { color: var(--muted); font-size: 9.5px; }
        @media (max-width: 640px) {
            .resume { margin: 0; padding: 24px 20px; }
            .row, .project-head { display: block; }
            .date, .project-head span { display: block; margin-top: 2px; }
            .skills { grid-template-columns: 1fr; gap: 0; }
            .skills strong { margin-top: 5px; }
        }
        @media print {
            body { background: #fff; }
            .resume { max-width: none; margin: 0; padding: 0; box-shadow: none; }
        }
    </style>
</head>
<body>
<main class="resume">
    <header>
        <h1>{{ name|upper }}</h1>
        <div class="contact">
            {{ contact|join(' | ') }} |
            <a href="https://linkedin.com/in/manomaygadiyar">LinkedIn</a> |
            <a href="https://github.com/TheyCallMePBJ">GitHub</a>
        </div>
    </header>

    <section>
        <h2>SUMMARY</h2>
        <p>2nd-year B.Tech AI &amp; ML student at Atlas SkillTech, Mumbai. I build end-to-end ML systems, NLP pipelines, RAG applications, and computer vision tools.</p>
    </section>

    <section>
        <h2>EDUCATION</h2>
        <div class="row">
            <strong>B.Tech, Computer Science with AI &amp; ML | Atlas SkillTech University</strong>
            <span class="date">2024 – 2028</span>
        </div>
    </section>

    <section>
        <h2>TECHNICAL SKILLS</h2>
        <div class="skills">
            <strong>Languages</strong><span>Python, SQL, Java</span>
            <strong>ML / DL</strong><span>scikit-learn, PyTorch, TensorFlow, XGBoost, YOLOv8</span>
            <strong>Web</strong><span>Flask, FastAPI, HTML, CSS, Git, Docker</span>
            <strong>Data</strong><span>Pandas, NumPy, Matplotlib, Seaborn</span>
        </div>
    </section>

    <section>
        <h2>PROJECTS</h2>
        <div class="entry">
            <div class="project-head"><strong>StreamLens — Movie Recommendation Engine</strong><span>Python, FastAPI, scikit-learn</span></div>
            <p>A hybrid recommendation system combining content-based filtering and collaborative filtering.</p>
        </div>
        <div class="entry">
            <div class="project-head"><strong>Call Analyzer — AI Audio Platform</strong><span>Python, Flask, Whisper</span></div>
            <p>A full-stack platform for transcription, sentiment analysis, keyword extraction, and PDF reports.</p>
        </div>
        <div class="entry">
            <div class="project-head"><strong>VisionTrack — Object Detection App</strong><span>Python, YOLOv8, OpenCV</span></div>
            <p>A computer vision app that detects and labels objects in uploaded images.</p>
        </div>
    </section>

    <section>
        <h2>CONTACT</h2>
        <p>Email: <a href="mailto:manomay.gadiyar@gmail.com">manomay.gadiyar@gmail.com</a> | GitHub: <a href="https://github.com/TheyCallMePBJ">TheyCallMePBJ</a></p>
    </section>
</main>
</body>
</html>
"""


@app.get("/")
def resume():
    return render_template_string(
        PAGE,
        name="Manomay Gadiyar",
        contact=["Mumbai, MH", "9322222267", "manomay.gadiyar@gmail.com"],
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
