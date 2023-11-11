import os
import io
import psycopg2
from reportlab.pdfgen import canvas
from psycopg2 import DatabaseError

def generate_pdf(appointments_data):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer)

    c.drawString(100, 750, "Citas Médicas")
    
    y_position = 720  # Posición vertical inicial
    for appointment in appointments_data:
        # Agrega los detalles de cada cita médica al PDF
        c.drawString(100, y_position, f"ID Cita: {appointment[0]}")
        c.drawString(60, y_position - 15, f"Fecha: {appointment[1]}")
        c.drawString(60, y_position - 30, f"Hora: {appointment[2]}")
        c.drawString(60, y_position - 45, f"Doctor: {appointment[3]}")
        c.drawString(60, y_position - 60, f"Prescripción: {appointment[4]}")
        
        y_position -= 80  # Ajusta la posición vertical para la siguiente cita

    c.showPage()
    c.save()
    return buffer.getvalue()

# Configura la conexión a la base de datos
db_connection = psycopg2.connect(
    user='healthcare_o0ig_user',
    password='RW6WWdFotQmdTMaifvkfNW9JTfk87As6',
    host='dpg-cl058g2s1bgc738vdvn0-a.oregon-postgres.render.com',
    port=5432,
    database='healthcare_o0ig'
)

# Consulta todos los registros de la tabla "appointments"
def select_all_appointments():
    with db_connection:
        with db_connection.cursor() as cursor:
            cursor.execute('SELECT * FROM appointments')
            return cursor.fetchall()
        
def save_pdf_to_file(data, file_path):
    with open(file_path, 'wb') as pdf_file:
        pdf_file.write(data)

try:
    # Consulta todos los registros de la tabla "appointments"
    appointments_data = select_all_appointments()

    # Genera el PDF con la información de las citas médicas
    pdf_data = generate_pdf(appointments_data)
    # Ruta de la carpeta de descargas
    download_folder = os.path.expanduser('~') + '\\Downloads'

    # Nombre del archivo PDF
    pdf_filename = "citas_medicas.pdf"

    # Ruta completa del archivo PDF en la carpeta de descargas
    pdf_file_path = os.path.join(download_folder, pdf_filename)

    # Guardar el PDF en la carpeta de descargas
    save_pdf_to_file(pdf_data, pdf_file_path)

    with db_connection:
        with db_connection.cursor() as cursor:
            table_name = 'diagnosticimaging'  # Nombre de la tabla
            cursor.execute(f"INSERT INTO {table_name} (diagnosticimages) VALUES (%s)", (psycopg2.Binary(pdf_data),))
            db_connection.commit()
    print("PDF generado e insertado en la base de datos como bytea.")
except DatabaseError as e:
    print(f"Error al consultar la base de datos: {e}")
finally:
    db_connection.close()

