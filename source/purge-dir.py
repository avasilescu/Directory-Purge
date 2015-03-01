import os, time, shutil

def purgeDir(dir, age):
    print "Scanning:", dir
    age = age * 86400
    for f in os.listdir(dir):
        now = time.time()
        filepath = os.path.join(dir, f)
        modified = os.stat(filepath).st_mtime      
        print 'Inspecting: %s (%s) - Current: %s' % (f, modified, now)
        #if modified < (now - age):
        if (now - modified) > age:           
            if os.path.isfile(filepath):
                os.remove(filepath)
                print 'Deleted: %s (%s)' % (f, modified)
            if os.path.isdir(filepath):
                shutil.rmtree(filepath)
                print 'Deleted: %s (%s)' % (f, modified)

# 1 Day	= 86400 seconds

#Replace [FOLDER] with the absolute folder path. If running on Windows, use "\\" to replace "\".
#Example "E:\\Downloads"

purgeDir('[FOLDER]', 30)