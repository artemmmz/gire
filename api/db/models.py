from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.dialects.postgresql import ARRAY


class Base(DeclarativeBase):
    ...


class BaseWithId(Base):
    id_ = Column(Integer, primary_key=True, unique=True, autoincrement=True)


class User(BaseWithId):
    __tablename__ = 'users'

    avatar = Column(String)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    teams = relationship('Teams', foreign_keys=['teams_members.user_id'])


class Team(BaseWithId):
    __tablename__ = 'teams'

    team_name = Column(String, nullable=False)
    slug = Column(String, nullable=False)
    avatar = Column(String)
    description = Column(String)
    address = Column(String)

    members = relationship()


class TeamMember(BaseWithId):
    __tablename__ = 'teams_members'

    team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    team = relationship(Team, back_populates='members', foreign_keys=[team_id])

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    tasks = relationship()
    created_tasks = relationship()


class Project(BaseWithId):
    __tablename__ = 'teams_projects'

    project_name = Column(String)
    avatar = Column(String)
    description = Column(String)
    columns = relationship()
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship(
        Team, foreign_keys=[team_id], back_populates='projects'
    )


class Column(BaseWithId):
    __tablename__ = 'columns'

    title = Column(String)
    project_id = Column(Integer, ForeignKey('teams_projects.id'))
    project = relationship(
        Project, back_populates='columns', foreign_keys=[project_id]
    )


class Task(Base):
    __tablename__ = 'tasks'

    title = Column(Integer)
    description = Column(String)

    for_member_id = Column(Integer, ForeignKey('teams_members.id'))
    for_member = relationship(
        TeamMember, back_populates='tasks', foreign_keys=[for_member_id]
    )

    created_by_id = Column(Integer, ForeignKey('teams_members.id'))
    created_by = relationship(
        TeamMember,
        back_populates='created_tasks',
        foreign_keys=[created_by_id]
    )

    column_id = Column(Integer, ForeignKey('columns.id'))
    column = relationship(
        Column,
        back_populates='tasks',
        foreign_keys=[column_id]
    )

    created_at = Column(DateTime)
    tags = Column(ARRAY(String))
    deadline = Column(DateTime)


class Invite(BaseWithId):
    __tablename__ = 'teams_invites'

    team_id = Column(Integer, ForeignKey('teams.id'))
    user_id = Column(Integer, ForeignKey('users.id'))


class JoinRequest(BaseWithId):
    __tablename__ = 'teams_join_requests'

    team_id = Column(Integer, ForeignKey('teams.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
