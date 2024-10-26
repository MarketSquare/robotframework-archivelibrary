*** Settings ***
Library           OperatingSystem
Library           ArchiveLibrary

*** Test Cases ***
Extract Zip File
    Remove Directory    ${TEMPDIR}/${/}zipout    True
    Extract Zip File    ${CURDIR}${/}test.zip    ${TEMPDIR}${/}zipout
    File Should Exist    ${TEMPDIR}${/}zipout${/}tests${/}testcase.txt

Extract Tar File
    Remove Directory    ${TEMPDIR}/${/}tarout    True
    Extract Tar File    ${CURDIR}${/}test.tar    ${TEMPDIR}${/}tarout
    File Should Exist    ${TEMPDIR}/${/}tarout${/}test${/}testcase.txt

Extract Tar Gzipped File
    Remove Directory    ${TEMPDIR}/${/}tarout    True
    Extract Tar File    ${CURDIR}${/}test.tar.gz    ${TEMPDIR}${/}tarout
    File Should Exist    ${TEMPDIR}/${/}tarout${/}test${/}testcase.txt

Extract TGZ File
    Remove Directory    ${TEMPDIR}/${/}tarout    True
    Extract Tar File    ${CURDIR}${/}test.tgz    ${TEMPDIR}${/}tarout
    File Should Exist    ${TEMPDIR}/${/}tarout${/}test${/}testcase.txt

Extract Tar Bzipped2 File
    Remove Directory    ${TEMPDIR}/${/}tarout    True
    Extract Tar File    ${CURDIR}${/}test.tar.bz2    ${TEMPDIR}${/}tarout
    File Should Exist    ${TEMPDIR}/${/}tarout${/}test${/}testcase.txt

Is File In Archive
    Archive Should Contain File    ${CURDIR}${/}test.zip    tests${/}testcase.txt
    Archive Should Contain File    ${CURDIR}${/}test.tar    test${/}testcase.txt

Extract Zip File No Folders
    Remove Directory    ${TEMPDIR}/${/}zipout    True
    Extract Zip File    ${CURDIR}${/}test-nofolders.zip    ${TEMPDIR}${/}zipout
    File Should Exist    ${TEMPDIR}${/}zipout${/}testcase.txt
    File Should Exist    ${TEMPDIR}${/}zipout${/}testcase-2.txt

Extract Zip File With Unordered Folders
    Remove Directory    ${TEMPDIR}/${/}zipout    True
    Extract Zip File    ${CURDIR}${/}test-with-unordered-folders.zip    ${TEMPDIR}${/}zipout
    ${root}    set variable    ${TEMPDIR}${/}zipout${/}main${/}
    File Should Exist    ${root}zoo${/}testcase-zoo.txt
    File Should Exist    ${root}foo${/}testcase-foo.txt

Extract Zip File Without Root Folders
    Remove Directory    ${TEMPDIR}/${/}zipout    True
    Extract Zip File    ${CURDIR}${/}test-noroots.zip    ${TEMPDIR}${/}zipout
    File Should Exist    ${TEMPDIR}${/}zipout${/}main${/}testcase.txt
    File Should Exist    ${TEMPDIR}${/}zipout${/}main${/}testcase-2.txt

Create TAR Package from files in directory
    ${tarfilename}=    set variable    newTarFile.tar
    Remove File    ${tarfilename}
    Create tar from Files in directory    ${CURDIR}${/}FilesToTar    ${tarfilename}
    Archive Should Contain File    ${tarfilename}    file1.txt
    Archive Should Contain File    ${tarfilename}    file2.txt
    Archive Should Contain File    ${tarfilename}    subdir${/}file3.txt
    Remove File    ${tarfilename}

Create TGZ Package from files in directory
    ${tarfilename}=    set variable    newTgzFile.tgz
    Remove File    ${tarfilename}
    Create tar from Files in directory    ${CURDIR}${/}FilesToTar    ${tarfilename}    tgz=True
    Archive Should Contain File    ${tarfilename}    file1.txt
    Archive Should Contain File    ${tarfilename}    file2.txt
    Archive Should Contain File    ${tarfilename}    subdir${/}file3.txt
    Remove File    ${tarfilename}

Create TAR Package from files in directory, without subdirectories
    ${tarfilename}=    set variable    newTarFile.tar
    Remove File    ${tarfilename}
    Create tar from Files in directory    ${CURDIR}${/}FilesToTar    ${tarfilename}    sub_directories=${false}
    Archive Should Contain File    ${tarfilename}    file1.txt
    Archive Should Contain File    ${tarfilename}    file2.txt
    Run Keyword And Expect Error    *does not contain value 'subdir${/}file3.txt'*    Archive Should Contain File    ${tarfilename}    subdir${/}file3.txt
    Remove File    ${tarfilename}

Create ZIP Package from files in directory
    ${zipfilename}=    set variable    newZipFile.zip
    Remove File    ${zipfilename}
    Create zip from Files in directory    ${CURDIR}${/}FilesToTar    ${zipfilename}
    Archive Should Contain File    ${zipfilename}    file1.txt
    Archive Should Contain File    ${zipfilename}    file2.txt
    Run Keyword And Expect Error    *does not contain value 'subdir${/}file3.txt'*    Archive Should Contain File    ${zipfilename}    subdir${/}file3.txt
    Remove File    ${zipfilename}

Create ZIP Package from files in directory and subdirectory
    ${zipfilename}=    set variable    newZipFile.zip
    Remove File    ${zipfilename}
    Create zip from Files in directory    ${CURDIR}${/}FilesToTar    ${zipfilename}    sub_directories=${true}
    Archive Should Contain File    ${zipfilename}    file1.txt
    Archive Should Contain File    ${zipfilename}    file2.txt
    Archive Should Contain File    ${zipfilename}    subdir${/}file3.txt
    Remove File    ${zipfilename}

Create ZIP Package from files in directory and subdirectory with no compression
    ${zipfilename}=    set variable    newZipFile.zip
    Remove File    ${zipfilename}
    Create zip from Files in directory    ${CURDIR}${/}FilesToTar    ${zipfilename}    sub_directories=${true}    compression=stored
    Archive Should Contain File    ${zipfilename}    file1.txt
    Archive Should Contain File    ${zipfilename}    file2.txt
    Archive Should Contain File    ${zipfilename}    subdir${/}file3.txt
    Remove File    ${zipfilename}

Create ZIP Package from files in same directory as files
    ${zipfilename}=    set variable    ${CURDIR}${/}FilesToTar${/}newZipFile.zip
    Remove File    ${zipfilename}
    Create zip from Files in directory    ${CURDIR}${/}FilesToTar    ${zipfilename}
    Archive Should Contain File    ${zipfilename}    file1.txt
    Archive Should Contain File    ${zipfilename}    file2.txt
    Run Keyword And Expect Error    *does not contain value 'newZipFile.zip'*    Archive Should Contain File    ${zipfilename}    newZipFile.zip
    Run Keyword And Expect Error    *does not contain value 'subdir${/}file3.txt'*    Archive Should Contain File    ${zipfilename}    subdir${/}file3.txt
    Remove File    ${zipfilename}

Create ZIP Package from files in directory and subdirectory with compression deflated
    ${zipfilename}=    set variable    newZipFile.zip
    Remove File    ${zipfilename}
    Create zip from Files in directory    ${CURDIR}${/}FilesToTar    ${zipfilename}    sub_directories=${true}    compression=deflated
    Archive Should Contain File    ${zipfilename}    file1.txt
    Archive Should Contain File    ${zipfilename}    file2.txt
    Archive Should Contain File    ${zipfilename}    subdir${/}file3.txt
    Remove File    ${zipfilename}

Create ZIP Package from files in directory and subdirectory with compression bzip2
    ${bad_python_version}=    Evaluate    float(sys.version[0:3])<3.3    modules=sys
    Run Keyword If    ${bad_python_version}    log    This compression working with python > 3.3 only!   level=WARN
    Pass Execution If  ${bad_python_version}   Rest of test skipped on this python version!
    ${zipfilename}=    set variable    newZipFile.zip
    Remove File    ${zipfilename}
    Create zip from Files in directory    ${CURDIR}${/}FilesToTar    ${zipfilename}    sub_directories=${true}    compression=bzip2
    Archive Should Contain File    ${zipfilename}    file1.txt
    Archive Should Contain File    ${zipfilename}    file2.txt
    Archive Should Contain File    ${zipfilename}    subdir${/}file3.txt
    Remove File    ${zipfilename}

Create ZIP Package from files in directory and subdirectory with compression lzma
    ${bad_python_version}=    Evaluate    float(sys.version[0:3])<3.3    modules=sys
    Run Keyword If    ${bad_python_version}    log    This compression working with python > 3.3 only!   level=WARN
    Pass Execution If  ${bad_python_version}   Rest of test skipped on this python version!
    ${zipfilename}=    set variable    newZipFile.zip
    Remove File    ${zipfilename}
    Create zip from Files in directory    ${CURDIR}${/}FilesToTar    ${zipfilename}    sub_directories=${true}    compression=lzma
    Archive Should Contain File    ${zipfilename}    file1.txt
    Archive Should Contain File    ${zipfilename}    file2.txt
    Archive Should Contain File    ${zipfilename}    subdir${/}file3.txt
    Remove File    ${zipfilename}
