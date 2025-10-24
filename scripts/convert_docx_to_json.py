import docx
import json
import os
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.table import Table
from docx.text.paragraph import Paragraph

def docx_to_json(docx_path, json_path):
    """
    Reads tables and their preceding titles from a .docx file and converts them to a JSON file.
    The JSON structure is a dictionary where keys are table titles and values are table data.
    """
    try:
        document = docx.Document(docx_path)
        data_with_titles = {}
        current_title = None

        for block in document.element.body:
            if isinstance(block, CT_P):
                paragraph = Paragraph(block, document)
                if paragraph.text.strip() and "Financial Highlights" in paragraph.text:
                    current_title = paragraph.text.strip()
            elif isinstance(block, CT_Tbl):
                if current_title:
                    table = Table(block, document)
                    table_data = []
                    if not table.rows:
                        continue

                    # Extract headers from the first row
                    headers = [cell.text.strip() for cell in table.rows[0].cells]
                    
                    # Extract data from the rest of the rows
                    for row in table.rows[1:]:
                        row_data = {}
                        for j, cell in enumerate(row.cells):
                            # Ensure we don't go out of bounds for headers
                            if j < len(headers):
                                row_data[headers[j]] = cell.text.strip()
                        table_data.append(row_data)
                    
                    data_with_titles[current_title] = table_data
                    current_title = None # Reset for next table

        # Ensure the output directory exists
        output_dir = os.path.dirname(json_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Write data to JSON file
        with open(json_path, 'w', encoding='utf-8') as json_file:
            json.dump(data_with_titles, json_file, indent=4, ensure_ascii=False)
            
        print(f"Successfully converted '{docx_path}' to '{json_path}' with table titles.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Correctly resolve paths relative to the project root
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    docx_file = os.path.join(project_root, 'data', '2025_dat_techcombank_paste.docx')
    json_file = os.path.join(project_root, 'data', 'financial_highlights.json')
    
    docx_to_json(docx_file, json_file)
