import math

print("Vdd の値を入力してください")
print("単位は[V]です。")
Vdd=float(input())

print("OmegaU の値を入力してください")
print("単位は[MHZ]です。")
OmegaU=float(input())
OmegaU=OmegaU*1000000

print("SR の値を入力してください")
print("単位は[V/us]です。")
SR=float(input())
SR=SR*1000000

print("Cc の値を入力してください")
print("Cc > 0.2xCout を満たす数値にしてください")
print("単位は[pF]です。")
Cc=float(input())
Cc=Cc*0.000000000001

print("VinMin の値を入力してください")
print("単位は[V]です。")
VinMin=float(input())

print("VinMax の値を入力してください")
print("単位は[V]です。")
VinMax=float(input())

print("Vtn　の値を入力してください")
print("単位は[V]です。")
Vtn=float(input())

print("Vtp　の値を入力してください")
print("単位は[V]です。")
Vtp=float(input())

print("BetaN の値を入力してください")
BetaN=float(input())

print("BetaP の値を入力してください")
BetaP=float(input())

print("入力作業完了、これから計算致します。")

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
print(VoutMin)

VoutMax=Vdd-math.sqrt((2*I5*(LW7/LW5))/(BetaP*LW6))
print(VoutMax)

#教科書　P194　式11.35　の　λp　λn の意味が分からないため　コメントアウト
#A0=(Cc*2*math.pi*OmegaU*10*Cc*2*math.pi*OmegaU)/((I5/2)*(  λp  +  λn  )*I5*(LW7/LW5)*(  λp  +  λn  ))
#print(A0)

print("計算が終了しました。")
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

exit=0
while exit==0:
    print("終了したい場合は何かキーを押してください。")
    exit = input()


