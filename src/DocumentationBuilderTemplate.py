from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('src/templates'))

from src.Utility import getFilesFromDirectory, addFilesToDictionary, readFiles
from src.ReferenceBuilderTemplate import ReferenceBuilderTemplate

class DocumentationBuilderTemplate:
    def __init__(self, directory, commentDenotion, filterList):
        self.directory = directory
        self.commentDenotion = commentDenotion
        self.filterList = filterList

    def createReferences(self):
        allFiles = getFilesFromDirectory(self.directory, self.filterList)
    
        fileNames = []
        for f in allFiles:
            fileNames.append(f.name)

        for i in range(0, len(allFiles)):
            dictionary = {}
            files = [allFiles[i]]

            addFilesToDictionary(files, dictionary)
            readFiles(files, self.commentDenotion, dictionary)
            ReferenceBuilderTemplate(files, dictionary).createReferences(allFiles[i].name, fileNames)

    def createIndex(self):
        template = env.get_template('index.html')
        with open("docs/index.html", 'w+') as file:
            template_data = template.render()
            file.write(template_data)

    def createDocumentation(self):
        print("Generating documentation.....")
        self.createIndex()
        self.createReferences()