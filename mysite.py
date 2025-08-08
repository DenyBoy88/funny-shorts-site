from flask import Flask, render_template
#from uyts import Search  # импорт твоей библиотеки для поиска
from pytubefix import Search

app = Flask(__name__)

def get_funny_videos():
    s = Search("funny shorts OR приколы OR смешное")
    
    # Проверяем, есть ли атрибут results, иначе пустой список
    results = getattr(s, 'videos', [])
    
    videos = []
    for vid in results[:5]:  # берём максимум 5 видео
        videos.append({
            "title": vid.title,
            "url": f"{vid.watch_url}"
        })
    return videos

@app.route("/")
def home():
    videos = get_funny_videos()
    return render_template("index.html", videos=videos)

if __name__ == "__main__":
    app.run(debug=True)
