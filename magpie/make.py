
ROOT = 'classpath/'
INTO = 'target/'

SOURCE = 8
import os
import subprocess

def main():

    ##
    # compile the class files    
    os.makedirs('target/classes/', exist_ok=True)
    result = subprocess.run(
        ['javac', 
            '-cp', ROOT,
            '-d',  INTO+'classes/',
            '-g:none',
            '--source', str(SOURCE),
            '--source-path', ROOT,

            # this will recompile everything int he directory, but, we still need to provide a starting file name
            (ROOT + 'java/lang/Object.java')
        ],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )


if '__main__' == __name__:
    main()

