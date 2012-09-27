import os
import zipfile


class ArchiveKeywords(object):
    ROBOT_LIBRARY_SCOPE = 'Global'

    def extract(self, p):
        z = zipfile.ZipFile(p)
        for f in z.namelist():
            if f.endswith('/'):
                os.makedirs(f)


if __name__ == '__main__':
    al = ArchiveKeywords()
    al.extract('master.zip')
