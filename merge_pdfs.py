#SCALANIE PDFÓW (W TYM PRZYPADKU 1 z 2, 3 z 4 ITD)
import os
from PyPDF2 import PdfMerger

pdfs_dir = r'C:\Users\USER_NAME\Desktop\laczenie_pdfow\do_scalenia'
output_dir = r'C:\Users\USER_NAME\Desktop\laczenie_pdfow\scalone'  

os.makedirs(output_dir, exist_ok=True)  

merger = PdfMerger()
x = 1
for i in range(1, 87, 2):  # iteruje od 1 do 86, przeskakując co dwa
    first_file = os.path.join(pdfs_dir, f'{i}.pdf')
    second_file = os.path.join(pdfs_dir, f'{i + 1}.pdf')
    output_file = os.path.join(output_dir, f'{x}.pdf')
    x = x +1

    merger.append(first_file)
    merger.append(second_file)

    merger.write(output_file)
    merger = PdfMerger()  # resetuje obiekt merger na kolejną iterację
