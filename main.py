import re
import requests
from hanspell import spell_checker
import pandas as pd


#100개에 대해서 생성해 봄. 1개의 영상 당 약 30개의 plot

plot_df = pd.read_csv('C:\\Users\\cas\\Desktop\\annotation_info.csv')

plot_ex = plot_df['plot'].dropna().reset_index(drop=True).copy()
plot_ex_100 = plot_ex[0:100].to_list()


num_list = []
target_list = []

#500자 제한
for i, text in enumerate(plot_ex_100):
    if len(text) > 500:
        num_list.append(i)
        target_list.append(text)


combined_results = {}

# 각 문자열을 개별적으로 검사하고 결과를 사전 형태로 변환
for i, text in enumerate(plot_ex_100):

    result = spell_checker.check(text)

    result_summary = {
        'checked': result.checked,
        'errors': result.errors
    }


    combined_results[f"Text_{i + 1}"] = result_summary


checked_df_100 = pd.DataFrame(combined_results).transpose().reset_index(drop=True)

plot_checked_100 = pd.concat((plot_ex[0:100],checked_df_100),axis=1)

plot_checked_100.to_csv('C:\\Users\\cas\\Desktop\\plot_checked_100.csv')