import sublime
import sublime_plugin


class ParallelBuilderCommand(sublime_plugin.WindowCommand):
    def run(self, **args):
        cmd = args.get("cmd")
        if isinstance(cmd, dict):

            self.tasks = cmd
            self.taskNames = self.tasks.keys()
            self.mainArgs = args

            self._run_all_tasks()

    def _run_all_tasks(self):

        for task in self.taskNames:
            print 'Building:' + task
            currTask = self.mainArgs
            currTask.update(self.tasks[task])
            try:
                self.window.run_command("exec", currTask)
            except:
                sublime.error_message("Unexpected error!")
