from jira import JIRA
from config import * 
from utils import * 

# Connecting to jira

print "Connecting to Jira"
my_jira = JIRA(server=JIRA_SERVER,basic_auth=(JIRA_USERNAME, JIRA_PASSWORD))
print_seperator()
print "Connected to JIRA"
print_seperator()

"""
Update a task's status
@param issue_id
"""
def mark_issue(issue_id):
    try:
        issue = my_jira.issue(issue_id)
    except: 
        print "Error fetching the issue."
        print "Make sure the issue id is correct."
        return

    new_status = raw_input("update to status? (\"To do\", \"Done\", \" In Progress\")")
    if (not validateStatus(new_status)):
        return

    my_jira.transition_issue(issue, new_status)
    print "Issue updated to " + new_status
    
"""
Add tasks 
@param JiraInstance
"""
def add_tasks():
    print("")
    print("")
    print("-------------------- ADD TASKS --------------")
    print("")
    project = raw_input("Project??(Default : PHRM) ")
    sprint = raw_input("Sprint??")
    if (sprint == ""):
       sprint = None
    if (project == ""):
        project = "PHRM"
    while (1==1):
        summary = raw_input("Summary of the task")
        points = input("Number of sprint points")
      	new_issue = my_jira.create_issue(project=project, 
                                         summary = summary,
					 issuetype = {'name': 'Task'},
					 customfield_10004 = points,
                                         customfield_10007 = sprint)
        print "TASK CREATED SUCCESSFULLY"
      	quit = raw_input("Continue?? (Y/N)")
      	if quit == 'N' or quit == 'n' :
      	   return

"""
Lists all sprint task filtered by status
@param JiraInstance
@param status - optional
"""
def sprint_tasks(status=""):
    jql_query = ("project = " 
                + PROJECT 
                + " and sprint in openSprints()"
                + " and sprint not in futureSprints()"
                + " and assignee = currentUser()")
    if (status!="" and not validateStatus(status)):
        return
    if (status!=""):
        jql_query = jql_query + " and status = \"" + status + "\""
    issues_in_sprint = my_jira.search_issues(jql_query)

    print_seperator()
    for issue in issues_in_sprint:
        print_issue(issue)
        print_seperator()
    return    

"""
Gives summary of all tasks of this sprint
@param JiraInstance
"""
def sprint_summary():

    jql_query = ("project = " + PROJECT 
                + " and sprint in openSprints()"
                + " and sprint not in futureSprints()"
                + " and assignee = currentUser()")

    all_issues = my_jira.search_issues(jql_query)    
    issues_count = {}
    issues_points_count = {}

    for  issue in all_issues:
        status = str(issue.fields.status).upper()
        if issues_count.has_key(status):
            issues_count[status] = issues_count[status] + 1
            issues_points_count[status] = issues_points_count[status] + 1
        else:
            issues_count[status] = 1
            issues_points_count[status] = 1

    print_seperator()
    print "Project: " + PROJECT 
    print "Current sprint stats"
    print_seperator()
    for status in issues_count:
        print "Tasks in status " + status + " : " + str(issues_count[status])
        print "Points of tasks in status " + status + " : " + str(issues_points_count[status])
    print_seperator()

    return
