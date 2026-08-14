# รับคะแนนนักเรียนห้าคน

scores = []
# รับคะแนนและเก็บลงใน list
for i in range(5):
   score = int(input(f"Enter score of student {i+1}: "))
   scores.append(score)
print()
# ตรวจสอบคะแนน
for i in range(5):
   if scores[i] >= 50:
       print(f"Student {i+1}: {scores[i]} -> ผ่าน")
   else:
       print(f"Student {i+1}: {scores[i]} -> ไม่ผ่าน")