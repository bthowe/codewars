class FileMaster():
    def __init__(self, filepath):
        self.filepath = filepath

    def extension(self):
        return self.filepath.split('.')[1]

    def filename(self):
        return self.filepath.split('.')[0].split('/')[-1]

    def dirpath(self):
        return '/'.join(self.filepath.split('.')[0].split('/')[:-1])+'/'

if __name__=="__main__":
    master = FileMaster('/Users/person1/Pictures/house.png')
    print master.extension()
    print master.filename()
    print master.dirpath()
