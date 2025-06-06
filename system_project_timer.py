 
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
 #  Information:  http://<domain>.<ext>	###
 #
 #  The Original Code is: all of this file.
 #
 #  Contributor(s): none yet.
 #
 #  ***** END GPL LICENSE BLOCK *****

import bpy
import time
from bpy.app.handlers import persistent 

class ProjectTimerReset(bpy.types.Operator):
    bl_idname = "project_timer.reset"
    bl_label = "Reset Project Timer"
    bl_description = "Resets project timer to 0."
    bl_options = {'INTERNAL'}

    def execute(self, context):
        bpy.projectTime = 0
        return {'FINISHED'}

class ProjectTimerPreferences(bpy.types.AddonPreferences):
    # this must match the addon name, use '__package__'
    # when defining this in a submodule of a python package.
    bl_idname = __package__

    def draw(self, context):
        layout = self.layout
        layout.operator("project_timer.reset")
        
            
bpy.types.Scene.projectTime = bpy.props.IntProperty(
            name = "Project Time",
            description='All time spent on project',
            default = 0)

def draw_timer(self, context):
    projectTimerUpdate(context.scene)
            
    layout = self.layout
    seconds = bpy.projectTime
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    layout.label(text="Project Time: " + str(h)+':'+format(m, '02d')+':'+format(s, '02d'))

def projectTimerUpdate(scene):
    if not hasattr(bpy, 'projectTimestamp'): #first open
        bpy.projectTime = scene.projectTime
        bpy.projectTimestamp = int(time.time())
        print('Project Time: ', bpy.projectTime)
        print('Project Timestamp: ', bpy.projectTimestamp)
    delta = int(time.time()) - bpy.projectTimestamp
    if delta < 30:
        bpy.projectTime += delta
    bpy.projectTimestamp = int(time.time())

@persistent 
def projectTimerSave(scene):
    projectTimerUpdate(scene)
    bpy.context.scene.projectTime = bpy.projectTime if scene else 0
    print('Project Time saved', bpy.projectTime)

@persistent    
def projectTimerLoad(scene):
    bpy.projectTime = bpy.context.scene.projectTime
    bpy.projectTimestamp = int(time.time())
    print('Project Time loaded', bpy.projectTime)

# Registration

def register():
    bpy.app.handlers.load_post.append(projectTimerLoad)
    bpy.app.handlers.save_pre.append(projectTimerSave)
    bpy.types.STATUSBAR_HT_header.append(draw_timer)
    bpy.utils.register_class(ProjectTimerReset)
    bpy.utils.register_class(ProjectTimerPreferences)


def unregister():
    bpy.app.handlers.load_post.remove(projectTimerLoad)
    bpy.app.handlers.save_pre.remove(projectTimerSave)
    bpy.types.STATUSBAR_HT_header.remove(draw_timer)
    bpy.utils.unregister_class(ProjectTimerReset)
    bpy.utils.unregister_class(ProjectTimerPreferences)
    

if __name__ == "__main__":
    register()