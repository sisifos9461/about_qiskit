from IPython.display import display, Markdown, Math
import numpy as np
import math
from fractions import Fraction

def num_to_latex(num, precision=5):
    """Takes a complex number as input and returns a latex representation
    
        Args:
            num (numerical): The number to be converted to latex.
            precision (int): If the real or imaginary parts of num are not close
                             to an integer, the number of decimal places to round to
        
        Returns:
            str: Latex representation of num
    """
    r = np.real(num)
    i = np.imag(num)
    common_factor = None
    
    # try to factor out common terms in imaginary numbers
    if np.isclose(abs(r), abs(i)) and not np.isclose(r, 0):
        common_factor = abs(r)
        r = r/common_factor
        i = i/common_factor
    
    common_terms = {
        1/math.sqrt(2): '\\tfrac{1}{\\sqrt{2}}',
        1/math.sqrt(3): '\\tfrac{1}{\\sqrt{3}}',
        math.sqrt(2/3): '\\sqrt{\\tfrac{2}{3}}',
        math.sqrt(3/4): '\\sqrt{\\tfrac{3}{4}}',
        1/math.sqrt(8): '\\tfrac{1}{\\sqrt{8}}'
    }
    def proc_value(val):
        # See if val is close to an integer
        val_mod = np.mod(val, 1)
        if (np.isclose(val_mod, 0) or np.isclose(val_mod, 1)):
            # If so, return that integer
            return str(int(np.round(val)))
        # Otherwise, see if it matches one of the common terms
        for term, latex_str in common_terms.items():
             if np.isclose(abs(val), term):
                    if val > 0:
                        return latex_str
                    else:
                        return "-" + latex_str
        # try to factorise val nicely
        frac = Fraction(val).limit_denominator()
        num, denom = frac.numerator, frac.denominator
        if num + denom < 20:
            if val > 0:
                return ("\\tfrac{%i}{%i}" % (abs(num), abs(denom)))
            else:
                return ("-\\tfrac{%i}{%i}" % (abs(num), abs(denom)))
        else:
            # Failing everything else, return val as a decimal
            return "{:.{}f}".format(val, precision).rstrip("0")
    
    if common_factor != None:
        common_facstring = proc_value(common_factor)
    else:
        common_facstring = None
    realstring = proc_value(r)
    if i > 0:
        operation = "+"
        imagstring = proc_value(i)
    else:
        operation = "-"
        imagstring = proc_value(-i)
    if imagstring == "1":
        imagstring = ""
    if imagstring == "0":
        return realstring
    if realstring == "0":
        if operation == "-":
            return "-{}i".format(imagstring)
        else:
            return "{}i".format(imagstring)
    if common_facstring != None:
        return "{}({} {} {}i)".format(common_facstring, realstring, operation, imagstring)
    else:
        return "{} {} {}i".format(realstring, operation, imagstring)

def vector_to_latex(vector, precision=5, pretext=""):
    """Latex representation of a complex numpy array (with dimension 1)

        Args:
            vector (ndarray): The vector to be converted to latex, must have dimension 1.
            precision: (int) For numbers not close to integers, the number of decimal places to round to.
            pretext: (str) Latex string to be prepended to the latex, intended for labels.
        
        Returns:
            str: Latex representation of the vector
    """
    out_string = "$$\n{}".format(pretext)
    out_string += "\\begin{bmatrix}\n"
    for amplitude in vector:
        num_string = num_to_latex(amplitude, precision=precision)
        out_string += num_string + " \\\\\n"
    if len(vector) != 0:
        out_string = out_string[:-4] + "\n" # remove trailing characters
    out_string += "\\end{bmatrix}\n"
    return out_string
