import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio
from flask import Flask, render_template, send_from_directory
import os


app = Flask(__name__)


@app.route("/")
def index():
    # "그래프 보기" 버튼을 포함한 HTML 페이지 렌더링
    return render_template("index.html")


@app.route("/graph")
def graph():
    # 데이터 프레임 생성
    df = pd.DataFrame(
        {"fruit": ["apples", "oranges", "bananas"], "quantity": [4, 2, 6]}
    )

    # Plotly 그래프 생성
    data = [go.Bar(x=df["fruit"], y=df["quantity"])]
    fig = go.Figure(data=data)

    # 그래프 파일로 저장
    pio.write_html(fig, file="templates/graph.html", auto_open=False)
    # "graph.html" 파일을 읽어서 HTML 페이지 렌더링
    with open("templates/graph.html", "r", encoding="utf-8") as f:
        graph_html = f.read()
    return graph_html


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


if __name__ == "__main__":
    # app.run
    app.run(host="0.0.0.0", port=5000)
