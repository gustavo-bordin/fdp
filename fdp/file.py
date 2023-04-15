import re
from os import path



class FDPFile:
    def __init__(self, file_path):
        self._file_path = file_path
        self._pdf_path = None
        self._content = None

    def read(self):
        with open(self._file_path, 'r') as f:
            first_line = f.readline()
            self._parse_pdf(first_line)
            content = f.read()
            self._set_content(content)

    @property
    def content(self):
        return self._content

    @property
    def pdf_path(self):
        return self._pdf_path

    def _set_content(self, content):
        self._content = content

    def _set_pdf_path(self, pdf_path):
        self._pdf_path = pdf_path

    def _is_pdf_path_valid(self, pdf_file_path):
        pdf_file_exists = path.exists(pdf_file_path)
        return pdf_file_exists

    def _parse_pdf(self, first_line):
        pdf_file_match = re.search('(?<=").*(?=")', first_line)

        if not pdf_file_match:
            raise Exception("PDF file reference not found")

        pdf_file_path = pdf_file_match.group()
        is_valid_path = self._is_pdf_path_valid(pdf_file_path)
        if is_valid_path:
            self._set_pdf_path(pdf_file_path)
            return

        raise Exception("PDF path is not valid")
