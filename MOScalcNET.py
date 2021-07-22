import math

print("=====================================================")
print("このツールはオペアンプにおけるLWの値を自動で算出するものです。")
print("=====================================================")

print("電源電圧　Vdd の値を入力してください")
print("単位は[V]です。")
Vdd=float(input())

print("=====================================================")

print("利得帯域幅　ωu の値を入力してください")
print("単位は[MHZ]です。")
OmegaU=float(input())
OmegaU=OmegaU*1000000

print("=====================================================")

print("スルーレート　SR の値を入力してください")
print("単位は[V/us]です。")
SR=float(input())
SR=SR*1000000

print("=====================================================")

print("位相補償用キャパシタ　Cc の値を入力してください")
print("(位相補償キャパシタCc) > 0.2　x (負荷容量Cl) を満たす数値にしてください")
print("単位は[pF]です。")
Cc_p=float(input())
Cc=Cc_p*0.000000000001

print("=====================================================")

print("入力範囲の最小値 VinMin の値を入力してください")
print("単位は[V]です。")
VinMin=float(input())

print("=====================================================")

print("入力範囲の最大値　VinMax の値を入力してください")
print("単位は[V]です。")
VinMax=float(input())

print("=====================================================")

print("Lの基準値を入力してください")
print("単位は[u]です。")
L=float(input())

print("=====================================================")

print("Wの基準値を入力してください")
print("単位は[u]です。")
W=float(input())

print("=====================================================")

print("基準値L,Wに対して")
print("nmosの閾値　Vtn　の値を入力してください")
print("単位は[V]です。")
Vtn=float(input())

print("=====================================================")

print("基準値L,Wに対して")
print("pmosの閾値　Vtp　の値を入力してください")
print("単位は[V]です。")
Vtp=float(input())

print("=====================================================")

print("基準値L,Wに対して")
print("BetaN の値を入力してください")
BetaN=float(input())

print("=====================================================")

print("基準値L,Wに対して")
print("BetaP の値を入力してください")
BetaP=float(input())


print("入力作業完了、これから計算致します。")

print("=====================================================")

I5 = SR * Cc
print("I5=",I5)

LW3=I5/(BetaP*(Vdd-VinMax+Vtn-Vtp)*(Vdd-VinMax+Vtn-Vtp))
LW4=LW3
print("LW3=",LW3)

LW1=(Cc*Cc*OmegaU*OmegaU*2*2*math.pi*math.pi)/(BetaN*I5)
LW2=LW1
print("LW1=",LW1)

LW5=(2*I5)/(BetaN*(VinMin-Vtn-math.sqrt(I5/(BetaN*LW1)))*(VinMin-Vtn-math.sqrt(I5/(BetaN*LW1))))
print("LW5=",LW5)

LW6=(10*Cc*2*math.pi*OmegaU*LW3)/math.sqrt(BetaP*LW3*I5)
print("LW6=",LW6)

LW7=(LW5*LW6)/(2*LW3)
print("LW7=",LW7)

VoutMin=math.sqrt((2*I5*LW7/LW5)/(BetaN*LW7))
print("VoutMin=",VoutMin)

VoutMax=Vdd-math.sqrt((2*I5*(LW7/LW5))/(BetaP*LW6))
print("VoutMax=",VoutMax)

#教科書　P194　式11.35　の　λp　λn の意味が分からないため　コメントアウト
#A0=(Cc*2*math.pi*OmegaU*10*Cc*2*math.pi*OmegaU)/((I5/2)*(  λp  +  λn  )*I5*(LW7/LW5)*(  λp  +  λn  ))
#print(A0)

print("計算が終了しました。")
print("=====================================================")
print("以下に計算結果を示します。")

print("LW1=",LW1)
print("LW2=",LW2)
print("LW3=",LW3)
print("LW4=",LW4)
print("LW5=",LW5)
print("LW6=",LW6)
print("LW7=",LW7)
print("VoutMin=",VoutMin)
print("VoutMax=",VoutMax)

print("=====================================================")

LW=W/L

L1=L
W1=L1*LW1*LW

L2=L
W2=L2*LW2*LW

L3=L
W3=L3*LW3*LW

L4=L
W4=L4*LW4*LW

L5=L
W5=L5*LW5*LW

L6=L
W6=L6*LW6*LW

L7=L
W7=L7*LW7*LW

L8=L

print("MOS1のL＝",L1,"[um]")
print("MOS1のW＝",W1,"[um]")
print("MOS2のL＝",L2,"[um]")
print("MOS2のW＝",W2,"[um]")
print("MOS3のL＝",L3,"[um]")
print("MOS3のW＝",W3,"[um]")
print("MOS4のL＝",L4,"[um]")
print("MOS4のW＝",W4,"[um]")
print("MOS5のL＝",L5,"[um]")
print("MOS5のW＝",W5,"[um]")
print("MOS6のL＝",L6,"[um]")
print("MOS6のW＝",W6,"[um]")
print("MOS7のL＝",L7,"[um]")
print("MOS7のW＝",W7,"[um]")

print("=====================================================")

print("netリストを生成します。")
print("netリストのファイル名を入力してください")
x=input()

print("=====================================================")

print("M8のLの値は",L8,"[um]です。")
print("バイアス段のMOS、M8のWの値を入力してください。")
print("単位は[um]です。")
W8=float(input())

print("=====================================================")

print("バイアス段の抵抗　R1の抵抗値を入力してください。")
print("単位は[KΩ]です。")
R1=float(input())

print("=====================================================")

print(x,".net　というファイルを作成します。")

f=open('./'+x+'.net','w')

f.write("opamp_netlist\n\n")
f.write(".param psvoltage="+str(Vdd*2)+"\n\n")
f.write(".subckt opamp inm inp out vdd vss\n\n")
f.write("M1 net1 inm  net2 vss cmosn L="+str(L1)+"u W="+str(W1)+"u\n")
f.write("M2 net3 inp  net2 vss cmosn L="+str(L2)+"u W="+str(W2)+"u\n")
f.write("M3 net1 net1 vdd  vdd cmosp L="+str(L3)+"u W="+str(W3)+"u\n")
f.write("M4 net3 net1 vdd  vdd cmosp L="+str(L4)+"u W="+str(W4)+"u\n")
f.write("M5 net2 vb   vss  vss cmosn L="+str(L5)+"u W="+str(W5)+"u\n")
f.write("M6 out  vb   vss  vdd cmosp L="+str(L6)+"u W="+str(W6)+"u\n")
f.write("M7 out  vb   vss  vss cmosn L="+str(L7)+"u W="+str(W7)+"u\n")
f.write("C1 net3 out "+str(Cc_p)+"p\n\n")
f.write("R1 vdd  vb "+str(R1)+"k\n")
f.write("M8 vb   vb   vss  vss cmosn L="+str(L8)+"u W="+str(W8)+"u\n\n")
f.write(".ends opamp\n")

f.close()

print(x,".net　というファイルを作成しました。")

exit=0
while exit==0:
    print("終了したい場合は何かキーを押してください。")
    exit = input()
