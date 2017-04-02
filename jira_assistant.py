import cmd
from jira import JIRA
from jira_functions import * 

class JiraAssistant(cmd.Cmd):
  """Tool to manage Jira tasks from CMD"""

  def do_configure(self,line):
      print "configured"

  def do_add_tasks(self, line):
      add_tasks()
      print "Added tasks"
      return

  def do_sprint_tasks(self, status=""):
      sprint_tasks(status)
      return
 
  def do_sprint_summary(self, line):
      sprint_summary()
      return

  def do_mark_issue(self, taskId):
      mark_issue(taskId)
      return

  def do_exit(self, line):
      return True;

if __name__ == '__main__':
  JiraAssistant().cmdloop()
      
