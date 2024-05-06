import extensionConverters.pdfConverterUtils as PCU
import os

def pdfConvert(pdf_path):

    pdfFileObj = open(pdf_path, 'rb')
    pdfReaded = PCU.PyPDF2.PdfReader(pdfFileObj)
    text_per_page = {}
    image_flag = False

    for pagenum, page in enumerate(PCU.extract_pages(pdf_path)):

        pageObj = pdfReaded.pages[pagenum]
        page_text = []
        line_format = []
        text_from_images = []
        text_from_tables = []
        page_content = []
        table_in_page= -1
        pdf = PCU.pdfplumber.open(pdf_path)
        page_tables = pdf.pages[pagenum]
        tables = page_tables.find_tables()

        if len(tables)!=0:
            table_in_page = 0

        for table_num in range(len(tables)):
            table = PCU.extract_table(pdf_path, pagenum, table_num)
            table_string = PCU.table_converter(table)
            text_from_tables.append(table_string)

        page_elements = [(element.y1, element) for element in page._objs]
        page_elements.sort(key=lambda a: a[0], reverse=True)

        for i,component in enumerate(page_elements):
            element = component[1]

            if table_in_page == -1:
                pass
            else:
                if PCU.is_element_inside_any_table(element, page ,tables):
                    table_found = PCU.find_table_for_element(element,page ,tables)
                    if table_found == table_in_page and table_found != None:    
                        page_content.append(text_from_tables[table_in_page])
                        page_text.append('table')
                        line_format.append('table')
                        table_in_page+=1
                    continue

            if not PCU.is_element_inside_any_table(element,page,tables):

                if isinstance(element, PCU.LTTextContainer):
                    (line_text, format_per_line) = PCU.text_extraction(element)
                    page_text.append(line_text)
                    line_format.append(format_per_line)
                    page_content.append(line_text)

                if isinstance(element, PCU.LTFigure):
                    PCU.crop_image(element, pageObj)
                    PCU.convert_to_images('cropped_image.pdf')
                    image_text = PCU.image_to_text('PDF_image.png')
                    text_from_images.append(image_text)
                    page_content.append(image_text)
                    page_text.append('image')
                    line_format.append('image')
                    image_flag = True

        dctkey = 'Page_'+str(pagenum)
        text_per_page[dctkey]= [page_text, line_format, text_from_images,text_from_tables, page_content]
    pdfFileObj.close()
    if image_flag:
        os.remove('cropped_image.pdf')
        os.remove('PDF_image.png')
    result = ''.join(text_per_page['Page_0'][4])
    return(result)