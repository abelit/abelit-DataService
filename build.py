import os
import shutil


def copy_and_overwrite(from_path, to_path):
    if os.path.exists(to_path) and os.path.isdir(to_path):
        shutil.rmtree(to_path)

    if os.path.exists(from_path) and os.path.isdir(from_path):
        print("copying dir ...")
        shutil.copytree(from_path, to_path)
    if os.path.exists(from_path) and os.path.isfile(from_path):
        print("copying file ...")
        shutil.copy(from_path,to_path)

staticdir = ['js','css','img','fonts']

for i in staticdir:
    if not os.path.exists('./static/'+i):
        os.mkdir('./static/'+i)

def build_reportweb():
    os.chdir("./reportweb")
    # os.system("npm install")
    os.system("npm run build")

    copy_and_overwrite('./dist/report_index.html','../templates/report_index.html')
    copy_and_overwrite('./dist/favicon.ico','../static/favicon.ico')

    if os.path.exists('./dist/static/js'):
        for i in os.listdir('./dist/static/js'):
            copy_and_overwrite('./dist/static/js/'+i,'../static/js/'+i)

    if os.path.exists('./dist/static/css'):
        for i in os.listdir('./dist/static/css'):
            copy_and_overwrite('./dist/static/css/'+i,'../static/css/'+i)
    if os.path.exists('./dist/static/fonts'):
        for i in os.listdir('./dist/static/fonts'):
            copy_and_overwrite('./dist/static/fonts/'+i,'../static/fonts/'+i)
    if os.path.exists('./dist/static/img'):
        for i in os.listdir('./dist/static/img'):
            copy_and_overwrite('./dist/static/img/'+i,'../static/img/'+i)
    
    os.chdir("../")

def build_ptrafficweb():
    os.chdir("./ptrafficweb")
    # os.system("npm install")
    os.system("npm run build")

    shutil.copy('./dist/ptraffic_index.html','../templates/ptraffic_index.html')

    if os.path.exists('./dist/static/js'):
        for i in os.listdir('./dist/static/js'):
            copy_and_overwrite('./dist/static/js/'+i,'../static/js/'+i)

    if os.path.exists('./dist/static/css'):
        for i in os.listdir('./dist/static/css'):
            copy_and_overwrite('./dist/static/css/'+i,'../static/css/'+i)
    if os.path.exists('./dist/static/fonts'):
        for i in os.listdir('./dist/static/fonts'):
            copy_and_overwrite('./dist/static/fonts/'+i,'../static/fonts/'+i)
    if os.path.exists('./dist/static/img'):
        for i in os.listdir('./dist/static/img'):
            copy_and_overwrite('./dist/static/img/'+i,'../static/img/'+i)

    os.chdir("../")

if __name__ == "__main__":
    build_ptrafficweb()
    # build_reportweb