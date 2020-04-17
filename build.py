import os
import shutil

os.chdir("./frontend")

os.system("npm install")

os.system("npm run build")

def copy_and_overwrite(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)

shutil.copy('./dist/index.html','../third_party_feedback/feedback/templates/index.html')
shutil.copy('./dist/favicon.ico','../third_party_feedback/feedback/static/favicon.ico')

for i in os.listdir('./dist/static'):
    copy_and_overwrite('./dist/static/'+i,'../third_party_feedback/feedback/static/'+i)