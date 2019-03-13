#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, time

# Watches for file changes and starts a build if file changed

extension_to_watch = ".tex"

watch_files = []

def walklevel(some_dir, level=1):
	some_dir = some_dir.rstrip(os.path.sep)
	assert os.path.isdir(some_dir)
	num_sep = some_dir.count(os.path.sep)
	for root, dirs, files in os.walk(some_dir):
		yield root, dirs, files
		num_sep_this = root.count(os.path.sep)
		if num_sep + level <= num_sep_this:
			del dirs[:]


# Get files to watch
for root, dirs, files in walklevel("./"):
	files = [f for f in files if not f[0] == '.']
	dirs[:] = [d for d in dirs if not d[0] == '.']
	for file in files:
		if file.endswith(extension_to_watch):
			watch_files.append(os.path.join(root, file))

print("Watching these files for changes:")
print("  \n".join(watch_files))

before = dict ([(f, os.stat(f).st_mtime) for f in watch_files])

while 1:
	time.sleep(1)
	now = dict ([(f, os.stat(f).st_mtime) for f in watch_files])
	changed = [f for f in now if not now[f] == before[f] ]
	if changed:
		for f in changed:
			print (("Change in file %s") %(f))
			cmd = "make -C" + "\"" + os.path.dirname(f) + "\""
			os.system(cmd)
	before = now
