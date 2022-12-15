from flask import Flask, request, render_template, jsonify
import os

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく

@app.route('/toppage',methods=['GET','POST'])
def toppage():
    # URLでhttp://127.0.0.1:5000/uploadを指定したときはGETリクエストとなるのでこっち
    if request.method == 'GET':
        return render_template('topPage.html')
    # formでsubmitボタンが押されるとPOSTリクエストとなるのでこっち
    elif request.method == 'POST':
        file = request.files['image']
        file.save(os.path.join('./images/nomal', file.filename))
        # return redirect(url_for('uploaded_file', filename=file.filename))


# http://127.0.0.1:5000/
@app.route('/')
def index():
    # トップページを表示させる
    return render_template("topPage.html")


if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)