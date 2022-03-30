from src.model.java_command import JavaCommand


if __name__ == '__main__':
    print("test...")
    javaCommand = JavaCommand()
    print(javaCommand.build('D:/EjemploJava8.java', 'D:/ '))
