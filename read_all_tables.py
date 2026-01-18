
import zipfile
import xml.etree.ElementTree as ET
import sys
import os

def read_docx_tables(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    try:
        with zipfile.ZipFile(file_path) as docx:
            xml_content = docx.read('word/document.xml')
            tree = ET.fromstring(xml_content)
            
            # Iterate through all tables
            for i, tbl in enumerate(tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tbl')):
                print(f"--- Table {i+1} ---")
                for tr in tbl.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr'):
                    row_cells = []
                    for tc in tr.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tc'):
                        # Get text from all paragraphs in the cell
                        cell_text = ""
                        for t in tc.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'):
                            if t.text:
                                cell_text += t.text
                        row_cells.append(cell_text)
                    print(" | ".join(row_cells))

    except Exception as e:
        print(f"Error reading docx: {e}")

if __name__ == "__main__":
    file_path = r"E:\SWP doc\COS Vision and Scope.docx" 
    read_docx_tables(file_path)
