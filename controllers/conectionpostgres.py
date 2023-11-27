import psycopg2
from psycopg2 import DatabaseError
from fastapi import HTTPException
from fastapi.responses import JSONResponse
import base64
import os
import io
import psycopg2
from reportlab.pdfgen import canvas
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
    except DatabaseError as e:
        
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
    except DatabaseError as e:
        
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
    except DatabaseError as e:
        
        raise e
    
def select_person(id_person):
    try:
        with psycopg2.connect(user= 'healthcare_o0ig_user',
                                  password= 'RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                                  host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                                  port=5432,
                                  database='healthcare_o0ig')       as conexion:
            with conexion.cursor() as cursor:
                sql = 'SELECT * FROM person WHERE id_person = %s'
                cursor.execute(sql, (id_person,))
                result = cursor.fetchone()
        return result
    except DatabaseError as e:
        
        raise e

def insert_person( typeperson, occupation):
    try:
        with psycopg2.connect(user= 'healthcare_o0ig_user',
                                  password= 'RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                                  host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                                  port=5432,
                                  database='healthcare_o0ig') as conexion:
            with conexion.cursor() as cursor:
                sql = 'INSERT INTO person (typeperson, ocupation) VALUES (%s, %s)'
                cursor.execute(sql, (typeperson, occupation))
                conexion.commit()
    except DatabaseError as e:
    
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
    except DatabaseError as e:
    
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
    except DatabaseError as e:
        
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
        return result
    except DatabaseError as e:
        
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
    except DatabaseError as e:
       
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
    except DatabaseError as e:
        
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
    except DatabaseError as e:
        
        raise e
    

def get_pdf_json(llave_images):
    try:
        with psycopg2.connect(user= 'healthcare_o0ig_user',
                                  password= 'RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                                  host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                                  port=5432,
                                  database='healthcare_o0ig') as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT diagnosticimages FROM diagnosticimaging WHERE llave_images = %s;", (llave_images,))
                pdf_data = cursor.fetchone()
                if pdf_data:
                    pdf_bytes = pdf_data[0]
                    # Codificar los datos binarios en base64
                    pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')
                    return JSONResponse(content={"pdf_data": pdf_base64})
                else:
                    raise HTTPException(status_code=404, detail="Registro no encontrado")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en la base de datos: {e}")
    

'''
def generate_pdf(diagnosticimaging_data):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer)

    c.drawString(100, 750, "Diagnostico de imagen")
    
    y_position = 720  # Posición vertical inicial
    for diagnosticimaging in diagnosticimaging_data:
        # Agrega los detalles de cada cita médica al PDF
        c.drawString(100, y_position, f"diagnostico principal: {diagnosticimaging[0]}")
        c.drawString(60, y_position - 15, f"diagnosticos_secundarios: {diagnosticimaging[1]}")
        c.drawString(60, y_position - 30, f"plan_de_tratamiento: {diagnosticimaging[2]}")
        c.drawString(60, y_position - 45, f"medicamentos_recetados: {diagnosticimaging[3]}")
        c.drawString(60, y_position - 60, f"procedimientos_realizados: {diagnosticimaging[4]}")
        
        y_position -= 80  # Ajusta la posición vertical para la siguiente cita

    c.showPage()
    c.save()
    return buffer.getvalue()


# Consulta todos los registros de la tabla "appointments"
def select_all_appointments():
    with conexion:
        with conexion.cursor() as cursor:
            cursor.execute('SELECT * FROM diagnosticimaging')
            return cursor.fetchall()
try:
    # Consulta todos los registros de la tabla "appointments"
    diagnosticimaging_data = select_all_appointments()

    # Genera el PDF con la información de las citas médicas
    pdf_data = generate_pdf(diagnosticimaging_data)

    with conexion:
        with conexion.cursor() as cursor:
            table_name = 'diagnosticimaging'  # Nombre de la tabla
            cursor.execute(f"INSERT INTO {table_name} (diagnosticimages) VALUES (%s)", (psycopg2.Binary(pdf_data),))
            conexion.commit()
    print("PDF generado e insertado en la base de datos como bytea.")
except DatabaseError as e:
    print(f"Error al consultar la base de datos: {e}")
finally:
    conexion.close()

'''

def insert_diagnosticimaging(diagnostico_principal, diagnosticos_secundarios, plan_de_tratamiento, medicamentos_recetados, procedimientos_realizados):
    try:
        with psycopg2.connect(user='healthcare_o0ig_user',
                              password='RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                              host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                              port=5432,
                              database='healthcare_o0ig') as conexion:
            with conexion.cursor() as cursor:
                sql = 'INSERT INTO diagnosticimaging (diagnostico_principal, diagnosticos_secundarios, plan_de_tratamiento, medicamentos_recetados, procedimientos_realizados) VALUES (%s, %s, %s, %s,%s)'
                cursor.execute(sql, (diagnostico_principal, diagnosticos_secundarios, plan_de_tratamiento, medicamentos_recetados, procedimientos_realizados))
                conexion.commit()
    except DatabaseError as e:
        raise e

def select_diagnosticimaging(llave_images):
    try:
        with psycopg2.connect(user='healthcare_o0ig_user',
                              password='RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                              host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                              port=5432,
                              database='healthcare_o0ig')       as conexion:
            with conexion.cursor() as cursor:
                sql = 'SELECT * FROM diagnosticimaging WHERE id_diagnostic = %s'
                cursor.execute(sql, (llave_images,))
                result = cursor.fetchone()
        return result
    except DatabaseError as e:
        raise e
    
def delete_diagnosticimaging_by_id(diagnosticimaging_id):
    try:
        with psycopg2.connect(user='healthcare_o0ig_user',
                              password='RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                              host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                              port=5432,
                              database='healthcare_o0ig') as conexion:
            with conexion.cursor() as cursor:
                sql = 'DELETE FROM diagnosticimaging WHERE id_diagnostic = %s'
                cursor.execute(sql, (diagnosticimaging_id,))
                conexion.commit()
    except DatabaseError as e:
        raise e   


def insert_person(id_auth,email,username):
    try:
        with psycopg2.connect(user='healthcare_o0ig_user',
                              password='RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                              host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                              port=5432,
                              database='healthcare_o0ig') as conexion:
            with conexion.cursor() as cursor:
                sql = 'INSERT INTO person (id_auth, email, username) VALUES (%s, %s, %s)'
                cursor.execute(sql, (id_auth, email, username))
                conexion.commit()
    except DatabaseError as e:
        raise e

def update_person_role(id_auth, typeperson='patient'):
    try:
        with psycopg2.connect(user='healthcare_o0ig_user',
                              password='RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                              host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                              port=5432,
                              database='healthcare_o0ig') as conexion:
            with conexion.cursor() as cursor:
                # Asegurarse de que el rol sea 'admin' o 'patient'
                typeperson = 'admin' if typeperson == 'admin' else 'patient'
                
                sql = 'UPDATE person SET typeperson = %s WHERE id_auth = %s'
                cursor.execute(sql, (typeperson, id_auth))
                conexion.commit()
    except DatabaseError as e:
        raise e

    
def insert_person(id_auth, email, username, is_admin=False):
    try:
        with psycopg2.connect(user='healthcare_o0ig_user',
                              password='RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                              host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                              port=5432,
                              database='healthcare_o0ig') as conexion:
            with conexion.cursor() as cursor:
                sql = 'INSERT INTO person (id_auth, email, username, role) VALUES (%s, %s, %s, %s)'
                
                # Determinar el rol del usuario
                role = 'admin' if is_admin else 'patient'
                
                cursor.execute(sql, (id_auth, email, username, role))
                conexion.commit()
    except DatabaseError as e:
        raise e




def allusers():
    try:
        with psycopg2.connect(user='healthcare_o0ig_user',
                              password='RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                              host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                              port=5432,
                              database='healthcare_o0ig') as conexion:
            with conexion.cursor() as cursor:
                cursor.execute('SELECT * FROM person')
                return cursor.fetchall()
    except DatabaseError as e:
        raise e


def id_user(id_auth):
    try:
        with psycopg2.connect(user='healthcare_o0ig_user',
                              password='RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                              host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                              port=5432,
                              database='healthcare_o0ig') as conexion:
            with conexion.cursor() as cursor:
                sql = 'SELECT * FROM person WHERE id_auth = %s'
                cursor.execute(sql, (id_auth,))
                result = cursor.fetchone()
        return result
    except DatabaseError as e:
        raise e

    

def insert_laboratory(test1, test2, test3, test4, test5):
    try:
        with psycopg2.connect(user='healthcare_o0ig_user',
                              password='RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                              host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                              port=5432,
                              database='healthcare_o0ig') as conexion:
            with conexion.cursor() as cursor:
                sql = 'INSERT INTO laboratorytests (test1, test2, test3, test4, test5) VALUES (%s, %s, %s, %s,%s)'
                cursor.execute(sql, (test1, test2, test3, test4, test5))
                conexion.commit()
    except DatabaseError as e:
        raise e

def select_laboratory(testid):
    try:
        with psycopg2.connect(user='healthcare_o0ig_user',
                              password='RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                              host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                              port=5432,
                              database='healthcare_o0ig')       as conexion:
            with conexion.cursor() as cursor:
                sql = 'SELECT * FROM laboratorytests WHERE testid = %s'
                cursor.execute(sql, (testid,))
                result = cursor.fetchone()
        return result
    except DatabaseError as e:
        raise e
    
def delete_laboratory(testid):
    try:
        with psycopg2.connect(user='healthcare_o0ig_user',
                              password='RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
                              host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
                              port=5432,
                              database='healthcare_o0ig') as conexion:
            with conexion.cursor() as cursor:
                sql = 'DELETE FROM laboratorytests WHERE testid = %s'
                cursor.execute(sql, (testid,))
                conexion.commit()
    except DatabaseError as e:
        raise e

