def horseshoes(s1, s2, s3, s4):
    colors = [s1, s2, s3, s4]
    unique_colors_count = len(set(colors))
    return 4 - unique_colors_count
s1, s2, s3, s4 = map(int, input().split())
print(horseshoes(s1, s2, s3, s4))
