from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import os
import cv2


UPLOAD_FOLDER = '/images/nomal'

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ファイルアップロード待受
@app.route('/upload', methods=['POST'])
def upload():
    print('upload')
    if 'file' not in request.files:
        print('no file')
        return render_template("topPage.html", message="ファイルを指定してください。")

    fs = request.files['file']
    print(fs)

    if '' == fs.filename:
        print('no filename')
        return render_template("topPage.html", message="ファイルを指定してください。")

    # 下記のような情報がFileStorageからは取れる
    print('file_name={}'.format(fs.filename))
    print('content_type={} content_length={}, mimetype={}, mimetype_params={}'.format(
          fs.content_type,
          fs.content_length,
          fs.mimetype,
          fs.mimetype_params))
    print(fs.name)

    # ファイルを保存
    # ファイルの保存ができない
    filename = secure_filename(fs.filename)
    fs.save(os.path.join(app.config['UPLOAD_FOLDER'],fs.filename))
    
    return render_template("topPage.html", message="ファイルのアップロードが完了しました。")


# http://127.0.0.1:5000/
@app.route('/')
def index():
    # トップページを表示させる
    return render_template("topPage.html")


if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)