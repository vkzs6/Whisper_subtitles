from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import os
import whisper
import ffmpeg
from datetime import timedelta

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def create_subs(file_path, transcription):
    base_path = os.path.splitext(file_path)[0]
    srt_path = f"{base_path}.srt"
    with open(srt_path, "w", encoding="utf-8") as srtFile:
        for segment in transcription["segments"]:
            startTime = f"0{timedelta(seconds=int(segment['start']))},000"
            endTime = f"0{timedelta(seconds=int(segment['end']))},000"
            text = segment["text"]
            segmentId = segment["id"] + 1
            segment_str = f"{segmentId}\n{startTime} --> {endTime}\n{text}\n\n"
            srtFile.write(segment_str)

def add_subtitles(file_path):
    srt_file = os.path.splitext(file_path)[0] + ".srt"
    output_path = os.path.join(OUTPUT_FOLDER, os.path.basename(file_path).replace(".mp4", "_legendado.mp4"))
    video = ffmpeg.input(file_path)
    audio = video.audio
    (
        ffmpeg
        .concat(
            video.filter("subtitles", srt_file),
            audio,
            v=1,
            a=1
        )
        .output(output_path, vcodec="libx264", acodec="aac", strict="experimental")
        .run()
    )
    return os.path.basename(output_path)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        if file and file.filename.endswith(".mp4"):
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            model = whisper.load_model("small")
            transcription = model.transcribe(filepath)
            create_subs(filepath, transcription)
            output_filename = add_subtitles(filepath)
            return redirect(url_for("view_video", filename=output_filename))
    return render_template("index.html")

@app.route("/outputs/<filename>")
def view_video(filename):
    return render_template("player.html", filename=filename)

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename, as_attachment=True)

@app.route("/file/<filename>")
def serve_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)
