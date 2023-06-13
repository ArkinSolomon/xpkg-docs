# Copyright (c) 2023. Arkin Solomon.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied limitations under the License.

'''
This script combines all of the scripts within the subdirectories into the
sidebar under their appropriate sections, instead of having to make the sidebar
manually using docsify. The README.md within each subdirectory must exist, and
will be the reference point for each main category.
'''

import os
import shutil

output_dir = './out/'
sidebar_output = './out/_sidebar.md'
src_dir = './docs/'

root_copy_files = ['index.html', 'README.md', '.nojekyll']

sidebar_content = ''

def fileNameToTitle(name: str) -> str:
  name = name.replace('.md', '')
  splitStr = name.split('-')
  finalWord = []
  for word in splitStr:
    if word == 'xpkg':
      word = 'X-Pkg'
    elif not word in ['and', 'the', 'but', 'of', 'for']:
      word = word.capitalize()
    finalWord.append(word)    
  return ' '.join(finalWord)

def processSubdir(subdir: str) -> None: 
  global sidebar_content
  sidebar_title = fileNameToTitle(subdir)
  sidebar_content += f'- [{sidebar_title}]({subdir + ".md"})\n'
  for file in os.listdir(src_dir + subdir):
    if file == 'README.md':
      dest_file_name = subdir + '.md'
      shutil.copyfile(src_dir + subdir + '/' + file, output_dir + dest_file_name)
    else:
      page_name = fileNameToTitle(file)
      sidebar_content += f'  * [{page_name}]({file})\n'
      shutil.copyfile(src_dir + subdir + '/' + file, output_dir + file)

try:
  shutil.rmtree(output_dir)
except:
  pass
os.makedirs(output_dir)

# Insert order of subdirectories here
processSubdir('package-developers')
processSubdir('xpkg-developers')

for file in root_copy_files: 
  shutil.copyfile(src_dir + file, output_dir + file)

with open(sidebar_output, 'w') as file:  
  file.write(sidebar_content)