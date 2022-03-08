import pyupbit
import numpy as np


#ohlcv open high low close volume 으로 당일 시가 고가 저가 종가 거래량에대한 데이터
df = pyupbit.get_ohlcv("KRW-BTC",count=30)  # count=N 지난 N일 동안 ohlcv 를 불러옴
# 변동성 돌파기준 범위 계산 고가 - 저가 *k 
df['range'] = (df['high'] - df['low']) * 0.5
#target (매수가)  range (변동성)칼럼을 한칸씩 밑으로 내림 shift(1)
df['target'] = df['open'] + df['range'].shift(1)

fee = 0.0009 # 수수료
# 수익률 range np.where(조건문 , 참값 , 거짓값) # 
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] - fee,
                     1)
#누적 수익률 계산   누적 곱
df['hpr'] = df['ror'].cumprod()
#하락폭 계산
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
#최대 하락
print("MDD(%): ", df['dd'].max())
#이것들을 xl파일에 저장 
df.to_excel("dd.xlsx")