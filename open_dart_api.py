from dart_fss.corp import corp_list
import pandas as pd
import dart_fss as dart

api_key = '7f9cec55cd92070c33c36b38d9f21fd0b2dd67ba'
dart.set_api_key(api_key=api_key)

df_code = pd.DataFrame({"회사명":["삼성전자", "이수화학"],
                        "종목코드":['005930', '005950']})
df_code = df_code.reset_index()

corp_list = dart.get_corp_list()
# print(corp_list)

for i in range(len(df_code)):
    s_name = df_code.loc[i, '회사명']
    # 개별회사를 검색한다.
    s = corp_list.find_by_corp_name(s_name, exactly=True)[0]
    # 특정일자 이후 연간 연결재무제표를 불러온다.
    fs = s.extract_fs(bgn_de='20180101')
    # 재무제표 검색 결과를 엑셀파일로 저장한다.(저장위치 : 현재폴더/fsdata)
    fs.save()
    
    
    
    