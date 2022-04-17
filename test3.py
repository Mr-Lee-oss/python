# print("\\   /\\")
# print(" )  ( ')")
# print("(  /  )")
# print(") \(__)|")

# print("\\    /\\")
# print(" )  ( ')")
# print("(  /  )")
# print(" \\(__)|")

a,b = map(int,input().split()) # map을 사용하여 split를 통해 여러 수를 한번에 입력받을 수 있음 
#map은 리스트의 요소를 지정된 함수로 처리해주는 함수입니다(map은 원본 리스트를 변경하지 않고 새 리스트를 생성합니다).
if a>b:
     print (">")
elif a<b:
     print("<")
elif a==b:
     print("==")