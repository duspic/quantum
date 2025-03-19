import numpy as np

def qubit_to_bloch(qubit_state):
    """
    Convert a 2D qubit state [alpha, beta] to its 3D Bloch sphere representation (x, y, z).
    """
    alpha, beta = qubit_state  # Extract components
    x = 2 * np.real(np.conj(alpha) * beta)
    y = 2 * np.imag(np.conj(alpha) * beta)
    z = np.abs(alpha)**2 - np.abs(beta)**2
    return np.array([x,y,z])
 
# following the linked doc
def construct_u2_matrix(phi_arg, lambda_arg):
    return np.array([
        [1, -np.exp(lambda_arg * 1j)],
        [np.exp(1j*phi_arg), np.exp(1j*(phi_arg+lambda_arg))]
    ]) * 1/np.sqrt(2)
