"""
0DEC
 -> 0 2
0269FAC9A0
 -> 1 1 7 8 0

"""
secrets = {
    '001101': 0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001011': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9,
}
password = list(input())
new_password = []
#16진수를 10진수 변환
for i in range(len(password)):
    d = ord(password[i])-ord('0') if '0' <= password[i] <= '9' else ord(password[i])-ord('A') + 10
    new_password.append(d)
#10진수 -> 2진수
output = ''
for i in new_password:
    for j in range(3, -1, -1):
        if i & (1<<j):
            output+='1'
        else:
            output+='0'
# 0DEC 일 때, output은 00 001101 111011 00
N = len(output)

ans = []
i = 0
while i <= N:
    if output[i:i+6] in secrets.keys():
        ans.append(secrets[output[i:i+6]])
        i += 6
    else:
        i+=1

print(ans)
