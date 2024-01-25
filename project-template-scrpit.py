import os
import shutil

def create_project_template():
    # Define the project structure
    project_structure = {
        'src': ['__init__.py','preprocessing.py','expo-data-analysis.py','transformation.py','metrics.py','predction.py','utilis.py'],
        'docs': ['README.md'],
        'notebooks':['preprocessing.ipynb','expo-data-analysis.ipynb','modeling.ipynb','metrics.ipynb'],
        'data-for-analysis':[],

    }

    # Create the project directory
    project_dir = os.path.join(os.getcwd())
    os.makedirs(project_dir, exist_ok=True)

    # Create the project structure
    for folder, files in project_structure.items():
        folder_path = os.path.join(project_dir, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            file_path = os.path.join(folder_path, file)
            open(file_path, 'w').close()  # Create an empty file

    print(f"Project template created in: {project_dir}")

if __name__ == "__main__":
    # Create the project template
    create_project_template()
