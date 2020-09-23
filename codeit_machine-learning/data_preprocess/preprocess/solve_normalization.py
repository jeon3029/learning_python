# 필요한 도구 임포트
from sklearn import preprocessing
import pandas as pd
# /Users/jeon3029/Documents/workspace/learning_python/codeit_machine-learning/data_preprocess/preprocess/data/liver_patient_data.csv
PATIENT_FILE_PATH = 'data/liver_patient_data.csv'
pd.set_option('display.float_format', lambda x: '%.5f' % x)

# 데이터 파일을 pandas dataframe으로 가지고 온다
liver_patients_df = pd.read_csv(PATIENT_FILE_PATH)
# Normalization할 열 이름들
features_to_normalize = ['Total_Bilirubin','Direct_Bilirubin', 'Alkaline_Phosphotase', 'Alamine_Aminotransferase']

# 코드를 쓰세요

my_df = liver_patients_df[features_to_normalize]

mmscaler = preprocessing.MinMaxScaler()
nor_data = mmscaler.fit_transform(my_df)
# norscaler = preprocessing.StandardScaler()


normalized_df = pd.DataFrame(nor_data,columns=features_to_normalize)
# 체점용 코드
print(normalized_df.describe())
