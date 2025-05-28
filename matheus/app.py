import openpyxl

# Criar uma planilha
book = openpyxl.Workbook()

#Como visualizar páginas existentes
print(book.sheetnames)

# Como criar uma página
book.create_sheet("camisas")
#como selecionar uma página
camisas_page = book['camisas']
camisas_page.append(['camisas', 'Nome', 'Número', 'Preço'])
camisas_page.append(['Manchester City', 'De Bruyne', '17', 'R$429,99'])
camisas_page.append(['Manchester United', 'Bruno Fernandes', '10', 'R$246,99'])
camisas_page.append(['Newcastle', 'Bruno Guimarães', '39', 'R$379,99'])
camisas_page.append(['Liverpool', 'Salah', '11', 'R$189,99'])
# Salvar a planilha
book.save('Planilha de camisas.xlsx')