from database import Base, engine
from models import Teachers, Timetable, Students, Weekdays, Lesson, Group

Base.metadata.create_all(bind=engine)