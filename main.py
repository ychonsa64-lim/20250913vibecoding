import streamlit as st
import pandas as pd
import altair as alt

st.title("🌍 국가별 MBTI 유형 분포 Top 10")

# CSV 업로드
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # MBTI 유형 리스트 (Country 제외)
    mbti_types = [col for col in df.columns if col != "Country"]

    # MBTI 유형 선택
    selected_type = st.selectbox("분석할 MBTI 유형을 선택하세요", mbti_types)

    # 선택한 유형 기준으로 정렬 후 상위 10개 추출
    top10 = df[["Country", selected_type]].sort_values(by=selected_type, ascending=False).head(10)

    # Altair 차트 생성
    chart = (
        alt.Chart(top10)
        .mark_bar()
        .encode(
            x=alt.X(selected_type, title=f"{selected_type} 비율"),
            y=alt.Y("Country", sort="-x", title="국가"),
            tooltip=["Country", selected_type]
        )
        .interactive()
    )

    st.altair_chart(chart, use_container_width=True)

    st.dataframe(top10)
else:
    st.info("📂 CSV 파일을 업로드해주세요.")
