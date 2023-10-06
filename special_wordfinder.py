from wordfinder import WordFinder


class SuperWordfinder(WordFinder):
    '''subclass extends wordfinder class to ignore
    hash marks (#) and blank lines when reading the file'''

    def new_reader(self):
        super().read_file()
        self.words = [line for line in self.words if not line.startswith(
            '#') and line.strip()]
