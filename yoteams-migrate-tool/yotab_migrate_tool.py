import shutil
import sys
import os

# create teamsapp.local.yml
with open("teamsapp.local.template.yml", 'r') as f:
    template = f.read()
with open("../teamsapp.local.yml", 'w') as f:
    f.write(template)

# create teamsapp.yml
with open("teamsapp.template.yml", 'r') as f:
    template = f.read()
with open("../teamsapp.yml", 'w') as f:
    f.write(template)

# create launch.json
with open("launch.template.json", 'r') as f:
    template = f.read()
with open("../.vscode/launch.json", 'w') as f:
    f.write(template)

# create tasks.json
with open("tasks.template.json", 'r') as f:
    template = f.read()
with open("../.vscode/tasks.json", 'w') as f:
    f.write(template)

# move .env to .env.local
if not os.path.exists("../env"):
    os.mkdir("../env")
shutil.copy("../.env", "../env/.env.local")

# move manifest
if not os.path.exists("../appPackage"):
    os.mkdir("../appPackage")
shutil.copy("../src/manifest/manifest.json", "../appPackage/manifest.local.json")
shutil.copy("../src/manifest/icon-outline.png", "../appPackage/icon-outline.png")
shutil.copy("../src/manifest/icon-color.png", "../appPackage/icon-color.png")

# modify package.json
with open("../package.json", 'r') as f:
    packages = f.readlines()
flag = False
line_cnt = 0
for package in packages:
    if package.find("\"eslint-plugin-n\"") != -1:
        flag = True
        break
    if package.find("\"eslint-plugin-node\":") != -1:
        pos = line_cnt
    line_cnt += 1
if not flag:
    packages.insert(pos, "    \"eslint-plugin-n\": \"^15.7.0\",\n")
with open("../package.json", 'w') as f:
    f.writelines(packages)

# modify gulp.js
with open("../gulpfile.js", 'r') as f:
    lines = f.readlines()
line_cnt = 0
for line in lines:
    if line.find("require(\"dotenv\").config()") != -1:
        lines[line_cnt] = "    require(\"dotenv\").config({ path: path.resolve(process.cwd(), \"env\", \".env.local\") });\n"
        break
    line_cnt += 1
with open("../gulpfile.js", 'w') as f:
    f.writelines(lines)