from flask import Flask
from src.model.java_command import JavaCommand
from src.model.execute import Execute
from src.model.parameter import Parameter

app = Flask(__name__)


@app.route('/', methods=['POST'])
def route():
    print('test')
    java_command = JavaCommand()
    execute = Execute()
    parameter = Parameter('D:/EjemploJava8.java', 'D:/ ')
    command = java_command.build(parameter)
    result = execute.run(command)
    return result


if __name__ == '__main__':
    app.run()

