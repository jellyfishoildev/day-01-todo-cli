# Todo CLI

โปรแกรมจัดการรายการงานผ่านเทอร์มินัล เขียนด้วย Python (ไม่ต้องติดตั้งไลบรารีเพิ่ม)

## Features

- เพิ่มงานใหม่ (`add`)
- ดูรายการงานทั้งหมด (`list`)
- ทำเครื่องหมายว่างานเสร็จแล้ว (`done`)
- ลบงาน (`del`)
- บันทึกข้อมูลลงไฟล์ `todos.json` ข้อมูลไม่หายเมื่อปิดโปรแกรม
- รองรับภาษาไทย

## วิธีรัน

ต้องมี Python 3 ติดตั้งอยู่

```bash
git clone https://github.com/jellyfishoildev/day-01-todo-cli.git
cd day-01-todo-cli
```

## วิธีใช้

```bash
python todo.py add "ส่งการบ้าน"
python todo.py list
python todo.py done 1
python todo.py del 1
```

ตัวอย่างผลลัพธ์:

```
1. [x] ส่งการบ้าน
2. [ ] ออกกำลังกาย
```

## สิ่งที่ได้เรียนรู้

- การอ่านอาร์กิวเมนต์จาก terminal ด้วย `sys.argv`
- การอ่าน/เขียนไฟล์ JSON ด้วยโมดูล `json` พร้อมรองรับภาษาไทย (`ensure_ascii=False`)
- การจัดการ error ด้วย `try/except` และการตรวจขอบเขตของ index
- การใช้ Git: commit แยกตามฟีเจอร์ และเขียน commit message แบบ Conventional Commits

## แผนต่อไป

- [ ] เปลี่ยนไปใช้ `argparse`
- [ ] เพิ่มวันที่กำหนดส่ง
- [ ] เพิ่ม unit test ด้วย `pytest`