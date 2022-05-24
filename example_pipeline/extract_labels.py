from xml.etree import cElementTree as ET
import os

def extractLabels(folder, out_dir):
    files = os.listdir(folder)
    for filename in files:
        if 'xml' in filename:
            dir = os.path.join(folder, filename)
            with open(dir, 'r') as f:
                tree = ET.parse(f)
                root = tree.getroot()
                new_filename = "labels_" + filename.replace("xml", "txt")
            with open(out_dir + new_filename, "w") as Outfile:
                for aspectTerms in root.iter('aspectTerms'):
                    for aspectTerm in root.iter('aspectTerm'):
                        line = aspectTerm.attrib['term']
                        Outfile.write(line + " \n")
                Outfile.close()
            f.close()

if __name__ == "__main__":
    extractLabels("../data", "../data/")
