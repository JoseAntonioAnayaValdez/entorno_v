from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 

app= Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://computo_066r_user:sgsNO0GgTXypqMDtftbCPVEeyp2ooBmB@dpg-culso4q3esus73b3b6g0-a.oregon-postgres.render.com/computo_066r'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Alumno(db.Model):
    __tablename__ = 'alumnos'
    no_control = db.Column(db.String, primary_key=True)
    nombre = db.Column(db.String)
    ap_paterno = db.Column(db.String)
    ap_materno = db.Column(db.String)
    semestre = db.Column(db.Integer)

    def to_dict(self):
        return{
            'no_control': self.no_control,
            'nombre': self.nombre,
            'ap_paterno': self.ap_paterno,
            'ap_materno': self.ap_materno,
            'semestre': self.semestre,
        }


@app.route('/')
def index():
    #Trae a los alumnos
    alumnos = Alumno.query.all()
    return render_template('index.html', alumnos=alumnos)

#creal alumnos
@app.route('/alumnos/new', methods=['GET', 'POST'])
def create_alumno():
    if request.method == 'POST':
        no_control = request.form['no_control']
        nombre = request.form['nombre']
        ap_paterno = request.form['ap_paterno']
        ap_materno = request.form['ap_materno']
        semestre = request.form['semestre']

        nvo_alumno = Alumno(no_control=no_control, 
                            nombre=nombre, 
                            ap_paterno=ap_paterno, 
                            ap_materno=ap_materno, 
                            semestre=semestre)
        db.session.add(nvo_alumno)
        db.session.commit()

        return redirect(url_for('index'))
    
    return render_template('create_alumno.html')

@app.route('/alumnos/delete/<string:no_control>')
def delete_alumno(no_control):
    alumno = Alumno.query.get(no_control)
    if alumno:
        db.session.delete(alumno)
        db.session.commit()
    return redirect(url_for('index'))
#-----------------------Actualizar alumno
@app.route('/alumnos/modify/<string:no_control>',  methods=['GET', 'POST'])
def uptade_alumno(no_control):
    alumno = Alumno.query.get(no_control)

    if request.method == 'POST':
        alumno.nombre = request.form['nombre']
        alumno.ap_paterno = request.form['ap_paterno']
        alumno.ap_materno = request.form['ap_materno']
        alumno.semestre = request.form['semestre']

        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update_Alumno.html', alumno=alumno)


if __name__ == '__main__':
    app.run(debug=True)