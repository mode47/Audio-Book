import pyttsx3
import PyPDF2
class pdf:
    def read(self,book):
        pdf = open(book, 'rb')
        read_pdf = PyPDF2.PdfReader(pdf)
        pdf_page = read_pdf.numPages
        #print(pdf_page)
        pdf_speker = pyttsx3.init()
        for i in range(0, pdf_page):
            choose_page = read_pdf.getPage(i)
            pdf_text = choose_page.extractText()
            pdf_speker.say(pdf_text)
            pdf_speker.runAndWait()
        #    print(f"page number {i} finshed")

pdf=pdf()
pdf.read('Introduction.pdf')




