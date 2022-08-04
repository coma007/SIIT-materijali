import existDB
import xml.etree.ElementTree as ET


# Takes in a xml element from etree, and displays its contents recursively
def print_xml_element(element, indent):
    print('  '*indent+'<'+element.tag, end='')
    print_attributes(element)
    print('>', end='')

    if len(list(element)) > 0:
        print()
        for sub_elements in element:
            print_xml_element(sub_elements, indent+1)
        print('  '*indent, end='')
    else:
        print(element.text, end='')

    print('</'+element.tag+'>')


def print_attributes(element):
    for atr in element.attrib:
        print(' '+atr+'='+element.attrib[atr], end='')


def write_to_db_from_file(db, collection_name, file_path):
    file = open(file_path, 'r')
    db.create_document(collection_name, file_path.split('/')[-1], file.read())


def execute_xpath_etree(element, xpath):
    results = element.findall(xpath)
    for i, result in enumerate(results):
        print('RESULT '+str(i)+':')
        print_xml_element(result, 0)


def execute_xpath_db(db, doc_name, collection, xpath):
    results = db.read_document(doc_name, collection, xpath)
    print(results)


def execute_queries(tree, xpath, exist_db, collection, document_name):
    results = tree.findall(xpath)
    for i, result in enumerate(results):
        print('Query '+str(i)+":")
        execute_xpath_db(exist_db, document_name, collection, result.text)


if __name__ == "__main__":
    # Connecting to existDB
    exist_db = existDB.ExistDB(url="http://localhost:8090/exist/rest", username='admin', password='')

    # Writing to existDB
    # write_to_db_from_file(exist_db, 'uplatniceColl', 'data/uplatnice.xml')
    # result = exist_db.read_document('uplatnice.xml', 'uplatniceColl')
    # print(result)
    # write_to_db_from_file(exist_db, 'boooooks', 'data/books.xml')

    # XML Tree
    # tree = ET.parse('data/uplatnice.xml')
    # print_xml_element(tree.getroot(), 0)

    # XPath
    # xpath_tree = ET.parse('data/books_xpath.xml')
    # execute_xpath_etree(xpath_tree, './/expression')
    # execute_queries(xpath_tree, './/expression', exist_db, 'boooooks', 'books.xml')

    # execute_xpath_db(exist_db, 'uplatnice.xml', 'uplatniceColl','//uplata[position()=1]')
