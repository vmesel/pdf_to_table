from tabula import read_pdf
df = read_pdf("teste_ler_pdf.pdf", spreadsheet=True, multiple_tables=True, pages=[1,2])

for ind in range(0,2):
    df_ = df[ind]
    df_.to_csv("file_{}.csv".format(ind))
