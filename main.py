from flask import Flask, request, render_template, jsonify, send_from_directory
import json  # Python標準のJSONライブラリを読み込んで、データの保存等に使用する
import glob  # ファイルの一覧を取得用に使用
import os  # パス操作用に使用

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく

# http://127.0.0.1:5000/
@app.route('/')
def index():
    # トップページを表示させる
    return render_template("test_topPage.html")

@app.route('/uploaded')
def showUploaded():
    # アップロードされた画像を表示させる
    app.config['UPLOAD_FOLDER'] = './images/uploaded'
    files = glob.glob("images/uploaded/*.jpeg")
    print(files)
    paths = []
    for file in files:
        paths.append({
            "filename": os.path.basename(file),
            "url": "/images/uploaded/" + os.path.basename(file)
        })
    return render_template("uploaded.html", target_files=paths)

@app.route('/mosaic')
def showMosaic():
    # モザイク処理された画像を表示させる
    app.config['UPLOAD_FOLDER'] = './images/mosaic'
    files = glob.glob("images/mosaic/*.jpeg")
    print(files)
    paths = []
    for file in files:
        paths.append({
            "filename": os.path.basename(file),
            "url": "/images/mosaic/" + os.path.basename(file)
        })
    return render_template("mosaic.html", target_files=paths)

@app.route('/frame')
def showFrame():
    # 枠で囲われた画像を表示させる
    app.config['UPLOAD_FOLDER'] = './images/frame'
    files = glob.glob("images/frame/*.jpeg")
    print(files)
    paths = []
    for file in files:
        paths.append({
            "filename": os.path.basename(file),
            "url": "/images/frame/" + os.path.basename(file)
        })
    return render_template("frame.html", target_files=paths)

@app.route('/outline')
def showOutline():
    # 輪郭抽出された画像を表示させる
    app.config['UPLOAD_FOLDER'] = './images/outline'
    files = glob.glob("images/outline/*")
    print(files)
    paths = []
    for file in files:
        paths.append({
            "filename": os.path.basename(file),
            "url": "/images/outline/" + os.path.basename(file)
        })
    return render_template("outline.html", target_files=paths)

@app.route('/grayscale')
def showGrayscale():
    # グレースケール化された画像を表示させる
    app.config['UPLOAD_FOLDER'] = './images/gs'
    files = glob.glob("images/gs/*")
    print(files)
    paths = []
    for file in files:
        paths.append({
            "filename": os.path.basename(file),
            "url": "/images/gs/" + os.path.basename(file)
        })
    return render_template("outline.html", target_files=paths)

@app.route('/images/uploaded/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/images/mosaic/<path:filename>')
def mosaic_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/images/frame/<path:filename>')
def frame_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/images/outline/<path:filename>')
def outline_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/images/gs/<path:filename>')
def gs_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)