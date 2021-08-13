from services.task_planner import TaskPlanner

if __name__ == "__main__":
    """
    CREATE USER id name email
    CREATE SPRINT id name
    CREATE FEATURE id title creator_id assignee_id due_date <LOW/MODERATE/HIGH> summary
    CREATE BUG id title creator_id assignee_id due_date <P0/P1/P2>
    CREATE STORY id title creator_id assignee_id due_date summary <sprint_id/Empty>
    """
    commands = [
        "CREATE USER U1 User1 u1@gmail.com",
        "CREATE USER U2 User2 u2@gmail.com",
        "CREATE USER U3 User3 u3@gmail.com",

        "CREATE SPRINT SP1 Sprint-1",

        "CREATE FEATURE F1 Feature-1 U1 U2 2021-11-07 LOW summary",

        "CREATE BUG B1 Bug-1 U1 U2 2021-11-07 P1",

        "CREATE STORY ST1 Story-1 U1 U2 2021-11-07 summary S1"
    ]

    task_planner = TaskPlanner()
    for cmd in commands:
        task_planner.handleCommand(cmd)

    print (task_planner)
