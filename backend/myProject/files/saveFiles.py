from pdf2image import convert_from_path
import os


def saveFiles(files, i):
    newFiles = []
    poppler_path = r'myProject/files/poppler-0.68.0_x86/poppler-0.68.0/bin'
    for file in files:
        # when the type file is pdf
        if file.filename.endswith('pdf'):
            file.save(f'myProject/files/file/{i}{file.filename}')
            pages = convert_from_path(pdf_path=f'myProject/files/file/{i}{file.filename}', dpi=500, poppler_path=poppler_path)
            for page in pages:
                path = f'myProject/files/file/{i}{file.name}.png'
                page.save(f'{path}')
            newFiles.append(f'{path}')
            os.remove(f'myProject/files/file/{i}{file.filename}')
        # when the type file is jpg
        elif file.filename.lower().endswith('jpg'):
            path = f'myProject/files/file/{i}{file.name}.png'
            file.save(f'{path}')
            newFiles.append(f'{path}')
        # when the type file is png
        else:
            path = f'myProject/files/file/{i}{file.name}.png'
            file.save(f'{path}')
            newFiles.append(f'{path}')

    return newFiles
