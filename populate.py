
from connect import engine ,db
from models import Program ,Course 





# program1 = Program(
#     name = "Bachelors in CS" ,
#     years_of_study = 3
# )
# 
# program2 = Program(
#     name = "Bachelors in IT" ,
#     years_of_study = 3
# )

# saving programs
# db.add_all([program1 , program2])# 
# db.commit()

# qurey for the created programs
program1 = db.query(Program).filter_by(name = "Bachelors in CS").first()

program2 = db.query(Program).filter_by(name = "Bachelors in IT").first()

# created courses object  
course1 = Course(
    title = "Python" ,
    code = "PY001" ,
)

course2 = Course(
    title = "Java" ,
    code = "J001" ,
)

course3 = Course(
    title = "C++" ,
    code = "C001" ,
)

course4 = Course(
    title = "C" ,
    code = "C002" ,
)

# adding child objects to parent object
# program1.courses.append(course1)
# program1.courses.append(course2)
# program1.courses.append(course3)
# program2.courses.append(course4)
# 
# db.commit( )