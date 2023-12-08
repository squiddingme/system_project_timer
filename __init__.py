 
 #  ***** BEGIN GPL LICENSE BLOCK *****
 #
 #  This program is free software: you can redistribute it and/or modify
 #  it under the terms of the GNU General Public License as published by
 #  the Free Software Foundation, either version 3 of the License, or
 #  (at your option) any later version.
 #
 #  This program is distributed in the hope that it will be useful,
 #  but WITHOUT ANY WARRANTY; without even the implied warranty of
 #  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 #  GNU General Public License for more details.
 #
 #  You should have received a copy of the GNU General Public License
 #  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 #
 #  The Original Code is Copyright (C) 2013 by Marcin Zielinski
 #  All rights reserved.
 #
 #  Contact:      martin.zielinsky@gmail.com
 #  Information:  http://<domain>.<ext> ###
 #
 #  The Original Code is: all of this file.
 #
 #  Contributor(s): none yet.
 #
 #  ***** END GPL LICENSE BLOCK *****

bl_info = {
    "name": "Project Timer",
    "author": "Martin Zielinski",
    "version": (1, 5),
    "blender": (2, 80, 0),
    "location": "Info",
    "description": "Shows time spent on project",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "System"}

if "bpy" in locals():
    from importlib import reload
    if "system_project_timer" in locals():
        reload(system_project_timer)
else:
    from .system_project_timer import *

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()