from datetime import datetime
Column, Integer, Float, DateTime, String, Text = None
db = None

class Base:
    pass

# Column, Integer, Float, DateTime, String, Text

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(120), nullable=False, unique=True)
    password = Column(String(120), nullable=False)
    created_at = Column(DateTime(), default=datetime.now())
    
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "created_at": self.created_at
        }
          
""" INSERT """
# INSERT INTO users (username, password) VALUES ('lrodriguez', '123456');

user = User() # creando una instacion de usuario
user.username = "lrodriguez"
user.password = "123456"

db.session.add(user) # Preparando el SQL
db.session.commit() # Guarda el usuario en la base de datos

""" SELECT """
# SELECT * FROM users;
users = User.query.all() # todos => [<User 1>, <User 2>]

# SELECT * FROM users WHERE id = 1;
user = User.query.get(1) # un usuario por la pk (primary key) => <User 1>

# SELECT * FROM users WHERE username = 'lrodriguez';
user = User.query.filter_by(username='lrodriguez') # [<User 1>]
user = User.query.filter_by(username='lrodriguez').first() # <User 1>


""" UPDATE """
# UPDATE users SET password='1234567890' WHERE id = 1;
user = User.query.get(1)
user.password = "1234567890"
db.session.commit()

""" DELETE """
# DELETE FROM users WHERE id = 1
user = User.query.get(1) # buscamos el usuario que queremos eliminar
db.session.delete(user) # eliminamos el usuario
db.session.commit() # confirmar la eliminacion

# DELETE FROM users;
error = False
users = User.query.all()
for user in users:
    try:
        db.session.delete(user)  
    except:
        error = True      
        
if error:
    db.session.rollback() # Deshace los cambios
else:
    db.session.commit() # Confirma los cambios

