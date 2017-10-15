"""Transfer the json result to excel and D3"""
import json
import xlsxwriter

if __name__ == '__main__':
    f = open(file='temp/INC500_3.json', encoding='utf-8', mode='r')
    json_obj = json.loads(f.read())
    f.close()

    filename = "temp/INC500_4.xlsx"

    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()

    # Widen the first column to make the text clearer.
    worksheet.set_column('C:C', 20)

    # Formats
    title_style = workbook.add_format({'bold': True, 'align': 'left'})
    content_style = workbook.add_format({'bold': False, 'align': 'left'})

    # Write titles
    worksheet.write('A1', 'CompanyID', title_style)
    worksheet.write('B1', 'Ranking', title_style)
    worksheet.write('C1', 'CompanyName', title_style)
    worksheet.write('D1', 'Industry', title_style)
    worksheet.write('E1', 'Growth', title_style)
    worksheet.write('F1', 'Revenue', title_style)
    worksheet.write('G1', 'City', title_style)
    worksheet.write('H1', 'StateAbbr', title_style)
    worksheet.write('I1', 'StateName', title_style)
    worksheet.write('J1', 'YearsOnINCList', title_style)
    worksheet.write('K1', 'Partner', title_style)
    worksheet.write('L1', 'BriefDescription', title_style)
    worksheet.write('M1', 'Description', title_style)
    worksheet.write('N1', 'Leadership', title_style)
    worksheet.write('O1', 'Founded', title_style)
    worksheet.write('P1', 'ThreeYearGrowth', title_style)
    worksheet.write('Q1', 'Employees', title_style)
    worksheet.write('R1', 'Website', title_style)
    worksheet.write('S1', 'Location', title_style)
    worksheet.write('T1', 'WikipediaPage', title_style)
    worksheet.write('U1', 'WikipediaURL', title_style)

    rows = 1

    for company in json_obj:
        worksheet.write(rows, 0, company['CompanyID'], content_style)
        worksheet.write(rows, 1, company['Ranking'], content_style)
        worksheet.write(rows, 2, company['CompanyName'], content_style)
        worksheet.write(rows, 3, company['Industry'], content_style)
        worksheet.write(rows, 4, company['Growth'], content_style)
        worksheet.write(rows, 5, company['Revenue'], content_style)
        worksheet.write(rows, 6, company['City'], content_style)
        worksheet.write(rows, 7, company['StateAbbr'], content_style)
        worksheet.write(rows, 8, company['StateName'], content_style)
        worksheet.write(rows, 9, company['YearsOnINCList'], content_style)
        worksheet.write(rows, 10, company['Partner'], content_style)
        worksheet.write(rows, 11, company['BriefDescription'], content_style)
        worksheet.write(rows, 12, company['Description'], content_style)
        worksheet.write(rows, 13, company['Leadership'], content_style)
        worksheet.write(rows, 14, company['Founded'], content_style)
        worksheet.write(rows, 15, company['ThreeYearGrowth'], content_style)
        worksheet.write(rows, 16, company['Employees'], content_style)
        worksheet.write(rows, 17, company['Website'], content_style)
        worksheet.write(rows, 18, company['Location'], content_style)
        worksheet.write(rows, 19, company['WikipediaPage'], content_style)
        worksheet.write(rows, 20, company['WikipediaURL'], content_style)
        rows += 1

    workbook.close()

    # For Debug Purpose
    print("Dumped data into Excel file")


