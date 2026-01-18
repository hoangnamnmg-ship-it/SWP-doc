
import zipfile
import xml.etree.ElementTree as ET
import sys
import os

def read_docx_section_3_2(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    try:
        with zipfile.ZipFile(file_path) as docx:
            xml_content = docx.read('word/document.xml')
            tree = ET.fromstring(xml_content)
            
            namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            
            text_parts = []
            capture = False
            
            for node in tree.iter():
                if node.tag.endswith('}p'):
                    # Check for section headers (simplified check)
                    node_text = "".join([t.text for t in node.iter() if t.tag.endswith('}t') and t.text])
                    if "3.2" in node_text and "Priorities" in node_text:
                        capture = True
                        text_parts.append(f"\n[SECTION START: {node_text}]\n")
                    elif "3.3" in node_text and capture:
                        capture = False
                        break
                    
                    if capture:
                         text_parts.append(node_text + "\n")

            print("".join(text_parts))
            
    except Exception as e:
        print(f"Error reading docx: {e}")

if __name__ == "__main__":
    file_path = r"E:\SWP doc\COS Vision and Scope.docx" 
    read_docx_section_3_2(file_path)
