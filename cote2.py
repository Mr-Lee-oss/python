# def solution(id_list, report):
#     print("ID: : %s" %id_list )
#     print("신고횟수 : %d" %report)
# solution("test", 2 )

id_list = input("아이디 입력.\n")
def solution(id_list):
    members = ["muzi", "frodo", "apeach", "neo"]
    for members in members:
       if members == id_list:
           return True
    return False
if solution(id_list):
    print('Hello, '+id_list)
else:
    print("nugu")
