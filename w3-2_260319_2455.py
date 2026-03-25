max_people = 0
current_people = 0
for _ in range(4):
    out_p, in_p = map(int, input().split())
    current_people = current_people - out_p + in_p
    if current_people > max_people:
        max_people = current_people
print(max_people)