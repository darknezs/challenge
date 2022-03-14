'''
solution() เช็คว่า input ()[]{} เปิดปิดครบหรือไม่
[] --> true
]) --> false
'''
def solution(s):
    arr = []
    for i in range(len(s)):
        if i%2 == 0:
            # print(ord(s[i+1]) - ord(s[i]))
            if ord(s[i+1]) - ord(s[i]) == 1 or ord(s[i+1]) - ord(s[i]) == 2:
                arr.append('true')
            else:
                arr.append('false')
    if 'false' not in arr:
        return 'true'
    else:
        return 'false'

s1 = "()"
s2 = "()[]{}"
s3 = "{]"
s4 = "([)]"
s5 = "(){]"

print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))
print(solution(s5))









# if ord(s[i]) == ord(s[i-1]) + 1:
