
toDo={
     "monday":"play football",
      "Tuesday":"dance",
       "wednesday":"skip",
        "Thursday":"bake",
         "friday":"out",
          "saturday":"dance",
          "sunday":"eat chicken"
 }
def get_all_to_do():
     return f"<ul>{to_do_do}</ul>"
def to_do_do():
    li=""
    for key in toDo:
        li=li+f"<li><h1>on: <b>{key}</b> we {toDo[key]}</h1></li>"
        return li

        

    