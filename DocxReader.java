import java.io.*;
import java.util.zip.*;
import javax.xml.parsers.*;
import org.w3c.dom.*;

public class DocxReader {
    public static void main(String[] args) {
        File file = new File("G6_RDS .docx");
        if (!file.exists()) {
            System.out.println("File not found: " + file.getAbsolutePath());
            return;
        }

        try (ZipFile zip = new ZipFile(file)) {
            ZipEntry entry = zip.getEntry("word/document.xml");
            if (entry == null) {
                System.out.println("Not a valid docx file (missing word/document.xml)");
                return;
            }

            try (InputStream is = zip.getInputStream(entry)) {
                DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
                factory.setNamespaceAware(true);
                DocumentBuilder builder = factory.newDocumentBuilder();
                Document doc = builder.parse(is);

                printNode(doc.getDocumentElement());
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void printNode(Node node) {
        String name = node.getNodeName();
        // Simple heuristic for paragraphs to add a newline
        if (name.endsWith(":p") || name.equals("p")) { 
             System.out.println();
        }
        
        // w:t is the text node
        if ((name.endsWith(":t") || name.equals("t")) && node.getTextContent() != null) {
            System.out.print(node.getTextContent() + " ");
        }
        
        NodeList children = node.getChildNodes();
        for (int i = 0; i < children.getLength(); i++) {
            printNode(children.item(i));
        }
    }
}
