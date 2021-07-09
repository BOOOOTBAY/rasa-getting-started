"""debugger for rasa"""
import sys
import rasa

def run(command: str):
    sys.argv = command.split()
    from rasa import __main__
    __main__.main()


# run nlu model
# run("rasa train nlu -u ./data/nlu")

# train core model
# run("rasa train core")

# run shell command
run("rasa shell --debug")
