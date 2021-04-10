from flask import flash, render_template, redirect, request
from FlaskExercise import app


@app.route('/')
def home():
    log = request.values.get('log_button')
    # TODO: Appropriately log the different button presses
    #   with the appropriate log level.
    if log == 'info':
        app.logger.info('info Log Test')
    elif log == 'warning':
        app.logger.warning('warning Log Test')
    elif log == 'error':
        app.logger.error('error Log Test')
    elif log == 'critical':
        app.logger.critical('critical Log Test')
    else:
        pass
    
    return render_template(
        'index.html',
        log=log
    )
