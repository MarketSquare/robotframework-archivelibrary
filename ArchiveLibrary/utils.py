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
        self.directories = directories
        for dir in directories:
            curdir = os.path.join(basedir, dir)
         #   print curdir + "test"
            if not os.path.exists(curdir):
          #      print  curdir
                os.makedirs(curdir)


class Unzip(Archive):
    def extract(self, zfile, dest='.'):
        dest = os.path.abspath(dest)
        if not dest.endswith(':') and not os.path.exists(dest):
            os.mkdir(dest)

        zf = zipfile.ZipFile(zfile)
        self.extracted = []
        # create directory structure to house files
        self._createstructure(zfile, dest)

        # extract files to directory structure
        for i, name in enumerate(zf.namelist()):
           #print i
            #self.extracted.append(name)
            if not name.endswith('/'):
                self.extracted.append(name)
                if not ((name.split(".")[1] == "zip") or (name.split(".")[1] == "tar")):
                    outfile = open(os.path.join(dest, name), 'wb')
                    outfile.write(zf.read(name))
                    outfile.flush()
                    outfile.close()
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
        self.directories = directories
        for dir in directories:
            curdir = os.path.join(basedir, dir)
         #   print curdir + "test"
            if not os.path.exists(curdir):
          #      print  curdir
                os.makedirs(curdir)


class Unzip(Archive):
    def extract(self, zfile, dest='.'):
        dest = os.path.abspath(dest)
        if not dest.endswith(':') and not os.path.exists(dest):
            os.mkdir(dest)

        zf = zipfile.ZipFile(zfile)
        self.extracted = []
        # create directory structure to house files
        self._createstructure(zfile, dest)

        # extract files to directory structure
        for i, name in enumerate(zf.namelist()):
           #print i
            #self.extracted.append(name)
            if not name.endswith('/'):
                self.extracted.append(name)
                if not ((name.split(".")[1] == "zip") or (name.split(".")[1] == "tar")):
                    outfile = open(os.path.join(dest, name), 'wb')
                    outfile.write(zf.read(name))
                    outfile.flush()
                    outfile.close()
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
        self.directories = directories
        for dir in directories:
            curdir = os.path.join(basedir, dir)
         #   print curdir + "test"
            if not os.path.exists(curdir):
          #      print  curdir
                os.makedirs(curdir)


class Unzip(Archive):
    def extract(self, zfile, dest='.'):
        dest = os.path.abspath(dest)
        if not dest.endswith(':') and not os.path.exists(dest):
            os.mkdir(dest)

        zf = zipfile.ZipFile(zfile)
        self.extracted = []
        # create directory structure to house files
        self._createstructure(zfile, dest)

        # extract files to directory structure
        for i, name in enumerate(zf.namelist()):
           #print i
            #self.extracted.append(name)
            if not name.endswith('/'):
                self.extracted.append(name)
                if not ((name.split(".")[1] == "zip") or (name.split(".")[1] == "tar")):
                    outfile = open(os.path.join(dest, name), 'wb')
                    outfile.write(zf.read(name))
                    outfile.flush()
                    outfile.close()
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
        self.directories = directories
        for dir in directories:
            curdir = os.path.join(basedir, dir)
         #   print curdir + "test"
            if not os.path.exists(curdir):
          #      print  curdir
                os.makedirs(curdir)


class Unzip(Archive):
    def extract(self, zfile, dest='.'):
        dest = os.path.abspath(dest)
        if not dest.endswith(':') and not os.path.exists(dest):
            os.mkdir(dest)

        zf = zipfile.ZipFile(zfile)
        self.extracted = []
        # create directory structure to house files
        self._createstructure(zfile, dest)

        # extract files to directory structure
        for i, name in enumerate(zf.namelist()):
           #print i
            #self.extracted.append(name)
            if not name.endswith('/'):
                self.extracted.append(name)
                if not ((name.split(".")[1] == "zip") or (name.split(".")[1] == "tar")):
                    outfile = open(os.path.join(dest, name), 'wb')
                    outfile.write(zf.read(name))
                    outfile.flush()
                    outfile.close()
               elif name.split(".")[1] == "zip":
                    pass
                    #TODO : handle zip file inside an another

                    #print name.split(".")[0]
                    #if not os.path.exists(dest): os.mkdir(name.split(".")[0])




                    #nxfile = zfile + "/" +name
                    #ut.extract(zfile/name, dest/name)


        #print  enumerate(zf.namelist() )
        #return the extracted files in a list
        return self.extracted
    def _listdirs(self, zfile):
        """ Grabs all the directories in the zip structure
        This is necessary to create the structure before trying
        to extract the file to it. """

        zf = zipfile.ZipFile(zfile)
#        print zf.namelist()
        dirs = [name.rsplit('/',1)[0] for name in zf.namelist() if '/' in name ]
        #print  dirs
        #return dirs


class Untar(Archive):
    def extract(self, tfile, dest="."):
        if not dest.endswith(':') and not os.path.exists(dest):
            os.mkdir(dest)

        tff = tarfile.open(name=tfile)
        tff.extractall(dest)
    def _listdirs(self, tfile):
        """ Grabs all the directories in the tar structure
        This is necessary to create the structure before trying
        to extract the file to it. """

        tff = tarfile.open(name=tfile)
        return [name for name in tff.getnames() if name.endswith('/')]


if __name__ == "__main__":
    ut = Unzip()
    
