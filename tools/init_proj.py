#!/usr/bin/env python
"""
Initialise HDL project.
"""

import argparse
import os
import shutil
import sys

import shlex
import subprocess
from subprocess import Popen, PIPE

# TODO: Refactor to use ProjMgmt class and do more than initialise.

if __name__ == "__main__":

    # Parse arguments.
    PROJ_DIR_DEFAULT = "aHdlTemplate"
    parser = argparse.ArgumentParser(description="Initialise HDL project.")
    parser.add_argument("proj_name", help="Project name.")
    parser.add_argument("--dir_orig", "-d", default=PROJ_DIR_DEFAULT,
                        help="Original project directory name. [default:%s]" %
                        (PROJ_DIR_DEFAULT))
    args = parser.parse_args()

    # Delete .git directory after determining project path.
    path_script = os.path.dirname(os.path.realpath(__file__))
    proj_root = path_script
    while args.dir_orig != os.path.basename(proj_root):
        proj_root = os.path.split(proj_root)[0]
        if os.path.split(proj_root)[1] == "":
            print "Unable to find dir(%s)" % (args.dir_orig)
            sys.exit(-1)
    path_git = os.path.join(proj_root, ".git")
    if os.path.isdir(path_git):
        print "Removing git directory: %s" % (path_git)
        shutil.rmtree(path_git)

    # Derive lower_case and CamelCase versions of project name.
    proj_name_lc = '_'.join(args.proj_name.lower().split())
    print "lower_case project name (%s) derived from script arg (%s)." \
        % (proj_name_lc, args.proj_name)
    proj_name_cc = args.proj_name.title().replace(' ', '')
    print "CamelCase project name (%s) derived from project name (%s)." \
        % (proj_name_cc, args.proj_name)
    proj_dir = 'a' + proj_name_cc
    print "Project directory (%s) derived from project name (%s)." \
        % (proj_dir, args.proj_name)

    # Just use find, rename and sed to prepare files and directories.
    # TODO: Make this script Windows compatible.
    TEMPLATE_STR = 'sync'

    def build_rename_cmd(root, find_type, find_exec, old, new):
        str_sub = "'s/" + old + "/" + new + "/g' {}"
        if find_type is "d":
            str_end = "+" # avoid directory not found error from find
        else:
            str_end = "\;" # end exec cmd
        find_opt = "-not -path '*/\.*' -type"
        cmd = " ".join(["find", root, find_opt, find_type, "-exec", find_exec,
                        str_sub, str_end])
        return cmd

    cmds = []
    # 1. Rename directories.
    cmds.append(build_rename_cmd(proj_root, "d", "rename",
                                 TEMPLATE_STR, proj_name_lc))
    # 2. Rename files.
    cmds.append(build_rename_cmd(proj_root, "f", "rename",
                                 TEMPLATE_STR, proj_name_lc))
    # 3. Replace lower_case template strings - 'sync'.
    cmds.append(build_rename_cmd(proj_root, "f", "sed -i",
                                 TEMPLATE_STR, proj_name_lc))
    # 4. Replace CamelCase template strings - 'Sync'.
    cmds.append(build_rename_cmd(proj_root, "f", "sed -i",
                                 TEMPLATE_STR.title(), proj_name_cc))

    print("Replacing template text 'sync'.")
    for cmd in cmds:
        print("."), # Python3 print(".", end="")
        proc = Popen(shlex.split(cmd), stderr=PIPE)
        out, err = proc.communicate()
        if err:
            print("")
            print(err)
    print("")

    # Rename project directory.
    proj_dir_old = proj_root
    proj_dir_new = proj_root.replace(args.dir_orig, proj_dir)
    print "Project directory (%s) renamed to (%s)." \
        % (proj_dir_old, proj_dir_new)
    #Python 3 ? os.renames(proj_dir_old, proj_dir_new)
    shutil.move(proj_dir_old, proj_dir_new)
