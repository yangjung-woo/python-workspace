import pyupbit
import numpy as np

# 변동성 전략 수익률 계산 후 최적의 k값을 출력
def get_ror(k=0.5):
    df = pyupbit.get_ohlcv("KRW-BTC",count=5)
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    fee = 0.0032
    df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'] - fee,
                         1)

    ror = df['ror'].cumprod()[-2]
    return ror


for k in np.arange(0.1, 1.0, 0.1):
    ror = get_ror(k)
    print("%.1f %f" % (k, ror))