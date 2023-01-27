import zipfile
import shutil
import os

base_dir = os.getcwd()
extraction_path = 'Extracted'
archival_path = 'Archived'


def unzip_archives(
        target_path,
        is_path_relative=True,
        in_file_ext='.zip',
        out_file_ext='.zip',
        pwd=None):
    """
    Will collect and extract all the archive file from the specified path.
    Will create a directory for the output extracted files

    Example usage:
        unzip_archives('targ\\items')
        unzip_archives('h:\\Desktop\\test', False)

        :param target_path: The target location where archive files are located
                (if nested use double slash '\\' for windows).
        :param is_path_relative: Meaning the archive file/s path are relative to script path
                If set to false, the target_path value must be absolute
        :param in_file_ext: The input archive file extension
        :param out_file_ext: The output archive file extension
        :param pwd: Password in string format, Note that this password will be used to all archives

        :return: None
    """

    zip_list = []

    if is_path_relative:
        target_extraction_path = os.path.join(base_dir, target_path, extraction_path)
        zip_file_path = os.path.join(base_dir, target_path)
    else:
        target_extraction_path = os.path.join(target_path, extraction_path)
        zip_file_path = target_path

    print(f'\nBase Directory {base_dir}')
    print(f'Target extraction path {target_extraction_path}')

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


def zip_lambdas(
        target_path,
        is_path_relative=True,
        out_file_ext='.zip'):
    """
    Compress the extracted lambda files, will create an archive file similar to the
    exported archive file of AWS Lambda, the package must be a directory with
    lambda script inside.

    Example usage:
        zip_lambdas('targ\\items\\Extracted')
        zip_lambdas('h:\\Desktop\\test', False)

        :param target_path: Target path where the directories to archive are located
        :param is_path_relative: Meaning the target directory/s path are relative to
                script path. If set to false, the target_path value must be absolute
        :param out_file_ext: File format for the archive file
        :return: None
    """

    if is_path_relative:
        target_archival_path = os.path.join(base_dir, target_path, archival_path)
        file_path = os.path.join(base_dir, target_path)
    else:
        target_archival_path = os.path.join(target_path, archival_path)
        file_path = target_path

    print(f'\nBase Directory {base_dir}')
    print(f'Target archival path {target_archival_path}')

    # Create target dir
    if not os.path.exists(target_archival_path):
        print(f'Creating output directory: {target_archival_path}')
        os.makedirs(target_archival_path)

    # Create each archive files
    for root, dirs, files in os.walk(file_path):
        if dirs:
            continue # Wait the next traversal when target files are the root dirs
        else:
            lambda_package = root.split(os.sep)[-1]

            # Do not include the output directory
            if lambda_package == archival_path:
                continue

            package_path = os.path.join(target_archival_path, lambda_package)
            print(f'Archiving contents of {package_path}')

            with zipfile.ZipFile(package_path + out_file_ext, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for file in files:
                    zip_file.write(os.path.join(root, file), file)


def zip_with_password():
    """
    Create a password-protected zip file for securing file
        :return: None
    """
    pass


def zip_with_dynamic_password():
    """
    Create multiple password-protected zip files with dynamic and random password
        :return: None
    """
    pass


def unzip_with_dynamic_password():
    """
    Extract archives with dynamic password
        :return: None
    """
    pass
