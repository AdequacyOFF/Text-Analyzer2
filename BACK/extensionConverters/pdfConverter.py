import pdfConverterUtils as PCU
import os

def pdfConvert(pdf_path):
    # Find the PDF path

    # Create a pdf file object
    pdfFileObj = open(pdf_path, 'rb')
    # Create a pdf reader object
    pdfReaded = PCU.PyPDF2.PdfReader(pdfFileObj)
    # Create the dictionary to extract text from each image
    text_per_page = {}
    # Create a boolean variable for image detection
    image_flag = False

    # We extract the pages from the PDF
    for pagenum, page in enumerate(PCU.extract_pages(pdf_path)):

        # Initialize the variables needed for the text extraction from the page
        pageObj = pdfReaded.pages[pagenum]
        page_text = []
        line_format = []
        text_from_images = []
        text_from_tables = []
        page_content = []
        # Initialize the number of the examined tables
        table_in_page= -1
        # Open the pdf file
        pdf = PCU.pdfplumber.open(pdf_path)
        # Find the examined page
        page_tables = pdf.pages[pagenum]
        # Find the number of tables in the page
        tables = page_tables.find_tables()
        if len(tables)!=0:
            table_in_page = 0

        # Extracting the tables of the page
        for table_num in range(len(tables)):
            # Extract the information of the table
            table = PCU.extract_table(pdf_path, pagenum, table_num)
            # Convert the table information in structured string format
            table_string = PCU.table_converter(table)
            # Append the table string into a list
            text_from_tables.append(table_string)

        # Find all the elements
        page_elements = [(element.y1, element) for element in page._objs]
        # Sort all the element as they appear in the page 
        page_elements.sort(key=lambda a: a[0], reverse=True)


        # Find the elements that composed a page
        for i,component in enumerate(page_elements):
            # Extract the element of the page layout
            element = component[1]

            # Check the elements for tables
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
                    # Pass this iteration because the content of this element was extracted from the tables
                    continue

            if not PCU.is_element_inside_any_table(element,page,tables):

                # Check if the element is text element
                if isinstance(element, PCU.LTTextContainer):
                    # Use the function to extract the text and format for each text element
                    (line_text, format_per_line) = PCU.text_extraction(element)
                    # Append the text of each line to the page text
                    page_text.append(line_text)
                    # Append the format for each line containing text
                    line_format.append(format_per_line)
                    page_content.append(line_text)


                # Check the elements for images
                if isinstance(element, PCU.LTFigure):
                    # Crop the image from PDF
                    PCU.crop_image(element, pageObj)
                    # Convert the croped pdf to image
                    PCU.convert_to_images('cropped_image.pdf')
                    # Extract the text from image
                    image_text = PCU.image_to_text('PDF_image.png')
                    text_from_images.append(image_text)
                    page_content.append(image_text)
                    # Add a placeholder in the text and format lists
                    page_text.append('image')
                    line_format.append('image')
                    # Update the flag for image detection
                    image_flag = True


        # Create the key of the dictionary
        dctkey = 'Page_'+str(pagenum)
        # Add the list of list as value of the page key
        text_per_page[dctkey]= [page_text, line_format, text_from_images,text_from_tables, page_content]
    # Close the pdf file object
    pdfFileObj.close()
    # Delete the additional files created if image is detected
    if image_flag:
        os.remove('cropped_image.pdf')
        os.remove('PDF_image.png')
    # Display the content of the page
    result = ''.join(text_per_page['Page_0'][4])
    return(result)