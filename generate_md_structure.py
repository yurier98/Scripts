import os


def generate_md_structure2(root_dir, file_name, padding='    '):
    with open(file_name, 'w') as f:
        f.write(f"{padding}.\n")
        f.write(
            f"{padding}├── {os.path.basename(root_dir)}  # Directorio raíz que contiene todos los archivos de la API\n")

        for dirpath, dirnames, filenames in os.walk(root_dir):
            level = dirpath.replace(root_dir, '').count(os.sep)
            indent = padding * (level + 1)
            f.write(f"{indent}├── {os.path.basename(dirpath)}")  # Nombre del directorio

            if level > 0:
                f.write(f"  # Módulo que contiene los archivos relacionados con {os.path.basename(dirpath)}")
            f.write('\n')

            subindent = padding * (level + 2)
            for filename in filenames:
                f.write(f"{subindent }│   ├── {filename}  # Archivo que contiene {os.path.basename(dirpath)}\n")

            if not filenames:
                f.write(f"{subindent}└── (No hay archivos en este directorio)\n")

        f.write('\n')

def generate_md_structure(root_dir, file_name, padding='    '):
    with open(file_name, 'w') as f:
        f.write(f"{padding}.\n")
        f.write(f"{padding}├── {os.path.basename(root_dir)}  # Directorio raíz que contiene todos los archivos de la API\n")

        for dirpath, dirnames, filenames in os.walk(root_dir):
            level = dirpath.replace(root_dir, '').count(os.sep)
            indent = padding * (level + 1)
            f.write(f"{indent}├── {os.path.basename(dirpath)}")  # Nombre del directorio

            if level > 0:
                f.write(f"  # Módulo que contiene los archivos relacionados con {os.path.basename(dirpath)}")
            f.write('\n')

            subindent = padding * (level + 2)
            for dirname in dirnames:
                if dirname == '__pycache__':
                    continue
                subdirpath = os.path.join(dirpath, dirname)
                sublevel = subdirpath.replace(root_dir, '').count(os.sep)
                subindent = padding * (sublevel + 2)
                f.write(f"{subindent}├── {dirname}  # Subdirectorio\n")

            if filenames:
                for filename in filenames:
                    f.write(f"{subindent}├── {filename}  # Archivo que contiene {os.path.basename(dirpath)}\n")
            else:
                f.write(f"{subindent}└── (No hay archivos en este directorio)\n")

        f.write('\n')


#
# def generate_md_structure(root_dir, file_name, padding='    '):
#     with open(file_name, 'w') as f:
#         f.write(f"{padding}.\n")
#         f.write(f"{padding}├── {os.path.basename(root_dir)}  # Directorio raíz que contiene todos los archivos de la API\n")
#
#         for dirpath, dirnames, filenames in os.walk(root_dir):
#             level = dirpath.replace(root_dir, '').count(os.sep)
#             indent = padding * (level + 1)
#             f.write(f"{indent}├── {os.path.basename(dirpath)}")  # Nombre del directorio
#
#             if level > 0:
#                 f.write(f"  # Módulo que contiene los archivos relacionados con {os.path.basename(dirpath)}")
#             f.write('\n')
#
#             subindent = padding * (level + 2)
#             for dirname in dirnames:
#                 subdirpath = os.path.join(dirpath, dirname)
#                 sublevel = subdirpath.replace(root_dir, '').count(os.sep)
#                 subindent = padding * (sublevel + 2)
#                 f.write(f"{subindent}├── {dirname}  # Subdirectorio\n")
#
#             if filenames:
#                 for filename in filenames:
#                     f.write(f"{subindent}├── {filename}  # Archivo que contiene {os.path.basename(dirpath)}\n")
#             else:
#                 f.write(f"{subindent}└── (No hay archivos en este directorio)\n")
#
#         f.write('\n')

if __name__ == '__main__':
    root_dir = '.'  # Cambiar por la ruta del directorio raíz del proyecto
    file_name = 'project_structure.md'
    generate_md_structure(root_dir, file_name)
