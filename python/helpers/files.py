import pathlib

""" Returns list of strings, one string for each line of file_name
Hard coded for existing directory structure for warmups

TODO: Difficulty importing module on Mac; needs work
"""
def get_contents_of_input_file_for_day(day_number, file_name):
    helpers_parent_dir = pathlib.Path(__file__).parents[1]
    input_file = pathlib.PurePath(helpers_parent_dir, 'warmup', day_number, file_name)
    with open(input_file) as file:
        return file.readlines()