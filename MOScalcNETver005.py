import math

# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝　　関数　　＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
def line():
    print("=====================================================")
def line0():
    print("        =============================================")
def keyin(x):
    if x == 0:
        print("電源電圧のVp-p値を入力してください")
        print("単位は[V]です。")
        V = float(input())
        Vdd = V / 2
        Vss = -1 * V / 2
        return Vdd, Vss

    elif x == 1:
        print("利得帯域幅　GB の値を入力してください")
        print("単位は[MHZ]です。")
        GB = float(input())
        GB = GB * 1000000
        return GB

    elif x == 2:
        print("スルーレート　SR の値を入力してください")
        print("単位は[V/us]です。")
        SR = float(input())
        SR = SR * 1000000
        return SR

    elif x == 3:
        print("負荷容量の値 Cl を入力してください　単位は[pF]です。")
        Cl=float(input())
        Cckari=Cl*0.22
        print(Cckari,"[pF]以上の値を、位相補償用キャパシタ　Cc の値として入力してください")
        print("よくわからない場合は 0 と入力してください。")
        Cc_p = float(input())
        if Cc_p == 0:
            Cc_p = math.ceil(Cckari*10)/10
            print("位相補償用キャパシタ　Cc　を",Cc_p,"[pF]に設定しました。")
            wait()
        Cc = Cc_p * 0.000000000001
        return Cc

    elif x == 4:
        print("入力範囲の最小値 VinMin の値を入力してください")
        print("単位は[V]です。")
        VinMin = float(input())
        return  VinMin

    elif x == 5:
        print("入力範囲の最大値　VinMax の値を入力してください")
        print("単位は[V]です。")
        VinMax = float(input())
        return VinMax

    elif x == 6:
        print("Lの基準値を入力してください")
        print("単位は[u]です。")
        L = float(input())
        print("Wの基準値を入力してください")
        print("単位は[u]です。")
        W = float(input())
        print("nmosの閾値　Vtn　の値を入力してください")
        print("単位は[V]です。")
        Vtn = float(input())
        print("pmosの閾値　Vtp　の値を入力してください")
        print("単位は[V]です。")
        Vtp = float(input())
        print("BetaN の値を入力してください")
        BetaN = float(input())
        print("BetaP の値を入力してください")
        BetaP = float(input())
        print("uCox-n の値を入力してください")
        uCoxN = float(input())
        uCoxN = uCoxN * 0.000001
        print("uCox-p の値を入力してください")
        uCoxP = float(input())
        uCoxP = uCoxP * 0.000001
        return L, W, Vtn, Vtp, BetaN, BetaP, uCoxN, uCoxP

    else:
        line()

def keisan0(SR,Cc):
    I5 = SR * Cc
    return I5
def keisan1(Vdd,Vss,GB,Cc,VinMin,VinMax,Vtn,Vtp,BetaN,BetaP,uCoxN,uCoxP,I5):
    LW3 = I5 / (uCoxP * ((Vdd - VinMax) * (Vdd - VinMax) + Vtp - Vtn))
    LW1 = (Cc * Cc * GB * GB * 4 * math.pi * math.pi) / (uCoxN * I5)
    LW5 = (2 * I5) / (uCoxN * (VinMin - Vss - math.sqrt(I5 / (uCoxN * LW1)) - Vtn) * (VinMin - Vss - math.sqrt(I5 / (uCoxN * LW1)) - Vtn))
    LW6 = LW3 * (10 * GB * Cc * 2 * math.pi) / (math.sqrt(uCoxP * LW3 * I5))
    LW7 = (LW5 * LW6 * I5) / (2 * LW3 * LW3 * uCoxP)
    VoutMin = math.sqrt((2 * I5 * LW7 / LW5) / (BetaN * LW7))
    VoutMax = Vdd - math.sqrt((2 * I5 * (LW7 / LW5)) / (BetaP * LW6))
    print("出力最小値、出力最大値は以下のようになりました。")
    print("出力最小値　VoutMin=", VoutMin,"[V]")
    print("出力最大値　VoutMax=", VoutMax,"[V]")
    return LW1, LW3, LW5, LW6, LW7

def rounderro(LW,W):
    x = LW * W
    x = round(x, 2)
    erro=0
    if x < 0.5:
        erro = 1
    return x, erro

def hyouzi(LW,W,M):
    Wx, erro = rounderro(LW, W)
    if erro == 1:
        print("M",M,"のW値が最小デバイスパラメータの値を下回りました")
    else:
        print("MOS",M,"のL＝", L, "[um] W＝", Wx, "[um]")
    return Wx, erro

def filewrite(L,W1,W2,W3,W4,W5,W6,W7,W8,Cc_p,R1,Vdd,GB,SR,Cc,VinMin,VinMax, W, Vtn, Vtp, BetaN, BetaP, uCoxN, uCoxP):
    print("netリストを作成します。netリストのファイル名を入力してください。")
    x = input()
    VDD=Vdd*2
    Cc = Cc * 1000000000000
    f = open('./' + x + '.net', 'w')

    f.write("opamp_netlist\n\n")
    f.write(".param psvoltage=" + str(VDD) + "\n\n")
    f.write(".subckt opamp inm inp out vdd vss\n\n")
    f.write("M1 net1 inm  net2 vss cmosn L=" + str(L) + "u W=" + str(W1) + "u\n")
    f.write("M2 net3 inp  net2 vss cmosn L=" + str(L) + "u W=" + str(W2) + "u\n")
    f.write("M3 net1 net1 vdd  vdd cmosp L=" + str(L) + "u W=" + str(W3) + "u\n")
    f.write("M4 net3 net1 vdd  vdd cmosp L=" + str(L) + "u W=" + str(W4) + "u\n")
    f.write("M5 net2 vb   vss  vss cmosn L=" + str(L) + "u W=" + str(W5) + "u\n")
    f.write("M6 out  net3 vdd  vdd cmosp L=" + str(L) + "u W=" + str(W6) + "u\n")
    f.write("M7 out  vb   vss  vss cmosn L=" + str(L) + "u W=" + str(W7) + "u\n")
    f.write("C1 net3 out " + str(Cc_p) + "p\n\n")
    f.write("R1 vdd  vb " + str(R1) + "k\n")
    f.write("M8 vb   vb   vss  vss cmosn L=" + str(L) + "u W=" + str(W8) + "u\n\n")
    f.write(".ends opamp\n\n\n\n")

    GB=GB/1000000
    SR=SR/1000000
    uCoxN=uCoxN*1000000
    uCoxP=uCoxP*1000000

    f.write("$ このnetリストはオペアンプ自動計算プログラム(MOScalcNETver005.py)によって生成されました。\n")
    f.write("$ 以下にnetリスト生成時の設定数値を示します。\n\n")
    f.write("$ 電源電圧  :  "+str(VDD)+"[V]\n")
    f.write("$ 利得帯域GB  :  "+str(GB)+"[MHz]\n")
    f.write("$ スルーレート  :  "+str(SR)+"[V/us]\n")
    f.write("$ 位相補償キャパシタ容量  :  "+str(Cc)+"[pF]\n")
    f.write("$ 入力範囲の最小値  :  "+str(VinMin)+"[V]\n")
    f.write("$ 入力範囲の最大値  :  "+str(VinMax)+"[V]\n")
    f.write("$ Lの基準値  :  "+str(L)+"[um]\n")
    f.write("$ Wの基準値  :  "+str(W)+"[um]\n")
    f.write("$ Nmosの閾値電圧  :  "+str(Vtn)+"[V]\n")
    f.write("$ Pmosの閾値電圧  :  "+str(Vtp)+"[V]\n")
    f.write("$ NmosのBeta  :  "+str(BetaN)+"\n")
    f.write("$ PmosのBeta  :  "+str(BetaP)+"\n")
    f.write("$ Nmosのゲート容量（uCox）  :  "+str(uCoxN)+"\n")
    f.write("$ Pmosのゲート容量（uCox）  :  "+str(uCoxP)+"\n")
    f.close()

    print(x, ".net　というファイルを作成しました。")

def wait():
    i = 0
    while i == 0:
        print("                                            ok : enter")
        i = input()

# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝　　プログラム本体　　＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝

#　　　　数値　入力

line()
print("このツールはオペアンプにおけるLWの値を自動で算出するものです。")
print("これから、必要な数値をお聞きしますので単位に注意しながら入力してください。")
wait()
line()

Vdd, Vss = keyin(0)
GB = keyin(1)
SR = keyin(2)
Cc = keyin(3)
VinMin = keyin(4)
VinMax = keyin(5)
L, W, Vtn, Vtp, BetaN, BetaP, uCoxN, uCoxP = keyin(6)
print("お疲れ様でした。入力作業が完了しました。これから計算致します。")
line()

# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝　　計算ループ　　＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
owari = 0
omakase = 0
while owari == 0:

    I5kari = keisan0(SR, Cc)
    if omakase == 0:
        print("計算した結果M5のMOSの電流値が I5=", I5kari * 1000000, "[uA]となりました。")
        print("I5の値を入力してください。　　　　(単位は[uA]です。)")
        line0()
        print("　　　　　通常I5の値は計算結果より桁外れ（10倍以上）に大きい値に設定することが多いです。")
        print("         よくわからない方は　0　を入力してください。　お任せモードを起動します。")
        line0()
        I5 = float(input())
        I5 = I5 * 0.000001
    else:
        I5 = 0

    if I5 == 0:
        I5 = I5kari * 16.6
        omakase = 1
        line()
        print(">>>   お任せモードを起動しました。 <<<")
        wait()
        line()

    print("I5の値を", I5 * 1000000, "[uA]として残りの計算をします。")
    wait()
    line()

    LW1, LW3, LW5, LW6, LW7 = keisan1(Vdd, Vss, GB, Cc, VinMin, VinMax, Vtn, Vtp, BetaN, BetaP, uCoxN, uCoxP, I5)

    LW2 = LW1
    LW4 = LW3

    # 　　　　計算結果表示

    line()
    print("計算が終了しました。計算結果は以下のようになりました。")
    print("LW1=", LW1)
    print("LW2=", LW2)
    print("LW3=", LW3)
    print("LW4=", LW4)
    print("LW5=", LW5)
    print("LW6=", LW6)
    print("LW7=", LW7)
    wait()
    line()

    W1, erro1 = hyouzi(LW1, W, 1)
    W2, erro2 = hyouzi(LW2, W, 2)
    W3, erro3 = hyouzi(LW3, W, 3)
    W4, erro4 = hyouzi(LW4, W, 4)
    W5, erro5 = hyouzi(LW5, W, 5)
    W6, erro6 = hyouzi(LW6, W, 6)
    W7, erro7 = hyouzi(LW7, W, 7)
    wait()

    erro = 0
    if erro1 == 0 and erro2 == 0 and erro3 == 0 and erro4 == 0 and erro5 == 0 and erro6 == 0 and erro7 == 0:
        if omakase == 1:
            filewrite(L, W1, W2, W3, W4, W5, W6, W7, W5, Cc, 150, Vdd, GB, SR, Cc, VinMin, VinMax, W, Vtn, Vtp, BetaN, BetaP, uCoxN, uCoxP)
        else:
            line()
            print("M8のLの値は", L, "[um]です。バイアス段のMOS、M8のWの値を入力してください。")
            print("基本的にはM5の値", W5, "[um]と同じ値を入力してください。単位は[um]です。")
            W8 = float(input())
            line()
            print("バイアス段の抵抗　R1の抵抗値を入力してください。")
            print("単位は[KΩ]です。　よくわからない場合は　0　と入力してください。")
            R1 = float(input())

            while R1 == 0:
                print("    ======================================================================================")
                print("    == とりあえずよくわかんない時は、100kΩ~150kΩの値をいい加減に入れておいてください。")
                print("    == その場合、シミュレーションの時にいい波形が出るように微調整してください。")
                print("    == 計算から算出する方法もありますが、時間かかる割に")
                print("    == 計算通りのシミュレーション結果にならないので時間の無駄です。")
                print("    ======================================================================================")
                print("バイアス段の抵抗　R1の抵抗値を入力してください。単位は[KΩ]です。")
                R1 = float(input())
            filewrite(L, W1, W2, W3, W4, W5, W6, W7, W8, Cc, R1, Vdd, GB, SR, Cc, VinMin, VinMax, W, Vtn, Vtp, BetaN, BetaP, uCoxN, uCoxP)

        line()
        print("オペアンプにおけるLWの値の計算の全ての過程を終了しました。お疲れ様でした。")
        line()
        owari = 1
    else:
        line()
        print("計算した結果が必要要件に満たなかったので再度計算をします。")
        print("現在の計算に必要な数値の設定値は以下のようになっています。")
        print("== 電源電圧             : ", Vdd*2)
        print("== 利得帯域幅           : ", GB*0.000001)
        print("== スルーレート         ： ", SR*0.000001)
        print("== 位相補償用キャパシタ   ： ", Cc*1000000000000)
        print("== 入力範囲の最小値      : ", VinMin)
        print("== 入力範囲の最大値      : ", VinMax)
        print("== Lの基準値           : ", L)
        print("== Wの基準値           : ", W)
        wait()

        kaihen = 1
        while kaihen == 1:
            line()
            print("以上の設定値のうちどの数値を変更しますか？")
            print("該当する番号を入力してください。")
            print("== 電源電圧            : 0")
            print("== 利得帯域幅          : 1")
            print("== スルーレート        ： 2")
            print("== 位相補償用キャパシタ ： 3")
            print("== 入力範囲の最小値     : 4")
            print("== 入力範囲の最大値     : 5")
            print("== L,Wの基準値        : 6")
            hennkou = float(input())
            line()
            if hennkou == 0:
                Vdd, Vss = keyin(0)
            elif hennkou == 1:
                GB = keyin(1)
            elif hennkou == 2:
                SR = keyin(2)
            elif hennkou == 3:
                Cc = keyin(3)
            elif hennkou == 4:
                VinMin = keyin(4)
            elif hennkou == 5:
                VinMax = keyin(5)
            else:
                L, W, Vtn, Vtp, BetaN, BetaP, uCoxN, uCoxP = keyin(6)

            line()
            print("まだ数値を変更しますか？")
            print("                                         yes:1 , no:0")
            kaihen = int(input())

        line()
        print("この値で再計算を行います。")
        print("== 電源電圧             : ", Vdd*2)
        print("== 利得帯域幅           : ", GB*0.000001)
        print("== スルーレート         ： ", SR*0.000001)
        print("== 位相補償用キャパシタ   ： ", Cc*1000000000000)
        print("== 入力範囲の最小値      : ", VinMin)
        print("== 入力範囲の最大値      : ", VinMax)
        print("== Lの基準値           : ", L)
        print("== Wの基準値           : ", W)
        wait()




exit = 0
while exit == 0:
    print("終了したい場合は何かキーを押してください。")
    exit = input()
exit()
