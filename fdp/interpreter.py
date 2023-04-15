import json
import fitz


class PDFInterpreter:
    def __init__(self, instructions, pdf_file_path):
        self.instructions = instructions
        self.pdf_file_path = pdf_file_path

    def run(self):
        with fitz.open(self.pdf_file_path) as doc:
            result = {}
            for instruction in self.instructions:
                label = instruction['label']
                after = instruction['after']
                before = instruction['before']
                result[label] = self.find_instruction(after, before, doc)

            return json.dumps(result, ensure_ascii=False, indent=2)

    def iter_pages(self, doc):
        for page in doc:
            yield page

    def find_instruction(self, after, before, doc):
        for page in self.iter_pages(doc):
            page_text = page.get_text("text")
            if after in page_text:
                start_index = page_text.find(after) + len(after)
                end_index = page_text.find(before, start_index)
                if end_index == -1:
                    break

                return page_text[start_index:end_index].strip()

        return ""
