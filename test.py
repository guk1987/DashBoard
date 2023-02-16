import pandas as pd
import plotly.graph_objs as go

# 1. wpn.xlsx 파일을 pandas로 읽어온다.
df = pd.read_excel('data/wpn.xlsx')

# 2. plotly 를 이용하여 그래프를 그린다.
fig = go.Figure()

# 2-1. x축 은 "중국 출시" 과거 순 부터 현재 순으로 정리한다.
df_sorted = df.sort_values('중국 출시', ascending=True)

# 2-2. y 축은 "14일 누적 매출" 순으로 정리한다.
df_sorted = df_sorted.sort_values('14일 누적 매출', ascending=False)

# 2-3. 등급이 초월일 경우 노란색으로 표시한다.
df_chowol = df_sorted[df_sorted['등급'] == '초월']
fig.add_trace(go.Bar(x=df_chowol['중국 출시'], y=df_chowol['14일 누적 매출'],
                     name='초월', marker_color='yellow'))

# 2-4. 등급이 에픽일 경우 보라색으로 표시한다.
df_epic = df_sorted[df_sorted['등급'] == '에픽']
fig.add_trace(go.Bar(x=df_epic['중국 출시'], y=df_epic['14일 누적 매출'],
                     name='에픽', marker_color='purple'))

# 2-5. 초월과 에픽 등급을 선택해서 그래프를 그룹으로 on/off 가능하게 처리한다.
fig.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    args=[{'visible': [True, False]}],
                    label='초월',
                    method='update'
                ),
                dict(
                    args=[{'visible': [False, True]}],
                    label='에픽',
                    method='update'
                ),
                dict(
                    args=[{'visible': [True, True]}],
                    label='전체',
                    method='update'
                )
            ]),
            direction='down',
            showactive=True,
            active=2
        )
    ]
)

# 2-6. 값 항목에 마우스 오버할 경우, "이름", "프로모션", "프로모션 연관 무기"가 툴팁으로 제공 되도록 한다.
fig.update_traces(hovertemplate="이름: %{이름}<br>프로모션: %{프로모션}<br>프로모션 연관 무기: %{프로모션 연관 무기}")

# 3. 위 그래프를 html로 저장한다.
fig.write_html("wpn.html")