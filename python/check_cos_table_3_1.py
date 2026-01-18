
import zipfile
import xml.etree.ElementTree as ET
import sys
import os

def read_docx_section_3_1(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    try:
        with zipfile.ZipFile(file_path) as docx:
            xml_content = docx.read('word/document.xml')
            tree = ET.fromstring(xml_content)
            
            namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            
            capture = False
            
            # Simple iteration to find table text or section text near 3.1
            for node in tree.iter():
                 # Look for paragraph text
                if node.tag.endswith('}p'):
                    node_text = "".join([t.text for t in node.iter() if t.tag.endswith('}t') and t.text])
                    if "3.1" in node_text and "Stakeholder" in node_text:
                        print(f"\n[SECTION FOUND: {node_text}]")
                        capture = True
                    elif "3.2" in node_text:
                        capture = False
                
                # Look for table rows if we are in the section or generally
                if node.tag.endswith('}tr'):
                    # Get all text in the row
                    row_text = []
                    for cell in node.iter():
                         if cell.tag.endswith('}tc'):
                             cell_text = "".join([t.text for t in cell.iter() if t.tag.endswith('}t') and t.text])
                             row_text.append(cell_text)
                    
                    # Check if this looks like the stakeholder table header
                    if any("Value" in t for t in row_text) and any("Benefit" in t for t in row_text):
                         print(f"Table Row Found: {row_text}")

            
    except Exception as e:
        print(f"Error reading docx: {e}")

if __name__ == "__main__":
    file_path = r"E:\SWP doc\COS Vision and Scope.docx" 
    read_docx_section_3_1(file_path)
