import PyPDF2
import pdfplumber

def command():
    file_path='invoice.pdf'
    invoice=file_path

    with pdfplumber.open(invoice) as pdf:
        page=pdf.pages[0]
        text=page.extract_text()
    #print(text)

    for row in text.split('\n'):
        if row.startswith('Total'):
            balance=row.split()[-1]
    print('balance:'+ '' + balance)
