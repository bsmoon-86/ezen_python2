import pandas as pd
import os

# 함수 생성 

def list_df(path, end_string):
    # file의 list를 변수로 생성
    file_list = os.listdir(path)
    # 확장자가 end_string과 같은 경우의 리스트만 추출
    file_list2 = []
    # 반복문을 이용하여 end_string과 같은 확장자만 파일만 file_list2에 추가
    # for file in file_list:
    #     if (file.split(".")[-1] == end_string):
    #         file_list2.append(file)
    
    for file in file_list:
        if (file.endswith(end_string)):
            file_list2.append(file)

    # file_list2가 완성이 되면 
    # file_list2를 이용하여 데이터프레임을 결합

    # 비어있는 데이터프레임을 생성 
    result = pd.DataFrame()

    # for문을 이용하여 file_list2 파일들을 비어있는 데이터프레임에 결합
    for file in file_list2:
        print(path + file)
        if(end_string == 'csv'):
            data = pd.read_csv(path + file)
        elif (end_string == 'json'):
            data = pd.read_json(path + file)
        elif (end_string == 'xlsx') | (end_string == 'xls'):
            data = pd.read_excel(path + file)
        
        # result와 data 라는 2개의 데이터프레임을 유니언 결합
        result = pd.concat([result, data], axis=0, ignore_index=True)
    
    return result