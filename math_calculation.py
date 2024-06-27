import datetime
import os
import random
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
dt = datetime.date.today().strftime("%Y%m%d")

def generate_question():
    """生成一个随机的计算题"""
    operators = ['+', '-', '×', '÷']
    operator = random.choice(operators)
    if operator == '+':
        num1 = random.randint(1,199)
        num2 = random.randint(1,199)
    elif operator == '-':
        num1 = random.randint(1,199)
        num2 = random.randint(1,99)
        num1, num2 = max(num1, num2), min(num1, num2)
    elif operator == '×':
        num1 = random.randint(2,99)
        num2 = random.randint(2,9)
    elif operator == '÷':
        num1 = random.randint(2,9)
        num2 = random.randint(2,9)
        num1 = num1 * num2
    question = f"{num1} {operator} {num2} = "
    return question

def generate_exam(num_questions):
    return [generate_question() for _ in range(num_questions)]

def save_exam_to_pdf(filename,questions,questions_per_page=148,columns=4):
    c = canvas.Canvas(filename,pagesize=A4)
    width,height = A4
    margin = 72  # 1 inch
    column_width = (width - 2 * margin) / columns
    start_x = margin
    start_y = height - margin - 30
    inter_line_spacing = 20
    for index,question in enumerate(questions):
        exam_number = index // questions_per_page +1
        title = f"Lisa  GO!GO!GO!  {dt} ({exam_number})"
        if index % questions_per_page == 0:  # 每页的第一个问题
            if index != 0:
                c.showPage()  # 除了第一页外，每开始新一页前显示上一页
            c.drawString(margin, height - margin + 15, title)  # 新页也添加标题
        column = index % columns
        row = (index % questions_per_page) // columns
        x = start_x + column * column_width
        y = start_y - row * inter_line_spacing
        c.drawString(x, y, question)
    c.save()
    print(f"试卷已保存到文件：{filename}")

# 生成试卷
if not os.path.exists(f"./data/{dt}"):
    os.makedirs(f"./data/{dt}")
exam_questions = generate_exam(148*10)
save_exam_to_pdf(f"./data/{dt}/1.pdf", exam_questions)
