

# def show_skills(*skills):

#   print(type(skills))

#   for skill in skills:

#     print(f"{skill}")

# show_skills("Html", "CSS", "JS")

# mySkills = {
#   'Html': "80%",
#   'Css': "70%",
#   'Js': "50%",
#   'Python': "80%",
#   "Go": "40%"
# }

# def show_skills(name,*skills):

#   print(f"hello {name} \n Skills Without Progress Is: ")

#   for skill in skills :

#     print(f"-{skill}")

# show_skills("Osama","html","css","js")



mySkills = {
  'Html': "80%",
  'Css': "70%",
  'Js': "50%",
  'Python': "80%",
  "Go": "40%",
  "C#": "99%"
}

# def show_skills(**skills):
#   for skill,value in skills.items():
#     print(f"{skill} => {value}")
# show_skills(**mySkills)

myTuple = ()
def show_skills(name,*SkillWiOuAr,**SkillWiAr):
    print(f"hello {name} your skills is: \n")
    print(f"skills with out progress is:")
    if len(SkillWiOuAr) == 0:
        print("Unknown")
    else:
        for skill in SkillWiOuAr :
            print(f"- {skill}")
    
    print("\n skills with progress is: ")  
    for skill_key,skill_value in SkillWiAr.items():
      print(f"- {skill_key} => {skill_value}")

show_skills("ali ahmad",*myTuple,**mySkills)