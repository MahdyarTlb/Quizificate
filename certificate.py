from fpdf import FPDF
from datetime import date

def generate_certificate(name, score, total):

    today = date.today().strftime("%d/%m/%Y")

    if score < (7 * total): # 70% of total points
        return False
    elif score > (10 * total) or score < 0 or not score:
        return None

    if not name:
        return None

    if not total:
        return None

    name = name.capitalize()

    pdf = FPDF("L", "mm", "A4")
    pdf.add_page()
    pdf.image("./assets/background.jpg", x=0, y=0, w=297)

    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "", 14)
    pdf.text(12, 12, today)

    pdf.set_text_color(0, 0, 0)

    pdf.set_font("Times", "B", 40)
    pdf.set_xy(0, 55)
    pdf.cell(297, 20, "Certificate", align="C")

    pdf.set_font("Times", "", 18)
    pdf.set_xy(0, 90)
    pdf.cell(297, 10, "This certifies that", align="C")

    pdf.set_font("Times", "B", 18)
    pdf.set_xy(0, 105)
    pdf.cell(297, 10, name, align="C")

    pdf.set_font("Times", "", 18)
    pdf.set_xy(0, 125)
    pdf.cell(297, 10, "has successfully completed the Quiz by score", align="C")

    pdf.set_font("Times", "B", 18)
    pdf.set_xy(0, 140)
    pdf.cell(297, 10, f"{score}/{total * 10}", align="C")

    pdf.set_font("Times", "", 18)
    pdf.set_xy(0, 175)
    pdf.cell(297, 10, "be successful", align="C")

    try:
        pdf.output(f"certificates/{name}_cirtificate.pdf")
    except Exception as e:
        return e
    else:
        return True


