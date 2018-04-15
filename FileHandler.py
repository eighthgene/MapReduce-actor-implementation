import os


class FileHandler(object):
    """FileHandler class
    Manages splitting input files and joining outputs together.

    """

    def __init__(self, input_file_path, output_dir):
        """
        Note: the input file path should be given for splitting.
        The output directory is needed for joining the outputs.
        :param input_file_path: input file path
        :param output_dir: output directory path
        """
        self.input_file_path = input_file_path
        self.output_dir = output_dir
        self.default_input_dir = output_dir
        self.number_of_splits = None

    def initiate_file_split(self, split_index, index):
        """initialize a split file by opening and adding an index.
        :param split_index: the split index we are currently on, to be used for naming the file.
        :param index: the index given to the file.
        """
        file_split = open(self.get_input_split_file(split_index - 1), "w+")
        file_split.write(str(index) + "\n")
        return file_split

    @classmethod
    def is_on_split_position(cls, character, index, split_size, current_split):
        """Check if it is the right time to split.
        i.e: character is a space and the limit has been reached.
        :param character: the character we are currently on.
        :param index: the index we are currently on.
        :param split_size: the size of each single split.
        :param current_split: the split we are currently on.
        """
        return index > split_size * current_split + 1 and character.isspace()

    def split_file(self, number_of_splits):
        """split a file into multiple files.
        note: this has not been optimized to avoid overhead.
        :param number_of_splits: the number of chunks to
        split the file into.
        """
        self.number_of_splits = number_of_splits
        file_size = os.path.getsize(self.input_file_path)
        unit_size = file_size / number_of_splits + 1
        original_file = open(self.input_file_path, "r")
        file_content = original_file.read()
        original_file.close()
        (index, current_split_index) = (1, 1)
        current_split_unit = self.initiate_file_split(current_split_index, index)
        for character in file_content:
            current_split_unit.write(character)
            if self.is_on_split_position(character, index, unit_size, current_split_index):
                current_split_unit.close()
                current_split_index += 1
                current_split_unit = self.initiate_file_split(current_split_index, index)
            index += 1
        current_split_unit.close()

    def get_input_split_file(self, index, input_dir=None, extension=".txt"):
        """
        Return the name of the current split file corresponding to the given index
        :param index:  index of chank
        :param input_dir: directory of chank
        :param extension: extension
        :return: path of split file
        """
        if not (input_dir is None):
            return input_dir + "/file_" + str(index) + extension
        return self.default_input_dir + "/file_" + str(index) + extension

    def clear(self):
        """
        Method for delete all temporary files, chunks of file.
        """
        for i in range(self.number_of_splits):
            os.unlink(self.output_dir + "/file_" + str(i) + ".txt")
        print 'Cleaning temp files...'
