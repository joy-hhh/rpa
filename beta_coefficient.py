import pandas as pd
import FinanceDataReader as fdr
import xlwings as xw

df_code = pd.DataFrame({'회사명' : ['삼성전자', '이수화학'],
                        '종목코드' : ['005930', '005950']})

start_date = '2019-01-01'
end_date = '2020-12-31'

table_list = []
for i in range(len(df_code)):
    code = df_code.loc[i, '종목코드']
    name = df_code.loc[i, '회사명']
   
    df_stcock = fdr.DataReader(code, start_date, end_date)
    df_kospi = fdr.DataReader('KS11', start_date, end_date)

    df_change = df_stcock['Change']
    df_ks11change = df_kospi['Change']

    df_join = pd.merge(df_change, df_ks11change, how='left', left_on=['Date'], right_on=['Date'], suffixes=('_s', '_k'))

    cov_s_k = df_join.cov().iloc[0]['Change_k']
    var_k = df_join['Change_k'].var()

    # β =  개별자산과 시장 간의 공분산/ 시장분산
    beta = cov_s_k/var_k

    table_list = table_list + [[code, name, start_date, end_date, beta]]

    df_result = pd.DataFrame.from_records(table_list, columns=['개별종목코드', '개별종목명', '시작일자', '종료일자', '베타'])

    # 주가 및 변동 history table 구하기
    df_history = pd.merge(df_stcock, df_kospi, how = 'left', left_on=['Date'], right_on=['Date'], suffixes=('_{}'.format(name), '_코스피지수'))
    
    # 주가 및 변동 history 테이블에서 필요한 칼럼 선택
    df_history = df_history.iloc[:,[3,6,5,11]]
    xw.view(df_history)
    
xw.view(df_result)

