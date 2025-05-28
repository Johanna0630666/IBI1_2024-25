import xml.dom.minidom as minidom 
import xml.sax
import time

# ---------------- DOM Method ----------------
dom_start = time.time()  # Start timing the DOM parsing
dom_tree = minidom.parse("C:/Users/frank/Desktop/IBI1/IBI1_2024-25/Practical 14/go_obo.xml")
terms = dom_tree.getElementsByTagName("term")  # Get all <term> elements from the DOM tree

# Track deepest term for each ontology
dom_results = {
    "molecular_function": ("", 0, ""),  # (name, is_a_count, id)
    "biological_process": ("", 0, ""),
    "cellular_component": ("", 0, "")
}

for term in terms:
    ns = term.getElementsByTagName("namespace")[0].firstChild.data
    name = term.getElementsByTagName("name")[0].firstChild.data
    go_id = term.getElementsByTagName("id")[0].firstChild.data  # Get GO ID
    is_a_list = term.getElementsByTagName("is_a")
    depth = len(is_a_list)
    if ns in dom_results and depth > dom_results[ns][1]:
        dom_results[ns] = (name, depth, go_id)

dom_end = time.time()  # End timing the DOM parsing
dom_duration = dom_end - dom_start

# Print DOM results
print("\n--- DOM Results ---")
for ns, (term_name, count, go_id) in dom_results.items():
    print(f"{ns}: GO term '{term_name}' (ID: {go_id}) has {count} <is_a> elements")
print(f"DOM parsing took {dom_duration:.4f} seconds")


# ---------------- SAX Method ----------------
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.in_term = False
        self.in_name = False
        self.in_namespace = False
        self.in_id = False
        self.in_is_a = False
        self.name = ""
        self.namespace = ""
        self.go_id = ""
        self.is_a_count = 0
        self.results = {
            "molecular_function": ("", 0, ""),
            "biological_process": ("", 0, ""),
            "cellular_component": ("", 0, "")
        }

    def startElement(self, tag, attributes):
        if tag == "term":
            self.in_term = True
            self.name = ""
            self.namespace = ""
            self.go_id = ""
            self.is_a_count = 0
        elif tag == "name":
            self.in_name = True
        elif tag == "namespace":
            self.in_namespace = True
        elif tag == "id":
            self.in_id = True
        elif tag == "is_a":
            self.in_is_a = True
            self.is_a_count += 1

    def endElement(self, tag):
        if tag == "term":
            if self.namespace in self.results and self.is_a_count > self.results[self.namespace][1]:
                self.results[self.namespace] = (self.name.strip(), self.is_a_count, self.go_id.strip())
            self.in_term = False
        elif tag == "name":
            self.in_name = False
        elif tag == "namespace":
            self.in_namespace = False
        elif tag == "id":
            self.in_id = False
        elif tag == "is_a":
            self.in_is_a = False

    def characters(self, content):
        if self.in_name:
            self.name += content
        elif self.in_namespace:
            self.namespace += content
        elif self.in_id:
            self.go_id += content

sax_start = time.time()  # Start timing the SAX parsing
parser = xml.sax.make_parser()
handler = GOHandler()
parser.setContentHandler(handler)
parser.parse("C:/Users/frank/Desktop/IBI1/IBI1_2024-25/Practical 14/go_obo.xml")
sax_end = time.time()
sax_duration = sax_end - sax_start

# Print SAX results
print("\n--- SAX Results ---")
for ns, (term_name, count, go_id) in handler.results.items():
    print(f"{ns}: GO term '{term_name}' (ID: {go_id}) has {count} <is_a> elements")
print(f"SAX parsing took {sax_duration:.4f} seconds")

# Compare speed
if dom_duration < sax_duration:
    print(f"# DOM was faster than SAX ({dom_duration:.4f} vs {sax_duration:.4f} seconds)")
else:
    print(f"# SAX was faster than DOM ({sax_duration:.4f} vs {dom_duration:.4f} seconds)")
