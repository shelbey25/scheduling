class HSClass:
    def __init__(self, name, pre, post, credits, gradeReq, sem, teacherRec, con, prestige):
        self.name = name
        self.pre = pre
        self.post = post
        self.credits = credits
        self.gradeReq = gradeReq
        self.sem = sem
        self.teacherRec = teacherRec
        self.con = con
        self.prestige = prestige

    def returnAll(self):
        return {"name": self.name, "pre": self.pre, "post": self.post, "credits": self.credits, "gradeReq": self.gradeReq, "sem": self.sem, "teacherRec": self.teacherRec, "prestige": self.prestige}
