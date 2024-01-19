import streamlit as st
import pandas as pd
from io import StringIO

# CSV ファイルのパス
csv_file_path = 'tasks.csv'

# CSV ファイルの読み込み
def load_data():
    try:
        return pd.read_csv(csv_file_path, encoding="shift-jis")
    except Exception as e:
        st.error(f"Error loading CSV file: {e}")
        return pd.DataFrame()

# データの保存
def save_data(data):
    try:
        data.to_csv(csv_file_path, index=False)
        st.success("Data saved to CSV")
    except Exception as e:
        st.error(f"Error saving CSV file: {e}")

# メイン関数
def main():
    st.title("CSV File Editor")

    # データの読み込み
    if 'data' not in st.session_state or st.button('Reload Data'):
        st.session_state['data'] = load_data()

    # データの編集
    if st.session_state['data'].empty:
        st.write("No data available to edit.")
    else:
        csv_text = st.text_area("Edit CSV", st.session_state['data'].to_csv(index=False), height=300)
        if csv_text:
            new_data = pd.read_csv(StringIO(csv_text))
            if not new_data.equals(st.session_state['data']):
                st.session_state['data'] = new_data
                save_data(new_data)

if __name__ == '__main__':
    main()
