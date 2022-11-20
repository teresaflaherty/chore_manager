import subprocess

if __name__ == "__main__":
    p = subprocess.Popen(['python', 'chore_timer.py'])
    p = subprocess.Popen(['python', 'flask_app.py'])

    p.wait()
