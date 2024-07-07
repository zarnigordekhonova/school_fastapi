from database import Base
from sqlalchemy import Column, String, Integer, Boolean, Float, ForeignKey, Text
from sqlalchemy.orm import relationship


class Teachers(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(64), index=True)
    last_name = Column(String(64), index=True)
    contact_number = Column(Integer, index=True)
    timetable = relationship('Timetable', back_populates='teacher')

    def __repr__(self):
        return f"Teacher<(First name = {self.first_name}, Last name = {self.last_name})>"


class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(32), index=True)
    last_name = Column(String(32), index=True)
    age = Column(Integer, index=True)
    group_id =Column(Integer, ForeignKey('group.id'))
    group = relationship('Group', back_populates='student')

    def __repr__(self):
        return f"<Student(First name = {self.first_name}, Last name = {self.last_name}, Group = {self.group_id})>"


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(32), index=True)
    student = relationship('Students', back_populates='group')
    timetable = relationship('Timetable', back_populates='group')

    def __repr__(self):
        return f"<Group(Name = {self.name})>"


class Timetable(Base):
    __tablename__ = 'timetables'
    id = Column(Integer, primary_key=True, index=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship('Teachers', back_populates='timetable')
    group_id = Column(Integer, ForeignKey('group.id'))
    group = relationship('Group', back_populates='timetable')
    weekday_id = Column(Integer, ForeignKey('weekdays.id'))
    weekday = relationship('Weekdays', back_populates='timetable')

    def __repr__(self):
        return f"<Timetable(Teacher = {self.teacher_id}, Group = {self.group_id}, Weekday = {self.weekday_id})>"


class Weekdays(Base):
    __tablename__ = 'weekdays'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(32), index=True)
    timetable = relationship('Timetable', back_populates='weekday')
    lesson_id = Column(Integer, ForeignKey('lesson.id'))
    lesson = relationship('Lesson', back_populates='weekday')

    def __repr__(self):
        return f"<Weekday(Day = {self.name}, Para = {self.para_id})>"

class Lesson(Base):
    __tablename__ = 'lesson'
    id = Column(Integer, primary_key=True, index=True)
    number_lessons = Column(Integer, index=True)
    weekday = relationship('Weekdays', back_populates='lesson')

    def __repr__(self):
        return f"<Lessons(Number of lessons = {self.number_lessons})>"