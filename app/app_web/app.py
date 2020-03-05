from flask import Flask, render_template

app = Flask(__name__)



side_menu = [ { "MENU_NM" : "keyword", "MENU_URL" :"/keyword"}
            , {"MENU_NM" :"news","MENU_URL": "/news"}
            , {"MENU_NM" :"cupang", "MENU_URL":"/cupang"} ]



@app.route('/')
def index():
    return render_template(
                '/index.html'
                 ,side_meus = side_menu
            )

@app.route('/news')
def news():
    return render_template(
                '/section_main.html'
                 ,section = "news"
            )

@app.route('/cupang')
def cupang():
    return render_template(
                '/section_main.html'
                 ,section = "cupang"
            )

@app.route('/keyword')
def keyword():
    return render_template(
                '/section_main.html'
                 ,section = "keyword"
            )




if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")