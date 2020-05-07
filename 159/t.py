# 48時間後を予測するのに必要なデータを作成する
i = 0

def make_datas():
    # 持ってるデータの幅
    now = 0
    t_width = 8
    x1 = all_data.loc[now,"MSLP"] # MSLP(t=0)
    x2 = all_data.loc[now, "MSLP"] - all_data.loc[now - min(w_time, 2), "MSLP"] # 過去12時間の中心気圧変化量 = MSLP(t = 0) - MSLP(t = -12)
    x3 = abs(970 - x1) # MSLP　と970hPaの差分の絶対値
    x4 = (x1 - 880) * x2 # (MSLP(t=0) - 880)* 過去12時間の中心気圧変化量
#     x22 = # TWACの時間変化量 = TWAC(t = 48) - TWAC(t = 0)
#     # 時間平均
    x5 = 9999 # RSST VMAX(t = 0)の差の時間平均値
    x6 = 9999 # x5の二乗
    x7 = mean(all_data.loc[now : now + t_width , "THCP"])# TCHP の時間平均値
    x8 = mean([i ** 2 for i in all_data.loc[now:now+t_width, "THCP"]])# TCHPの2乗
    x9 = mean(all_data.loc[now : now + w_time, "T200"])# T200の時間平均値
    x10 = mean(all_data.loc[now: now+w_time, "T250"]) # T250の時間平均値
    x11 = 9999# LONから計算した東西方向の移動速度の時間平均値
    x12 = mean(all_data.loc[now:now+w_time, "RHMD"])# RHMD の時間平均値
    x13 = mean(all_data.loc[now: now+w_time, "EPOS"])# EPOS の時間平均値
    x14 = mean(all_data.loc[now:now +w_time, "SHRD"])# SHRD の時間平均値
    x15 =  mean(all_data.loc[now: now + w_time, "SHGC"])# SHGC の時間平均値
    x16 = mean([i ** 2 for i in all_data.loc[now:now +w_time, "SHRD"]])# SHRDの二乗
    sin = [math.sin(i) for i in all_data.loc[now:now+w_time, "LAT "]]
    shrd = all_data.loc[now:now + w_time, "SHRD"]
    s = 0
    for i in range(len(sin)):
        s += shrd[i] * sin[i]
    x17 = s / len(sin)# SHRD / sin(LAT)
    x18 = mean(all_data.loc[now:now+w_time, "SHRD"] / all_data.loc[now, "VMAX"])# SHRD / VMAX(t = 0)
    x19 = mean((all_data.loc[now, "MSLP"] - 880) * all_data.loc[now: now + w_time, "SHRD"])# (MSLP(t = 0) - 880) * SHRD(t)
    x20 = mean(all_data.loc[now:now + w_time, "Z850"])# Z850
    x21 = mean(all_data.loc[now: now+w_time, "D200"])# D200
    x22 = all_data.loc[now + w_time, "TWAC"] - all_data.loc[now, "TWAC"]
    x23 = mean(all_data.loc[now: now + w_time, "TADV"])# TADV
    x24 = mean(all_data.loc[now:now+w_time, "TGRD"])# TGRD
    x = [x1, x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24]
    return x
