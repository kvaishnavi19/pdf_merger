import PyPDF2


merger = PyPDF2.PdfMerger()

pdfiles = ["Experiment_4.pdf", "Experiment_5.pdf",]
for filename in pdfiles:
    pdfFiles = open(filename, "rb")
    pdfReader = PyPDF2.PdfReader(pdfFiles)
    merger.append(pdfReader)
    pdfFiles.close()
merger.write("Merged.pdf")
