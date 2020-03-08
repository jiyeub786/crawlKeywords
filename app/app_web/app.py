from flask import Flask, render_template

from source import functions as fn
from source import crawler as cw


app = Flask(__name__)



side_menu = [ { "MENU_NM" : "keyword", "MENU_URL" :"/keyword"}
            , {"MENU_NM" :"news","MENU_URL": "/news"}
            , {"MENU_NM" :"cupang", "MENU_URL":"/cupang"} ]



@app.route('/')
def index():
    return render_template(
                '/main.html'
                 ,side_meus = side_menu
            )

@app.route('/news')
def news():
    return render_template(
                '/main.html'
                 ,section = "news"
            )

@app.route('/cupang')
def cupang():
    return render_template(
                '/main.html'
                 ,section = "cupang"

            )

@app.route('/keyword')
def keyword():
    return render_template(
                 '/main.html'
                 ,section = "keyword"
                 , datas=cw.getResultKeywordFileList()
            )

@app.route('/keyword/list')
def keyword_list():
    return render_template(
                 '/main.html'
                 ,section = "keyword_list"
                 , datas=cw.getResultKeywordFileList()
            )


@app.route('/keyword/list/detail')
def keyword_list_detail():
    return render_template(
                 '/main.html'
                 ,section = "keyword_list_detail"
                 , datas=fn.getFile()
            )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    #app.run(host="0.0.0.0", port="8080")