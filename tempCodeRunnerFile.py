def web_open(df,html_path = "output.html"):
    # 将 DataFrame 转换为 HTML 文件
    html_path = html_path
    df.to_html(html_path)
    webbrowser.open(html_path)