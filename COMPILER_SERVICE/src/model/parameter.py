class Parameter:
    def __init__(self, file_path, folder_path):
        self.file_path = file_path
        self.folder_path = folder_path

    def get_file_path(self):
        return self.file_path

    def get_folder_path(self):
        return self.folder_path
