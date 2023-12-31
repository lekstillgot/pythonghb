def checkberdee(phone_number=0):
    # สร้างตัวแปลเก็บผลรวมเบอร์
    total = 0
    predict = ""

    # วนลูป
    for phone in (phone_number):
        total += int(phone)

    # ทำนายผลรวม
    if total in (4, 5, 6, 9, 14, 15, 19, 23, 24, 32,
                 36, 40, 41, 42, 44, 45, 46, 50, 51, 54):
        predict = "เลขผลรวมดีมาก โอกาสประสบผลสำเร็จสูง อุปสรรคน้อย เจริญรุ่งเรือง ร่ำรวย รวดเร็ว และมีความสุขในชีวิต"
    elif total in (8, 10, 13, 16, 18, 22, 25, 26, 28,
                   31, 35, 38, 39, 47, 49, 52, 53):
        predict = "เลขผลรวมดีปานกลาง โอกาสประสบผลสำเร็จสูง อุปสรรคน้อย เจริญรุ่งเรือง ร่ำรวย รวดเร็ว และมีความสุขในชีวิต"
    elif total in (3, 7, 11, 12, 17, 20, 21, 27, 29,
                   30, 33, 34, 37, 43, 48):
        predict = "(ให้โทษ ใครได้ผลรวมเหล่านี้ควรเปลี่ยน)เลขผลรวมไม่ดี เหนื่อยมาก อุปสรรคมาก เจอปัญหารุมเร้า การงาน การเงิน ความรัก โอกาสเกิดอุบัติเหตุสูง"
    else:
        predict = "ไม่พบ"

    return predict


phone = input("กรุณากรอกหมายเลขทะเบียนของคุณ :")
print(checkberdee(phone))
