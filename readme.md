====================================
Parallel Builder for SublimeText 2
====================================

It allows you to run more than one build command in Parallel

Once you define your custom Build settings you will be able to run more than one build process at the same time.

This is plugin is ideal if you have to compile more than one LESS/SASS file in the same time, minify your javascript and so on.
I suggest you to use it combined with NODEJS and "OnSaveBuild":https://github.com/alexnj/SublimeOnSaveBuild


Usage
------------

- Put the plugin folder inside your Sublime Text2 Package folder
- Create you custom builder JSON setting the value of the "target" property to "parallel_builder" (see the following example)
- Run your Sublime Text2 Builder (Windows: CTRL + B, Mac: Cmd-B)


Example: Custom Builder
(To create your custom builder you need to go on Tools -> Build System -> New Build System more info http://docs.sublimetext.info/en/latest/reference/build_systems.html#troubleshooting-build-systems)
----------------------------------

ON OS

<pre><code>
{
    
    "working_dir": "${project_path:${folder}}",
    "target" : "parallel_builder",
    
    "cmd": {
            "Js Min":{
                "cmd": ["minifyjs", "path_to_your_js_file.js", ">", "output_path.js"]
            },
            "less file1":{
                "cmd": ["lessc", "path_to_your_LESS_file.less", "output_path.less.css"]   
            },
            "Less file2":{
                "cmd": ["lessc", "path_to_your_LESS_file2.less", "output_path2.less.css"]
            }
    }
    
}
</code></pre>

ON WINDOWS

<pre><code>
{
    
    "working_dir": "${project_path:${folder}}",
    "target" : "parallel_builder",
    
    "cmd": {
            "Js Min":{
                "cmd": ["minifyjs.cmd", "path_to_your_js_file.js", ">", "output_path.js"]
            },
            "less file1":{
                "cmd": ["lessc.cmd", "path_to_your_LESS_file.less", "output_path.less.css"]   
            },
            "Less file2":{
                "cmd": ["lessc.cmd", "path_to_your_LESS_file2.less", "output_path2.less.css"]
            }
    }
    
}
</code></pre>

More Details
------------
Once you set the property "target" to "parallel_builder", for each item of the "cmd" node you can set the command to run and also the path to your command script. In the previous example any command is already installed through Npm and set as system environment variables.
The name for each cmd node should be a short description of the command final task

Known issues
------------

Even each command is executed sequentially I suggest you to run in parallel any command for a different task without use them working the same files. For these tasks I suggest you to build a GRUNT script https://github.com/cowboy/grunt 
