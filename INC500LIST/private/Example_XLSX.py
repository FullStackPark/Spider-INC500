import xlsxwriter

filename = "demo.xlsx"

workbook = xlsxwriter.Workbook(filename)
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 20)

# Formats
title_style = workbook.add_format({'bold': True, 'align': 'left'})
content_style = workbook.add_format({'bold': False, 'align': 'left'})

# Write titles
worksheet.write('A1', 'Hello', title_style)
worksheet.write('B1', 'Hello', title_style)

# Text with formatting.
worksheet.write('A2', 'World', content_style)

# Write some numbers, with row/column notation.
worksheet.write(2, 0, 123, content_style)
worksheet.write(3, 0, 123.456, content_style)

# Insert an image.
# worksheet.insert_image('B5', 'logo.png')

workbook.close()
