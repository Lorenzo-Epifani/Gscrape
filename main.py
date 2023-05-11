import sys
import controller

def _controller(cl_args):
    entry_function = controller.cmd_to_f.get(cl_args[0],'CMD_NOT_FOUND')
    if entry_function=='CMD_NOT_FOUND':
        raise Exception(entry_function)
    entry_function()

if __name__ == '__main__':
    cl_args=sys.argv[1:]


    #plt.ion()
    _controller(cl_args)
