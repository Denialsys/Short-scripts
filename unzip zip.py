import zipfile
import shutil
import os

base_dir = os.getcwd()
extraction_path = 'Extracted'

def unzip_archives(
        target_path,
        is_path_relative = True,
        in_file_ext = '.zip',
        out_file_ext = '.zip',
        pwd = None):

    """
    Will collect and extract all the archive file from the specified path.
    Will create a directory for the output extracted files

        :param target_path: The target location where archive files are located
                (if nested use double slash '\\' for windows).
        :param is_path_relative: Meaning the archive file/s path are relative to script path
                If set to false, the target_path value must be absolute
        :param in_file_ext: The input archive file extension
        :param out_file_ext: The output archive file extension
        :param pwd: Password in string format, Note that this password will be used to all archives

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

    # Gather the files to extract
    for fyl in os.listdir(zip_file_path):
        if fyl.endswith(in_file_ext):
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

        zip_filename = fyl.split(os.sep)[-1].replace(out_file_ext, '')
        current_zip_extraction_path = os.path.join(target_extraction_path, zip_filename)

        # Extract all the contents of zip file into target directory
        # Use password if password was specified
        with zipfile.ZipFile(fyl, 'r') as zipObj:
            if pwd:
                zipObj.extractall(current_zip_extraction_path, pwd=bytes(pwd, 'utf-8'))
            else:
                zipObj.extractall(current_zip_extraction_path)

def zip_with_password():
    """
    Create a password-protected zip file for securing file
        :return: None
    """
    pass


def zip_with_dynamic_password():
    """
    Create a password-protected zip file with dynamic and random password
        :return: None
    """
    pass

def unzip_with_dynamic_password():
    """
    Extract archives with dynamic password
        :return: None
    """
    pass

def zip_lambdas():
    """
    Compress the extracted lambda files
        :return: None
    """
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

# unzip_archives('targ\\items')
# unzip_archives('h:\\Desktop\\test', False)
