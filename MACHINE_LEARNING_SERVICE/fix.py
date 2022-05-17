def fix_machine():
    filename = "./opt/conda/lib/python3.9/site-packages/keras_vggface/models.py"
    text = open(filename).read()
    open(filename, "w+").write(text.replace('keras.engine.topology', 'keras.utils.layer_utils'))
    print(filename)


if __name__ == '__main__':
    fix_machine()
