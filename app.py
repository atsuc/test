from flask import Flask
from flask import render_template
from flask import request, stream_with_context, Response
from time import sleep
import os
import glob
import json

app = Flask(__name__)
'''
@app.route('/')
def hello_world():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8" />
            <link rel="stylesheet" href="/static/style.css" />
        </head>
        <body>
            <h1>Hello World!</h1>
        </body>
    </html>
    """

@app.route('/hoge',methods=['GET'])
def hoge():
    return 'hoge!'

@app.route('/hoge',methods=['POST'])
def Hoge():
    return 'Hoge!'
'''

@app.route('/title/<title>')
def title(title):
    return render_template('index.html',title=title)

@app.route('/search')
def search():
    q = request.args.get('q','')
    return q

@app.route('/login',methods=['GET'])
def render_form():
    return render_template('login.html')

@app.route('/login',methods=['POST'])
def login():
    if request.form['username'] and request.form['email']:
        return render_template('check.html',email=request.form['email'],username=request.form['username'])
    else:
        return render_template('error.html')

@app.route('/upload',methods=['GET'])
def render_upload_form():
    return render_template('upload.html')

@app.route('/upload',methods=['POST'])
def upload_file():
    if request.form['name'] and request.form['image']:
        f = request.files['image']
        f.save('static/hoge.png')
        return render_template('result.html',name=request.form['name'])
    else:
        return render_template('error.html')

@app.route('/test',methods=['GET'])
def test():
    def generate():
        # create and return your data in small parts here
        fileList = divide_file('/Users/user/Documents/AItext/horiemon/data_cleaned.csv', 250000)
        for i in fileList:
            yield i
            sleep(1)
    resp = Response(stream_with_context(generate()))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-Type'] = 'text/csv'
    return resp

@app.route('/test2',methods=['GET'])
def test2():
    path = '/Users/user/Documents/vue/vuex-example/vuestate/src'
    # print(glob.glob(os.path.join(path, '*'), recursive=False))
    # dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    # print(dirs)
    resp = Response(json.dumps(createFolderList(path, "/")))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
    # print(createFolderList(path, "/"))

    '''
    print(os.walk('/Users/user/Documents/vue/vuex-example/vuestate/src'))
    for folder, subfolders, files in os.walk('/Users/user/Documents/vue/vuex-example/vuestate/src'):
        print(folder)
        print(subfolders)
        print(files)
    '''
    # return 'aaa'
    # return Response(os.walk('/Users/user/Documents/vue/vuex-example/vuestate/src'))

def partial_content(filePath, start, end):

    partialSize = end - start + 1
    f = open(filePath, "rb")
    f.seek(start)
    data = f.read(partialSize)

    return data

# 指定されたデータサイズでファイルを分割する
def divide_file(filePath, chunkSize):

    readedDataSize = 0
    i = 0
    fileList = []

    # 対象ファイルを開く
    f = open(filePath, "rb")

    # ファイルを読み終わるまで繰り返す
    contentLength = os.path.getsize(filePath)
    while readedDataSize < contentLength:

        # 読み取り位置をシーク
        f.seek(readedDataSize)

        # 指定されたデータサイズだけ読み込む
        data = f.read(chunkSize)

        # 分割ファイルを保存
        saveFilePath = filePath + "." + str(i)
        with open(saveFilePath, 'wb') as saveFile:
            saveFile.write(data)

        # 読み込んだデータサイズの更新
        readedDataSize = readedDataSize + len(data)
        i = i + 1
        # fileList.append(saveFilePath)
        fileList.append(data)

    return fileList

def createFolderList(path, name):
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    json_tmp = {}
    json_tmp["name"] = name
    json_tmp["children"] = []
    for d in dirs:
        l = createFolderList(os.path.join(path, d),d)
        json_tmp["children"].append(l)
    return json_tmp