import pandas as pd
# excel 파일을 다운로드하는거와 동시에 pandas에 load하기
# 흔히 사용하는 df라는 변수는 data frame을 의미합니다.
df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]

df = df.sort_values(['종목코드'], ascending=[True])
df.to_excel("./상장법인목록.xls")

print(df)
#출처: https://wendys.tistory.com/173 [웬디의 기묘한 이야기]