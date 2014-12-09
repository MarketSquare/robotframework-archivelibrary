import os
import zipfile
import tarfile

""" Originally from

 http://code.activestate.com/recipes/252508/

 heavily refactored since

"""


class Archive(object):

    def _createstructure(self, file, dir):
        self._makedirs(self._listdirs(file), dir)

    def _makedirs(self, directories, basedir):
        """ Create any directories that don't currently exist """
        for dir in directories:
            curdir = os.path.join(basedir, dir)
            if not os.path.exists(curdir):
                os.makedirs(curdir)


class Unzip(Archive):
    def extract(self, zfile, dest='.'):
        dest = os.path.abspath(dest)
        if not dest.endswith(':') and not os.path.exists(dest):
            os.makedirs(dest)

        zf = zipfile.ZipFile(zfile)

        # create directory structure to house files
        self._createstructure(zfile, dest)

        # extract files to directory structure
        for i, name in enumerate(zf.namelist()):
            if not name.endswith('/'):
                outfile = open(os.path.join(dest, name), 'wb')
                outfile.write(zf.read(name))
                outfile.flush()
                outfile.close()

    def _listdirs(self, zfile):
        """ Grabs all the directories in the zip structure
        This is necessary to create the structure before trying
        to extract the file to it. """

        zf = zipfile.ZipFile(zfile)

        dirs = set()
        for name in zf.namelist():
            if name.endswith('/'):
                dirs.add(name)
            elif '/' in name:
                path = name[0:name.rindex('/')]
                dirs.add(path)

        return dirs


class Untar(Archive):
    def extract(self, tfile, dest="."):
        if not dest.endswith(':') and not os.path.exists(dest):
            os.makedirs(dest)

        tff = tarfile.open(name=tfile)
        tff.extractall(dest)

    def _listdirs(self, tfile):
        """ Grabs all the directories in the tar structure
        This is necessary to create the structure before trying
        to extract the file to it. """

        tff = tarfile.open(name=tfile)
        return [name for name in tff.getnames() if name.endswith('/')]


if __name__ == "__main__":
    ut = Untar()
    ut.extract(r"/tmp/test.tar", r"/tmp/testout")
