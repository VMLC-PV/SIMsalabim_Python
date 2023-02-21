import json,requests,os,git,shutil,uuid,platform,zipfile,io,asyncio
import tkinter as tk
from tkinter import messagebox
from SIMsalabim_utils.CompileProg import *


def download_simsalabim(path2prog=None):
    """Download SIMsalabim from GitHub and extract the files to the current working directory

    Parameters
    ----------
    path : str, optional
        Path to the directory where SIMsalabim will be downloaded, by default None\\
        If None, SIMsalabim will be downloaded to the current working directory in a folder named 'SIMsalabim'

    """    
    if path2prog is None:
        cwd = os.getcwd() # Get current working directory
        path2prog = os.path.join(cwd, 'SIMsalabim')

    folders = []
    folder_name = 'kostergroup-SIMsalabim-'
    for dirpath, dirnames, files in os.walk(cwd):
        for dirname in dirnames:
            if dirname.startswith(folder_name):
                # Pop out dialog box to confirm overwriting
                root = tk.Tk()
                root.withdraw()
                result = messagebox.askyesno("Confirm", "Are you sure you want to overwrite the 'SIMsalabim' folder?")
                if result == True:
                    shutil.rmtree(os.path.join(cwd,dirname))
                    print(f"Found a folder named {dirname}")
                # break
            # else:
            #     print("No folder found that starts with 'folder'")

    if os.path.exists(path2prog):
        # Pop out dialog box to confirm overwriting
        root = tk.Tk()
        root.withdraw()
        result = messagebox.askyesno("Confirm", "Are you sure you want to overwrite the 'SIMsalabim' folder?")
        if result == True:
            # Rename folder
            shutil.rmtree(path2prog)

            # # Get the files from the latest release
            url = 'https://api.github.com/repos/kostergroup/SIMsalabim/zipball'
            response = requests.get(url)

            # Open the zip file
            z = zipfile.ZipFile(io.BytesIO(response.content))

            # Extract all the files
            z.extractall(path=cwd)

            for dirpath, dirnames, files in os.walk(cwd):
                for dirname in dirnames:
                    if dirname.startswith(folder_name):
                        # Rename folder
                        shutil.move(os.path.join(cwd, dirname), path2prog)
                        break
        else:
            print(' We are keeping the current SIMsalabim version')
    else:
        # # Get the files from the latest release
        url = 'https://api.github.com/repos/kostergroup/SIMsalabim/zipball'
        response = requests.get(url)

        # Open the zip file
        z = zipfile.ZipFile(io.BytesIO(response.content))

        # Extract all the files
        z.extractall(path=cwd)

        for dirpath, dirnames, files in os.walk(cwd):
            for dirname in dirnames:
                if dirname.startswith(folder_name):
                    # print(f"Found a folder named {dirname}")
                    # Rename folder
                    shutil.move(os.path.join(cwd, dirname), path2prog)
                    break


    try :
        # Check if fpc is installed
        fpc = os.popen('fpc -h').read()
        print('fpc is installed so we are compiling the SIMsalabim programs')
        # Compile the programs
        fpc_prog('simss',os.path.join(path2prog,'SimSS'),show_term_output=False,force_fpc=True,verbose=False)
        fpc_prog('zimt',os.path.join(path2prog,'ZimT'),show_term_output=False,force_fpc=True,verbose=False)

        print('SIMsalabim programs have been compiled successfully!')

    except:
        print('')
        print('fpc is not installed so we are skipping the compilation of the SIMsalabim programs')
        print('For now we are downloading the pre-compiled binaries from GitHub')
        print('')
        print('If the binaries do not work or if you want to compile the SIMsalabim programs yourself, please install fpc.')
        print('For more information, please visit: https://www.freepascal.org/')
        print('')
        # # Get the assets from the latest release
        url = "https://api.github.com/repos/kostergroup/SIMsalabim/releases/latest"
        response = requests.get(url)
        data = json.loads(response.text)


        for asset in data["assets"]:
            download_url = asset["browser_download_url"]
            filename = asset["name"]
            response = requests.get(download_url)
            open(os.path.join(cwd,filename), "wb").write(response.content)


        for dirpath, dirnames, files in os.walk(cwd):

            for filename in files:
                if filename.startswith('simss') and os.path.exists(os.path.join(cwd, filename)):
                    # print(f"Found a folder named {filename}")
                    # Rename folder
                    shutil.move(os.path.join(cwd, filename), os.path.join(cwd, 'SIMsalabim','SimSS',filename))
                elif filename.startswith('zimt') and os.path.exists(os.path.join(cwd, filename)):
                    # print(f"Found a folder named {filename}")
                    # Rename folder
                    shutil.move(os.path.join(cwd, filename), os.path.join(cwd, 'SIMsalabim','ZimT',filename))
                else:
                    pass


if __name__ == '__main__':
    print('Downloading SIMsalabim from GitHub')
    print('For more information, please visit:')
    print('https://github.com/kostergroup/SIMsalabim')
    print('')
    print('This may take a few seconds...')
    print('Please wait...')

    download_simsalabim() # Download SIMsalabim

    print('')
    print('SIMsalabim has been downloaded successfully!')

             


