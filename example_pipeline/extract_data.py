from xml.etree import cElementTree as ET
import os
def extractXML(folder, out_dir):
    files = os.listdir(folder)
    for filename in files:
        if 'xml' in filename:
            dir = os.path.join(folder, filename)
            #file_name = os.path.basename(dir)
            with open(dir, 'r') as f:
                tree = ET.parse(f)
                root = tree.getroot()
                new_filename = filename.replace("xml", "txt")
            with open(out_dir + new_filename, "w") as Outfile:
                for page in root.iter('text'):
                    line = str(page.text)
                    Outfile.write(line + " \n")
                Outfile.close()
            f.close()

if __name__ == "__main__":
    extractXML("../data", '../data/cleanData/')
