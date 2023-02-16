import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio
import plotly.express as px
from flask import Flask, render_template, send_from_directory
import os


app = Flask(__name__)


@app.route("/")
def index():
    # "그래프 보기" 버튼을 포함한 HTML 페이지 렌더링
    return render_template("index.html")


@app.route("/graph_wpn")
def graph_wpn():
    # 데이터 프레임 생성
    df = pd.DataFrame(
        {"fruit": ["apples", "oranges", "bananas"], "quantity": [4, 2, 6]}
    )

    # Plotly 그래프 생성
    data = [go.Bar(x=df["fruit"], y=df["quantity"])]
    fig = go.Figure(data=data)

    # 그래프 파일로 저장
    pio.write_html(fig, file="templates/graph_wpn.html", auto_open=False)
    # "graph.html" 파일을 읽어서 HTML 페이지 렌더링
    with open("templates/graph_wpn.html", "r", encoding="utf-8") as f:
        graph_html = f.read()
    return graph_html

@app.route("/graph_mode")
def graph_mode():
    
    # CSV 파일 읽어오기
    df = pd.read_csv('data/20230216_111752.csv')

    # 모드와 날짜별 플레이 시간 비율 데이터프레임 생성
    df_playtime = df.groupby(['mode', '__timestamp']).sum()
    # df_playtime = df_playtime.groupby(level=0).apply(lambda x: 100 * x / float(x.sum()))

    # Plotly로 그래프 그리기
    fig = px.line(df_playtime.reset_index(), x='__timestamp', y='SUM(playtime)', color='mode')

    # 그래프 파일로 저장
    pio.write_html(fig, file="templates/graph_mode.html", auto_open=False)
    # "graph.html" 파일을 읽어서 HTML 페이지 렌더링
    with open("templates/graph_mode.html", "r", encoding="utf-8") as f:
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
