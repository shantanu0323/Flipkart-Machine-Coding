from models.user import User
from models.sprint import Sprint
from models.feature_task import FeatureTask
from models.bug_task import BugTask
from models.story_task import StoryTask

class TaskPlanner:
    def __init__(self) -> None:
        # TODO: Initialize the planner.
        self.users = {}
        self.sprints = {}
        self.features = {}
        self.stories = {}
        self.bugs = {}


    def __str__(self) -> str:
        return f"Users:\n{self.users}\nSprints:\n{self.sprints}\nFeatures:\n{self.features}\nStories:\n{self.stories}\nBugs:\n{self.bugs}\n"

    def handleCommand(self, cmd):    
        parts = cmd.split(" ")
        intent = parts[0]
        object = parts[1]
        if object == "USER":
            user = User.from_string(cmd)
            self.users[user.id] = user
        elif object == "SPRINT":
            sprint = Sprint.from_string(cmd)
            self.sprints[sprint.id] = sprint
        elif object == "FEATURE":
            feature = FeatureTask.from_string(cmd)
            self.features[feature.id] = feature
        elif object == "BUG":
            bug = BugTask.from_string(cmd)
            self.bugs[bug.id] = bug
        elif object == "STORY":
            story = StoryTask.from_string(cmd)
            self.stories[story.id] = story
        
    


