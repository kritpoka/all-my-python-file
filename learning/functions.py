def get_box_area(width, length, height):
    if width < 0 or length < 0 or height < 0:
        return 0 
    box_area = width * length * height
    return box_area

#เมื่อ funtions เจอ return จะหยุดทำงานทันที
#return จะส่งค่าไปยังบรรทัดที่เรียกใช้

box1 = get_box_area(4, 0, 2)
box2 = get_box_area(width=1, length=1, height=1)

print(box1)