import urllib.request
import re 
from datetime import datetime, timedelta
from zipfile import ZipFile
from pathlib import Path


class FileDownloadingError(Exception):
    """Custom exception for file downloading errors."""
    pass

class FileExtractionError(Exception):
    """Custom exception for file extract errors."""
    pass

class FileProcessingError(Exception):
    """Custom exception for file processing errors."""
    pass

class PathError(Exception):
    """Cuntom exception for path errors."""
    pass


def downloading(file_address= 'https://www.histdata.com/download-free-forex-historical-data/?/excel/1-minute-bar-quotes/eurusd/2018'):
    """download a file from a URL and save it locally"""
    try:
        # URL of the ZIP file
        url = file_address
        # the above url is hidden, so we can download and upload it elsewhere,
        # then give the function our own url, just for doing this task.
        urllib.request.urlretrieve(url, 'file.zip')
    except Exception as er:
        raise FileDownloadingError(f'An error occured while downloading the file: {er}')
    else:
        print('Your file is here:', Path('file.zip').resolve())
        print('****File downloaded successfully!')
        return 'file.zip'


def unzip(filename= 'HISTDATA_COM_XLSX_EURUSD_M12018.zip'):
    """unzipping a local file and extracting."""
    dir_path = Path(filename).parent
    try:
        with ZipFile(filename) as z:
            z.extractall()
    except Exception as er:
        raise FileExtractionError(f'An error occured while extrating the file: {er}')
    else:
        print('Your extracted files are here:', dir_path.resolve())
        print('****File extracted successfully!')
        return dir_path


def opening(folderpath = Path.cwd()):
    """opening files one by one and doing some operations on them and closing."""
    try:
        folder_path = folderpath
        print(folder_path.resolve())
        print('files in folder')
        for f in folder_path.iterdir():
            if f.is_file():
                print('\t',f.name)
    except Exception as er:
        raise PathError(f'An error occured while listing files in folder path: {er}')
    else:
        print('****Files listed successfully!')
        return [f.name for f in folder_path.iterdir()]

def read_write(files_in_folder):
    """doing some file processing such as reading, writing and copying."""
    try:
        for file in files_in_folder:
            fp = Path(file)
            if fp.suffix == '.txt':
                with open(file, 'r') as infile, open(f'Copy_{fp.name}', 'w') as outfile:
                    for line in infile:
                        outfile.write(infile.readline())
                    print(fp, 'copied to ', f'Copy_{fp}')
            elif fp.suffix == '.xlsx':
                with open(file, 'rb') as infile, open(f'Copy_{fp.name}', 'wb') as outfile:
                    outfile.write(infile.read(2048))        
                    print(fp, 'copied to ', f'Copy_{fp}')

    except Exception as er:
        raise FileProcessingError(f'An error occured while processing files: {er}')
    else:
        print('****Files copied successfully!')

def show(files_in_folder):
    """showing the content of excel file. 
    Because the xlsx in a binary format, it is not easily readable with just buil_in Python functions.
    The xlsx format is essentially a ZIP file, containing XML files that represent the workbooks, sheets, and information.
    Therefore, in this task, we treat the .XLSX as ZIP archive and manually extract the XML data. 
    """
    try:
        for file in files_in_folder:
            fp = Path(file)
            if fp.suffix == '.txt':
                with open(file, 'r') as text:
                    for line in text.readlines()[:20]:
                        print(line.strip())
            elif fp.suffix == '.xlsx':
                with ZipFile(file, 'r') as excel:
                    excel.extractall()

    except Exception as er:
        raise FileProcessingError(f'An error occured while displaying the {file} content: {er}')
    else:
        print('****File content dispalyed successfully!')

def find_floats(string):
    # Use regular expression to find all float numbers in the string
    float_pattern = re.compile(r'\d+\.\d+')
    float_numbers = float_pattern.findall(string)
    
    return float_numbers

def float_to_datetime(num):
    time = datetime(1899, 12, 30)
    delta = timedelta(num)
    return time+delta

def showxl(address = Path.cwd()):
    '''displaying the content of the main sheet of the excel file as strings in the output.'''
    try:
        print("____________________________________________________________________")
        print("   Date & Time      |  Open   |  High   |   Low   |  Close  |   F   ")
        print("--------------------------------------------------------------------")
        xmlpath = Path.joinpath(address , 'xl','worksheets', 'sheet1.xml')
        with open(xmlpath, 'r') as sheet:
                for line in sheet.readlines()[2:50]:
                    nums = find_floats(line)
                    if len(nums)>0:
                        dt = float_to_datetime(float(nums[0]))
                        print(dt, "|{:>9}|{:>9}|{:>9}|{:>9}|{:>5}".format(nums[1],nums[2],nums[3],nums[4],nums[5]))
    except Exception as er:
        raise FileProcessingError(f'An error occured while displaying the {xmlpath.name} content: {er}')
    else:
        print('****File content dispalyed successfully!')                    
