"""The main app file that contains the instantiation of the beer game app and all the endpoints of the app"""

from flask import Flask, g, render_template,request,redirect,session,make_response, flash
import os
import bcrypt
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

app=Flask(__name__)
app.secret_key=os.urandom(24)


from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt
app.config.from_object('config.Config')

db.init_app(app)
from models import *

@app.route('/')
def home():
    """Homepage"""
    return render_template('index.html')

@app.route('/instructor_login')
def instructor_login():
    if g.instructor:
        return redirect("/instructor")

    """Login as instructor frontend"""
    return render_template('instructor_login.html')    

@app.route('/instructor_register')
def instructor_register():
    """Register an instructor frontend"""
    return render_template('instructor_register.html')    

@app.route('/student_login')
def student_login():
    if g.student:
        return redirect("/student_dashboard")

    """Login as instructor frontend"""
    return render_template('student_login.html')   

@app.route('/choose_roles')
def choose_roles():
    """Homepage for choosing roles"""
    return render_template('choose_roles.html') 

@app.route('/student_register')
def student_about():
    """Register an instructor frontend"""
    return render_template('student_register.html')    

@app.route('/game_instructions')
def game_instructions():
    """Frontend for the instructions of the game"""
    return render_template('game_instructions.html')

@app.route('/instructor')
def instructor():
    """Homepage for the instructor"""
    return render_template('instructor.html')

@app.route('/instructor_dashboard')
def instructor_dashboard():
    """ If the instructor is not logged in, redirect to login """
    if not g.instructor:
        return redirect("/instructor_login")
    instructor = Instructor.query.filter_by(email=session['instructor_email']).first()
    session['instructor_name'] = instructor.name

    games = Game.query.filter_by(instructor_id = instructor.id).all()

    """Dashboard for the instructor"""
    return render_template('instructor_dashboard.html', games = games)

@app.route('/student_dashboard')
def student_dashboard():
    if not g.student:
        return redirect("/student_login")

    student = Student.query.filter_by(email=session['student_email']).first()
    session['student_name'] = student.username

    games = Game.query.all()
    # instructor_name = ""
    # game_info_arr = []
    # for game in games:
    #     if instructor_name != game['instructor']['name']:
    #         instructor_name = game['instructor']['name']
    #         count = Game.query.filter_by(instructor['name'] == instructor_name).count()
    #         game_info_arr.append(instructor_name, count)

    """Dashboard for the student"""
    # game = Game.query.filter_by(instructor='Jacobs University').first()
    return render_template('student_dashboard.html', games=games)

@app.route('/game_creation')
def game_creation():
    """Game creation frontend"""
    return render_template('game_creation.html')

@app.route('/game_screen1')
def game_screen1():
    """Frontend for the Game Screen"""
    if not g.student:
        return redirect("/student_login")

    student = Student.query.filter_by(email=session['student_email']).first()
    session['student_name'] = student.username
    games = Game.query.all()
    return render_template('game_screen1.html', games=games)

@app.route('/game_screen2')
def game_screen2():
    """Frontend for the Game Screen"""
    if not g.student:
        return redirect("/student_login")

    student = Student.query.filter_by(email=session['student_email']).first()
    session['student_name'] = student.username
    games = Game.query.all()
    return render_template('game_screen2.html', games=games)

@app.route('/game_screen3')
def game_screen3():
    """Frontend for the Game Screen"""
    if not g.student:
        return redirect("/student_login")

    student = Student.query.filter_by(email=session['student_email']).first()
    session['student_name'] = student.username
    games = Game.query.all()
    return render_template('game_screen3.html', games=games)

@app.route('/game_screen4')
def game_screen14():
    """Frontend for the Game Screen"""
    if not g.student:
        return redirect("/student_login")

    student = Student.query.filter_by(email=session['student_email']).first()
    session['student_name'] = student.username
    games = Game.query.all()
    return render_template('game_screen4.html', games=games)

@app.route('/create_instructor', methods=['GET', 'POST'])
def create_instructor():
    """Create a instructor via query string parameters."""
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    if name and email and password:
        existing_instructor = Instructor.query.filter(
            Instructor.email == email
        ).first()
        if existing_instructor:
            flash(f'{email} already exists!')
            return redirect("/instructor_login")
        new_instructor = Instructor(
            name=name,
            email=email,
            password=password,
        )
        db.session.add(new_instructor)
        db.session.commit()
        flash ('Account successfully created! Please login')
        return redirect("/instructor_login")
    else:
        flash ('Missing details')
        return redirect("/instructor_register")

@app.route('/create_student', methods=['GET', 'POST'])
def create_student():
    """Create a student via query string parameters."""
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    if username and email and password:
        existing_student = Student.query.filter(
            Student.email == email
        ).first()
        if existing_student:
            flash (f'{email} already exists!')
            return redirect("/student_login")
        new_student = Student(
            username=username,
            email=email,
            password=password,
        )
        db.session.add(new_student)
        db.session.commit()
        flash ('Account successfully created! Please login')
        return redirect("/student_login")
    else:
        flash ('Missing details')
        return redirect("/student_register")

@app.before_request
def before_request():
    g.instructor = None
    g.student = None

    if 'instructor_email' in session:
        user = [x for x in Instructor.query if x.email == session['instructor_email']][0]
        g.instructor = user

    if 'student_email' in session:
        user = [x for x in Student.query if x.email == session['student_email']][0]
        g.student = user

@app.route('/instructor_login_check', methods=['GET', 'POST'])
def instructor_login_check():
    """Password check for instructor backend"""
    email = request.form.get('email')
    password = request.form.get('password')
    if email and password:
        existing_instructor = Instructor.query.filter(
            Instructor.email == email
        ).filter(
            Instructor.password == password
        ).first()
        if existing_instructor:
            session['instructor_email'] = email
            return redirect("/instructor")
        else:
            flash('Wrong credentials')
            return redirect("/instructor_login")
    else:
        flash("Missing details")
        return redirect("/instructor_login")

@app.route('/instructor_logout')
def instructor_logout():
    """Instructor logout"""
    session.pop('instructor_email', None)
    return redirect("/instructor_login")

@app.route('/student_login_check', methods=['GET', 'POST'])
def student_login_check():
    """Password check for student/player backend"""
    email = request.form.get('email')
    password = request.form.get('password')
    if email and password:
        existing_student = Student.query.filter(
            Student.email == email
        ).filter(
            Student.password == password
        ).first()
        if existing_student:
            session['student_email'] = email
            return redirect("/student_dashboard")
        else:
            flash('Wrong credentials')
            return redirect("/student_login")
    else:
        flash("Missing details")
        return redirect("/student_login")

@app.route('/student_logout')
def student_logout():
    """Student logout"""
    session.pop('student_email', None)
    return redirect("/student_login")

@app.route('/create_game', methods=['GET', 'POST'])
def create_game():
    """Create individual games backend"""
    email = request.form.get('email')
    user_password = request.form.get('password')
    institute = request.form.get('institute')
    games = request.form.get('games', type=int)

    if email and user_password and institute and games:
        existing_instructor = Instructor.query.filter(
            Instructor.email == email
        ).filter(
            Instructor.password == user_password
        ).first()
        if existing_instructor:
            games = int(games)
            for i in range(games):
                new_game = Game(
                    session_length=10,
                    distributor_present=True,
                    wholesaler_present=True,
                    holding_cost=4,
                    backlog_cost=8,
                    session_id=1,
                    instructor=existing_instructor,
                    active=True,
                    info_sharing=True,
                    info_delay=2,
                    rounds_complete = 0,
                    is_default_game=False,
                    starting_inventory=10,
                    instructor_id=existing_instructor.id,

                )
                db.session.add(new_game)
                db.session.commit()
                response = "Created games with IDs: " + f'{new_game.id},'
            return redirect("/instructor_dashboard")
        else:
            flash("Wrong credentials")
        return redirect("/game_creation")
    else:
        flash("Missing details")
        return redirect("/game_creation")

@app.route('/reset_game/<game_id>', methods=['GET', 'POST'])
def reset_game(game_id):
    """Reset a specific game"""
    instructor = Instructor.query.filter_by(email=session['instructor_email']).first()
    session['instructor_name'] = instructor.name
    game = Game.query.filter_by(id = game_id, instructor_id = instructor.id).first()
    if game :
        game.holding_cost = 0
        game.backlog_cost = 0
    db.session.commit()
    return redirect("/instructor_dashboard")

@app.route('/delete_game/<game_id>', methods=['GET', 'POST', 'DELETE'])
def delete_game(game_id):
    """Delete a specific game"""
    try:
        instructor = Instructor.query.filter_by(email=session['instructor_email']).first()
        session['instructor_name'] = instructor.name
        db.session.delete(Game.query.filter_by(id=game_id, instructor_id=instructor.id).first())
        db.session.commit()
        response = "Deleted game"
        return redirect("/instructor_dashboard")
    except:
        flash("No games to delete")
        return redirect("/instructor_dashboard")

if __name__=="__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)