from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')
@app.route('/', methods=['POST'])
def home_input():
    return render_template('form.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    tcporudp = request.form['tcporudp']
    port = request.form['port']
    ipadress = request.form['ipadress']
    ostype = request.form['ostype']
    if tcporudp=='TCP' and port=='22':
        f = open('./sdnlog', 'w')
        f.write(tcporudp+'   '+port+'   '+ipadress+'   '+ostype)
        f.close()
        #status = os.system('sh ./shelltest.sh')     #在这里写脚本文件，在这个目录下有一个sdnlog文件，里面只有一行信息
                                                     #表示当前需要处理的条目，其中第二个信息是端口号
                                                     #最后一部分信息：1表示要禁止，2表示要解除禁止
        return render_template('home.html', message='Success!')
    return render_template('form.html', message='Bad input', tcporudp=tcporudp)

if __name__ == '__main__':
    app.run(host='0.0.0.0')