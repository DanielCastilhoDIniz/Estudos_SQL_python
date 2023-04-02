
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import select
from sqlalchemy import func

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey(
        "user_account.id"), nullable=False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address(id={self.id}, email={self.email_address})"


print(User.__tablename__)
print(Address.__tablename__)


# conexão  com banco de dados
engine = create_engine("sqlite://")

# criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

insetor_engine = inspect(engine)

print(insetor_engine.get_table_names())

with Session(engine) as session:
    daniel = User(
        name='Daniel',
        fullname='Daniel Castilho',
        address=[Address(email_address='danielcastilhodiniz@gmail.com')]
    )

    pedro = User(
        name='Pedro',
        fullname=' Pedro Pires',
        address=[Address(email_address='pires@gmail.com'),
                 Address(email_address='pedropires@email.com')]
    )

    lars = User(
        name='Lars',
        fullname='Lars Cado',
        address=[Address(email_address='lars@gmail.com'),
                 Address(email_address='larscado@email.com')]
    )

    # enviando para o BD (persistencia de dados)
    session.add_all([daniel, lars, pedro])

    session.commit()


stmt = select(User).where(User.name.in_(['Daniel', 'Pedro', 'Lars']))
print('\nRecuperando usuariaos a partir de condição de filtragem:')

for user in session.scalars(stmt):
    print(user)


stmt_address = select(Address).where(Address.user_id.in_([3]))
print('\nRecuperando os endereços de email do Pedro')

for address in session.scalars(stmt_address):
    print(address)

stmt_order = select(User).order_by(User.fullname.desc())
print('\nrecuperando info de maneira ordenada')
for result in session.scalars(stmt_order):
    print(result)


stmt_join = select(
    User.fullname, Address.email_address).join_from(Address, User)
for resut in session.scalars(stmt_join):
    print(result)

connetion = engine.connect()
results = connetion.execute(stmt_join).fetchall()

print("\nExecutanto statetment a partir da connetion")

for result in results:
    print(result)

stmt_count = select(func.count('')).select_from(User)
print("\nTotal de instancias em User")

for i in session.scalars(stmt_count):
    print(i)