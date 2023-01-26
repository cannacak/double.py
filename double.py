import numpy as np
def double(in) -> 'double type array':

    out = in.astype(np.float32)

    out /= 255 #to be able to divide by 255 it has to be converted float32 datatype
    out = np.around(out) #all the values except '0's become '1'. Same as double() in MatLab

    out = out.astype(np.uint8) 
    out  *= 255 #rescaling

    return out
