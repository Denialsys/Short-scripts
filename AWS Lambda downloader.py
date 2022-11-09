'''
    Author: Jenver I.

    Script used for backing up multiple lambda functions
    This will list all of the lambda functions available in the target region
    Also this will execute under the credentials of the user of the provided access keys
'''


import boto3
import json
import requests
import inspect

session = boto3.Session(
    aws_access_key_id="",
    aws_secret_access_key="",
    region_name=""
)

lambda_client = None

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def get_lambda_details():

    pagination_marker = '1'
    lambda_list = []
    lambda_list_logs = 'Findings/details/lambda_details.json'
    lambda_name_list_logs = 'Findings/details/lambda_name_list.txt'
    try:
        for fetch_iter in range(10):
            if pagination_marker == '1':
                function_list = lambda_client.list_functions()
            elif pagination_marker:
                function_list = lambda_client.list_functions(Marker=pagination_marker)
            else:
                break

            if function_list.get('Functions'):
                pagination_marker = function_list.get('NextMarker')

                for functions in function_list.get('Functions'):
                    lambda_list.append(functions)

        ## Log the function details to file
        with open(lambda_list_logs, 'w') as outfile:
            json.dump(lambda_list, outfile)

        ## Log all the function name
        lambda_function_names = [function.get("FunctionName") for function in lambda_list]
        with open(lambda_name_list_logs, 'w') as outfile:
            json.dump(lambda_function_names, outfile)

        print(f'Total lambda found {len(lambda_list)}')
        print(f'Please see /{lambda_name_list_logs} for function names')
        # for functions in lambda_list:
        #     print(functions.get('FunctionName'))

    except Exception as e:
        print(f'[Error] {inspect.stack()[0][3]}, {e.args}')

    return lambda_list

def download_lambda(function_list):
    try:
        functions_dir = 'Findings/files/'
        for function in function_list:
            print(f'Attempting download {function.get("FunctionName")}...', end='  ')
            current_function = lambda_client.get_function(FunctionName=function.get('FunctionName'))
            request = requests.get(
                current_function.get('Code').get('Location'),
                allow_redirects=True
            )
            if 'zip' in request.headers.get("Content-Type"):
                with open(f'{functions_dir}{function.get("FunctionName")}.zip', 'wb') as function_zip:
                    function_zip.write(request.content)

                print(f'{functions_dir}{function.get("FunctionName")}.zip was created')
            else:
                print(f'Download failed', end='\n')

    except Exception as e:
        print(f'[Error] {inspect.stack()[0][3]}, {e.args}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # global lambda_client
    lambda_client = session.client('lambda')
    lambda_list = get_lambda_details()
    download_lambda(lambda_list)
