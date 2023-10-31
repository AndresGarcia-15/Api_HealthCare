import psycopg2
from psycopg2 import DatabaseError

conexion = psycopg2.connect(user= 'healthcare_o0ig_user',
                                  password= 'RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                                  host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                                  port=5432,
                                  database='healthcare_o0ig')

     
def select_appointments(id_cita):
    try:
        with psycopg2.connect(user= 'healthcare_o0ig_user',
                                  password= 'RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                                  host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                                  port=5432,
                                  database='healthcare_o0ig') as conexion:
            with conexion.cursor() as cursor:
                sql = 'SELECT * FROM appointments WHERE id_cita = %s'
                cursor.execute(sql, (id_cita,))
                result = cursor.fetchone()
        conexion.close()
        return result
    except DatabaseError as e:
        raise e

def insert_appointments(date, time, doctor, prescription):
    try:
        with psycopg2.connect(user= 'healthcare_o0ig_user',
                                  password= 'RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                                  host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                                  port=5432,
                                  database='healthcare_o0ig') as conexion:
            with conexion.cursor() as cursor:
                sql = 'INSERT INTO appointments (date, time, doctor, prescription) VALUES (%s, %s, %s, %s)'
                cursor.execute(sql, (date, time, doctor, prescription))
                conexion.commit()
        conexion.close()
    except DatabaseError as e:
        # Manejar la excepción apropiadamente, como registrarla o devolver un error personalizado.
        raise e

def delete_appointments(id_cita):
    try:
        with psycopg2.connect(user= 'healthcare_o0ig_user',
                                  password= 'RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                                  host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                                  port=5432,
                                  database='healthcare_o0ig') as conexion:
            with conexion.cursor() as cursor:
                sql = 'DELETE FROM appointments WHERE id_cita = %s'
                cursor.execute(sql, (id_cita,))
                conexion.commit()
        conexion.close()
    except DatabaseError as e:
        # Manejar la excepción apropiadamente, como registrarla o devolver un error personalizado.
        raise e


def update_appointments(date, time, doctor, prescription, id_cita):
    try:
        with psycopg2.connect(user= 'healthcare_o0ig_user',
                                  password= 'RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                                  host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                                  port=5432,
                                  database='healthcare_o0ig') as conexion:
            with conexion.cursor() as cursor:
                sql = 'UPDATE appointments SET date = %s, time = %s, doctor = %s, prescription = %s WHERE id_cita = %s'
                cursor.execute(sql, (date, time, doctor, prescription, id_cita))
                conexion.commit()
        conexion.close()
    except DatabaseError as e:
        # Manejar la excepción apropiadamente, como registrarla o devolver un error personalizado.
        raise e
    
def select_person(id_person):
    try:
        with psycopg2.connect(user= 'healthcare_o0ig_user',
                                  password= 'RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                                  host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                                  port=5432,
                                  database='healthcare_o0ig') as conexion:
            with conexion.cursor() as cursor:
                sql = 'SELECT * FROM person WHERE id_person = %s'
                cursor.execute(sql, (id_person,))
                result = cursor.fetchone()
        conexion.close()
        return result
    except DatabaseError as e:
        # Manejar la excepción apropiadamente, como registrarla o devolver un error personalizado.
        raise e

def insert_person( typeperson, occupation):
    try:
        with psycopg2.connect(user= 'healthcare_o0ig_user',
                                  password= 'RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                                  host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                                  port=5432,
                                  database='healthcare_o0ig') as conexion:
            with conexion.cursor() as cursor:
                sql = 'INSERT INTO person (typeperson, occupation) VALUES (%s, %s)'
                cursor.execute(sql, (typeperson, occupation))
                conexion.commit()
        conexion.close()
    except DatabaseError as e:
        # Manejar la excepción apropiadamente, como registrarla o devolver un error personalizado.
        raise e

def delete_person(id_person):
    try:
        with psycopg2.connect(user= 'healthcare_o0ig_user',
                                  password= 'RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                                  host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                                  port=5432,
                                  database='healthcare_o0ig') as conexion:
            with conexion.cursor() as cursor:
                sql = 'DELETE FROM person WHERE id_person = %s'
                cursor.execute(sql, (id_person,))
                conexion.commit()
        conexion.close()
    except DatabaseError as e:
        # Manejar la excepción apropiadamente, como registrarla o devolver un error personalizado.
        raise e

def update_person(typeperson, occupation, id_person):
    try:
        with psycopg2.connect(user= 'healthcare_o0ig_user',
                                  password= 'RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                                  host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                                  port=5432,
                                  database='healthcare_o0ig') as conexion:
            with conexion.cursor() as cursor:
                sql = 'UPDATE person SET typeperson = %s, ocupation = %s WHERE id_person = %s'
                cursor.execute(sql, (typeperson, occupation, id_person))
                conexion.commit()
        conexion.close()
    except DatabaseError as e:
        # Manejar la excepción apropiadamente, como registrarla o devolver un error personalizado.
        raise e
    
def select_medicalhistorial(id):
    try:
        with psycopg2.connect(user= 'healthcare_o0ig_user',
                                  password= 'RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                                  host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                                  port=5432,
                                  database='healthcare_o0ig') as conexion:
            with conexion.cursor() as cursor:
                sql = 'SELECT * FROM medicalhistorial WHERE id = %s'
                cursor.execute(sql, (id,))
                result = cursor.fetchone()
        conexion.close()
        return result
    except DatabaseError as e:
        # Manejar la excepción apropiadamente, como registrarla o devolver un error personalizado.
        raise e

def insert_medicalhistorial(fullname, age, daybirthday, genre, placebirth, emergency_person, diseases, allergies):
    try:
        with psycopg2.connect(user= 'healthcare_o0ig_user',
                                  password= 'RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                                  host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                                  port=5432,
                                  database='healthcare_o0ig') as conexion:
            with conexion.cursor() as cursor:
                sql = 'INSERT INTO medicalhistorial (fullname, age, daybirthday, genre, placebirth, emergency_person, diseases, allergies) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
                cursor.execute(sql, (fullname, age, daybirthday, genre, placebirth, emergency_person, diseases, allergies))
                conexion.commit()
        conexion.close()
    except DatabaseError as e:
        # Manejar la excepción apropiadamente, como registrarla o devolver un error personalizado.
        raise e

def delete_medicalhistorial(id):
    try:
        with psycopg2.connect(user= 'healthcare_o0ig_user',
                                  password= 'RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                                  host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                                  port=5432,
                                  database='healthcare_o0ig') as conexion:
            with conexion.cursor() as cursor:
                sql = 'DELETE FROM medicalhistorial WHERE id = %s'
                cursor.execute(sql, (id,))
                conexion.commit()
        conexion.close()
    except DatabaseError as e:
        # Manejar la excepción apropiadamente, como registrarla o devolver un error personalizado.
        raise e

def update_medicalhistorial(fullname, age, daybirthday, genre, placebirth, emergency_person, diseases, allergies,id_medicalhistorial):
    try:
        with psycopg2.connect(user= 'healthcare_o0ig_user',
                                  password= 'RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                                  host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                                  port=5432,
                                  database='healthcare_o0ig') as conexion:
            with conexion.cursor() as cursor:
                sql = 'UPDATE medicalhistorial SET fullname = %s, age = %s, daybirthday = %s, genre = %s, placebirth = %s, emergency_person = %s, diseases = %s, allergies = %s WHERE id = %s'
                cursor.execute(sql, (fullname, age, daybirthday, genre, placebirth, emergency_person, diseases, allergies,id_medicalhistorial))
                conexion.commit()
        conexion.close()
    except DatabaseError as e:
        # Manejar la excepción apropiadamente, como registrarla o devolver un error personalizado.
        raise e