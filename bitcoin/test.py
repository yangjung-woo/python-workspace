import pyupbit

access = "U2xJ8UwYnzclIrbhbr3MxHO6c3WxxZkAYqxJEJLx"          # 본인 값으로 변경
secret = "tDJ4mGOmwzNLCBd6EXseW0gkmFXvlpYxO6mdUOR2"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회 xrt 의 금액 출력
print(upbit.get_balance("KRW"))     # 원화 량