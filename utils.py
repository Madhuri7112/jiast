
def print_seperator():
    print ""
    print "-----------------------------------------------------"
    return

def validateStatus(status):
    validStatus = ['DONE',
                    'TO DO',
                    'IN PROGRESS']

    if status.upper() in validStatus:
        return True

    print "Not a valid state for issue"
    print "valid states are: "
    for status in validStatus:
        print "   " + status

    return False

def print_issue(issue):
    print "Id:  " + str(issue)
    print "Task summary:  " + issue.fields.summary
    print "Task points:  " + str(issue.fields.customfield_10004)
    print "Status:  " + str(issue.fields.status)






