import os
import io
import psycopg2
from reportlab.pdfgen import canvas
from psycopg2 import DatabaseError

def generate_pdf(appointments_data):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer)

    c.drawString(100, 750, "Diagnostico de imagenes")
    
    y_position = 720  
    for diagnosticimaging in appointments_data:
        
        c.drawString(100, y_position, f"Diagnostico principal: {diagnosticimaging[0]}")
        c.drawString(60, y_position - 15, f"Diagnostico secundario: {diagnosticimaging[1]}")
        c.drawString(60, y_position - 30, f"Plande tratamiento: {diagnosticimaging[2]}")
        c.drawString(60, y_position - 45, f"Medicamentos recetados: {diagnosticimaging[3]}")
        c.drawString(60, y_position - 60, f"Procedimientos realizados: {diagnosticimaging[4]}")
        
        y_position -= 80  

    c.showPage()
    c.save()
    return buffer.getvalue()

db_connection = psycopg2.connect(
    user='healthcare_o0ig_user',
    password='RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
    host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
    port=5432,
    database='healthcare_o0ig'
)


def select_all_appointments():
    with db_connection:
        with db_connection.cursor() as cursor:
            cursor.execute('SELECT * FROM diagnosticimaging')
            return cursor.fetchall()
        
def save_pdf_to_file(data, file_path):
    with open(file_path, 'wb') as pdf_file:
        pdf_file.write(data)

try:
 
    appointments_data = select_all_appointments()

    
    pdf_data = generate_pdf(appointments_data)
    # Ruta de la carpeta de descargas
    download_folder = os.path.expanduser('~') + '\\Downloads'

    # Nombre del archivo PDF
    pdf_filename = "citas_medicas.pdf"


    pdf_file_path = os.path.join(download_folder, pdf_filename)


    save_pdf_to_file(pdf_data, pdf_file_path)

    with db_connection:
        with db_connection.cursor() as cursor:
            table_name = 'diagnosticimaging'  
            cursor.execute(f"INSERT INTO {table_name} (diagnosticimages) VALUES (%s)", (psycopg2.Binary(pdf_data),))
            db_connection.commit()
    print("PDF generado e insertado en la base de datos como bytea.")
except DatabaseError as e:
    print(f"Error al consultar la base de datos: {e}")
finally:
    db_connection.close()

