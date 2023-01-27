import zipfile
import shutil
import os

base_dir = os.getcwd()
extraction_path = 'Extracted'

def unzip_lambdas(target_path, is_path_relative = True):
    """
    Will collect and extract all the zip file from the specified path.
    Will create a directory for the output extracted files

        :param target_path: The target location where zip files are located
                (if nested use double slash '\\' for windows).
        :param is_path_relative: Meaning the zip file/s path are relative to script path
                If set to false, the target_path value must be absolute

        :return: None
    """

    if is_path_relative:
        target_extraction_path = os.path.join(base_dir, target_path, extraction_path)
        zip_file_path = os.path.join(base_dir, target_path)
    else:
        target_extraction_path = os.path.join(target_path, extraction_path)
        zip_file_path = target_path

    print(f'\nBase Directory {base_dir}')
    print(f'Target extraction path {target_extraction_path}')
    zip_list = []

    for fyl in os.listdir(zip_file_path):
        if fyl.endswith('.zip'):
            zip_list.append(os.path.join(zip_file_path, fyl))

    # If the target directory does not exist yet
    if zip_list:
        if not os.path.exists(target_extraction_path):
            print(f'Creating output directory: {target_extraction_path}')
            os.makedirs(target_extraction_path)

    print('-----------')

    # Begin the extraction
    for fyl in zip_list:
        print(f'Extracting: {fyl}')

        zip_filename = fyl.split(os.sep)[-1].replace('.zip', '')
        current_zip_extraction_path = os.path.join(target_extraction_path, zip_filename)

        # Extract all the contents of zip file into target directory
        with zipfile.ZipFile(fyl, 'r') as zipObj:
            zipObj.extractall(current_zip_extraction_path)

def zip_lambdas():

    # Create target dir
    zip_archive = "Packaged_lambdas"
    lambda_handler = "lambda_handler"

    zip_archive_abs_path = os.path.abspath(zip_archive)

    if not os.path.exists(zip_archive_abs_path):
        os.mkdir(zip_archive_abs_path)

    for file in os.listdir(base_dir):
        test_file = os.path.abspath(file)
        if os.path.isdir(test_file) and test_file != zip_archive_abs_path:
            lambda_zip = zip_archive_abs_path + '/' + file
            shutil.make_archive(lambda_zip, 'zip', test_file)

unzip_lambdas('targ\\items')
# unzip_lambdas('h:\\Desktop\\test', False)