from flask import Flask, render_template
from youtubesearchpython import VideosSearch  # Обрати внимание на импорт!

app = Flask(__name__)

def get_funny_videos():
    search = VideosSearch("funny shorts OR приколы OR смешное", limit=5)
    results = search.result()["result"]
    videos = []
    for video in results:
        videos.append({
            "title": video["title"],
            "url": f"https://www.youtube.com/embed/{video['id']}"
        })
    return videos

@app.route("/")
def home():
    videos = get_funny_videos()
    return render_template("index.html", videos=videos)

if __name__ == "__main__":
    app.run(debug=True)
