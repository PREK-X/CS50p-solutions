from fpdf import FPDF


def main():

    name = input("Name: ")

    pdf = FPDF()
    pdf.set_auto_page_break(True)
    pdf.add_page()
    pdf.set_font("helvetica", size = 50)
    pdf.cell(h = 70, text = "CS50 Shirtificate", center = True)
    pdf.image("shirtificate.png", x = 15, y = 80, w = 180, h = 180)
    pdf.set_font("helvetica", size = 30)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(h = 280, text = f"{name} took CS50", center = True)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
