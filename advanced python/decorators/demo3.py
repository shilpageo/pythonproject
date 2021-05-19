#

#def vaccinaion portal(**kwargs):
#     print("request id allowed location ekm")

#vaccination_portal(name="ram",age=25,address="address",health_issue=True)

#age above>65 or health_issue=True {allowed}
def decorator(fun):
     def wrapped(name,age,health_issue,place):
          if (age>65)or(health_issue==True):
            print("request id is allowed to ekm")
          else:
            raise Exception("not eligible")
            return fun(name,age,place,health_issue)
     return wrapped
@decorator
def vaccination_portal(**kwargs):
     name=kwargs["name"]
     age = kwargs["age"]
     place = kwargs["place"]
     health_issue = kwargs["health_issue"]
vaccination_portal(name="ram",age=67,place="ekm",health_issue=False)



