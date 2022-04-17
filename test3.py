# print("\\   /\\")
# print(" )  ( ')")
# print("(  /  )")
# print(") \(__)|")

# print("\\    /\\")
# print(" )  ( ')")
# print("(  /  )")
# print(" \\(__)|")
#백준 단계별 문제
# a,b = map(int,input().split()) # map을 사용하여 split를 통해 여러 수를 한번에 입력받을 수 있음 
# #map은 리스트의 요소를 지정된 함수로 처리해주는 함수입니다(map은 원본 리스트를 변경하지 않고 새 리스트를 생성합니다).
# if a>b:
#      print (">")
# elif a<b:
#      print("<")
# elif a==b:
#      print("==")

#9498번
# a = int(input())
# if 90<=a<=100:
#     print("A")
# elif 80<=a<=89:
#     print("B")
# elif 70<=a<=79:
#     print("C")
# elif 60<=a<=69:
#     print("D")
# else :
#     print("F")
#2753번
a = int(input())
if (a%4)==0 and (a%400) ==0: #or (a%400)==0: #or (a%100)==1:
    print("1")
    if (a%100) !=0:
     print("1")
else :
    print("0")