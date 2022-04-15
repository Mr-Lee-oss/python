#4월 9일
# 6006번
#print("\"!@#$%^&*()'")
# 6007번
#print("""\"C:\Download\\'hello'.py\"""") #해당 내용은 """으로 "출력하는것 과 경로에서 \ 을 이용해서 백슬래쉬를 프린트 해야 하는 거임
# 6008번
#print('print("'"Hello\\nWorld"'")') #이거는 \\으로 \를 출력해야 했고 print가 완전히 출력되어야 했음
# 6009번
#  a = input()
# print(a) # 변수설정과 프린트만 하면 되는 간단한 문제였음
#6010번
#a=input() # 변수를 입력받을 것인지
#a = int(a) # a로 변수로 입력받으면 이렇게 int(a)를 해줌
#print(a) # 프린트해줌
#6011번
#a = input() #변수 입력 받음
#a = float(a) #실수 입력 float
#print(a)
#6012번
#a = input() #2개의 변수를 입력을 받고 출력하는 것
#b = input()
#a = int(a) 
#b = int(b)
#print(a)
#print(b)
#6013번
#a = input() #줄을 바꿔서 출력하라고 했으니 출력을 두번하면 되는건가?
#b = input()
#a = str(a) # 문자로 받는다고 하니 문자인 str()로 해주면 됨
#b = str(b)
#print(b)
#print(a)
#6014번
#a=input() # 실수 하나를 받아서 출력 하는거
#a=float(a)
#print (a,a,a, sep='\n') # 변수 하나당 줄바꿈 하려면 sep='\n'을 해야함 
#6015번
#a, b = input().split() # 변수를 한번에 받고 split = 쪼개기? 느낌 를 쓰는 거
#print(a,b, sep='\n')
#6016번
#a,b = input().split()
#print(b,'%1s'%a) #문자열을 공배긍로 처리할 때는 '%공백숫자s'로 함 s는 문자열 처리 이 후 변수에 %를 붙여줌
#6017번
#a = input()
#print(a,'%1s'%a,'%1s'%a ) # 하나의 인풋을 받아 공백을 넣고 지속적 출력을 말하는 듯?
#6018번
#a,b = input().split(':') # 이렇게 하는 것은 조건이 3:16의 입력을 하기에 ':'이 기준으로 입력을 쪼갠다
#print(a,b,sep=':') # sep는 분류기호를 이야기한다고 함
#6019번
#y, m, d = input().split('.')
#print (d,m,y, sep='-') #sep는 분류 기호이기 때문에 따로따로 먹히는듯 
#6020번
#a,b = input().split('-') #입력을 000907-1121112 이런식으로 받으니 '-'로 나눠줄 수 있음
#print(a,b,sep='') # 표현 형식으로 ''로 하면 공백처리해서 붙이는 듯
#6021번
#a = input()
#for i in range(0,5) : # 문자열을 받고 그것을 배열형식으로 순번을 받으니 for문을 돌림
#  print(a[i])
#6022번
#a = input()
#print(a[0:2], a[2:4], a[4:6]) # 문자열을 배열로 잘라서 표현하는 것인듯?
#6023번
#a,b,c = input ().split(':') # 입력을 시:분:초 형식으로 하니 이걸로 나누고 분에 있는 것을 출력하면 될듯?
#print(b)
#6024번
#a,b = input().split()# 공백으로 쪼개서 입력받는다
##c= a+b # 변수로 합치기
#print(a+b) #문자열을 print에서 합쳐도 되는듯
#6025번
#a,b = input().split() # 공백으로 쪼개기
#print(int(a)+int(b)) # 입력을 123 -123로 받으니 + 해도 될듯?
#6026번
#a = float(input())
#b = float(input())
#print(a+b) # 실수 받아서 계산하는 거니 단위변환는 필요 없는듯?
#6027번
#a = int(input())
#print('%x'%a) # 정수를 받아서 16진수를 나타내면 이리 되는듯
#6028번
#a = int(input())
#print('%X'%a) #'%X'를 하면 대문자로 출력함
#6029번
#a = int(input(), 16) # 뒤에 숫자를 붙이면 몇진수로 받을지를 정할 수 있음
#print('%o'%a) # 진수 변화를 하여 출력할 때는 앞에 %d등을 붙여 할 수 잇음
#6030번
#a = input()
#print(ord(a)) #유니코드 변환은 ord
#6031번
#a = int(input())
#print(chr(a)) # ord는 문자 -> 정수 / chr은 정수 -> 문자로변환 시키는 것
#6032번
#a = int(input())
#print(-a) # 정수를 받고 -를 통해 부호 변환을 함
#6033번
#a = input()
#a = ord(a) # ord를 통해서 문자를 정수로 바꾸고
#print(chr(a+1)) # chr을 통해서 정수를 문자로 바꿈
#6034번
#a,b = input().split() #split을 사용하여 공백으로 쪼개기
#c = int(a) -int(b)  # 변수로 값 설정
#print(c)
