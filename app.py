from flask import Flask, render_template, request, redirect
import pymysql
from sklearn.externals import joblib

app = Flask(__name__)


# html = """
# <!DOCTYPE html>
# <html>
# <body>
#
# <h1>My First Heading</h1>
#
# <p>My first paragraph.</p>
#
# </body>
# </html>
# """


# @app.route("/hello/") # url->http://localhost:8000/hello/
# def index():
#     return "<h1>Hello world</h1>"


@app.route("/")  # url->http://localhost:8000/
def index():
    # return "<h1>Hello world</h1>"
    # return html
    response = render_template("app/index.html")
    print("html data:", type(response), response)
    return response


####  login form ##########
@app.route('/login/', methods=['GET', 'POST'])
def login():
    # print(request.method)
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('psw')
        try:
            with pymysql.connect(user='root', password='pass@123', database='user') as con:
                res = con.execute("select * from user_info where username=%s and password=%s",
                                  args=(username, password))
                # print("Result:", res)
                if res:
                    return redirect('/')
        except pymysql.DatabaseError() as e:
            print("Error:", e)
    return render_template('app/login.html')


@app.route('/ml/simple-linear-regression/', methods=['POST', 'GET'])
def ml_simple_linear_regression():
    if request.method == 'POST':
        area = request.form.get('area')
        # print("Area:", type(area), area)
        result = area.strip().split(",")
        # print("Result:", type(result), result)
        result2 = list(map(lambda x: int(x.strip()), result))
        # print("Result:", type(result2), result2)
        model = joblib.load('ml/simple_lr_reg')
        result = model.predict_target(result2)
        return "Predicted value: <h1>predicted value: " + str(result) + "</h1>"
    return render_template('ml/simple_linear_regression.html')


@app.route('/ml/api/simple-linear-regression/')
def ml_api_simple_linear_regression():
    area = request.args.get('area')
    print("Area:", type(area), area)
    result = area.strip().split(",")
    # print("Result:", type(result), result)
    result2 = list(map(lambda x: int(x.strip()), result))
    # print("Result:", type(result2), result2)
    model = joblib.load('ml/simple_lr_reg')
    result = model.predict_target(result2)
    return "Predicted value: <h1>predicted value: " + str(result) + "</h1>"


if __name__ == '__main__':
    app.run(port=8000, debug=True)
    # app.run(port=80)
